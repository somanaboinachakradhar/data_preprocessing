# streamlit_netflix_cleaner.py

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from scipy import stats
import openpyxl
import io

st.set_page_config(page_title="Netflix Data Cleaner", layout="wide")

# --- Functions from your script ---

def handle_outliers(df, numeric_cols):
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[col] = df[col].clip(lower_bound, upper_bound)
    return df

def clean_data(df):
    df = df.copy()

    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna('Unknown')
        elif df[col].dtype in ['int64', 'float64']:
            df[col] = df[col].fillna(df[col].median())

    text_cols = df.select_dtypes(include=['object']).columns
    for col in text_cols:
        df[col] = df[col].str.strip().str.lower()

    if 'date_added' in df.columns:
        df['date_added'] = df['date_added'].astype(str).str.strip()
        df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
        df['date_added'] = df['date_added'].apply(lambda x: x.strftime('%Y-%m-%d') if pd.notnull(x) else '')
        df['year_added'] = pd.to_datetime(df['date_added'], errors='coerce').dt.year
        df['month_added'] = pd.to_datetime(df['date_added'], errors='coerce').dt.month

    if 'duration' in df.columns:
        df['duration_value'] = df['duration'].str.extract(r'(\d+)').astype(float)
        df['duration_unit'] = df['duration'].str.extract(r'(\D+)').fillna('min')
        df = df.drop('duration', axis=1)

    df = df.drop_duplicates()
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    df = handle_outliers(df, numeric_cols)

    return df

def to_excel_download(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl', datetime_format='YYYY-MM-DD') as writer:
        df.to_excel(writer, index=False, sheet_name='Cleaned Data')
    output.seek(0)
    return output

# --- Streamlit UI ---

st.title("🎬 Netflix Data Cleaner & Formatter")
st.markdown("Upload your **CSV** file and get a cleaned and formatted Excel file ready for use!")

uploaded_file = st.file_uploader("📁 Upload your Netflix CSV file", type=["csv"])

if uploaded_file:
    st.success("File uploaded successfully!")
    try:
        df = pd.read_csv(uploaded_file)
        st.subheader("📊 Raw Data Preview")
        st.dataframe(df.head())

        if st.button("🧹 Clean & Process Data"):
            with st.spinner("Cleaning in progress..."):
                cleaned_df = clean_data(df)
                st.success("✅ Cleaning complete!")

                st.subheader("📄 Cleaned Data Preview")
                st.dataframe(cleaned_df.head())

                # Download links
                excel_bytes = to_excel_download(cleaned_df)
                st.download_button("📥 Download Cleaned Data (Excel)", data=excel_bytes, file_name="cleaned_netflix_data.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

                sample_bytes = to_excel_download(cleaned_df.head(100))
                st.download_button("📥 Download Sample Data (Excel)", data=sample_bytes, file_name="cleaned_netflix_data_sample.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    except Exception as e:
        st.error(f"⚠️ Error processing file: {str(e)}")
