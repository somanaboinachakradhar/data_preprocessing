
# Data Cleaner & Formatter

A Streamlit-based data cleaning app for  datasets!  
Upload your  CSV file, automatically clean and preprocess it, and download a cleaned Excel file ready for analysis or visualization.

---

## 📌 Project Overview

This project provides a web-based interface to clean and preprocess  data. It handles missing values, removes outliers, formats date fields, standardizes text, and prepares the dataset for further analysis or visualization — all in a few clicks!

---

## 🧾 Dataset

The app expects a dataset similar to [Netflix Titles Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows), typically structured with columns like:

- `show_id`
- `type`
- `title`
- `director`
- `cast`
- `country`
- `date_added`
- `release_year`
- `rating`
- `duration`
- `listed_in`
- `description`

Sample input used: `netflix_titles.csv`

---

## 🧹 Features

- ✅ Missing value imputation (text and numeric columns)
- ✅ Standardizes text (trimming and lowercasing)
- ✅ Converts `date_added` to `YYYY-MM-DD` and extracts `year_added`, `month_added`
- ✅ Splits `duration` into `duration_value` and `duration_unit`
- ✅ Removes duplicate rows
- ✅ Handles outliers using IQR method
- ✅ Downloads full cleaned dataset or 100-row sample as Excel

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/somanaboinachakradhar/data_preprocessing.git
cd data_preprocessing
```

### 2. Install dependencies

It’s recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```

**Required libraries:**
- `streamlit`
- `pandas`
- `numpy`
- `scikit-learn`
- `scipy`
- `openpyxl`

### 3. Run the app

```bash
streamlit run pycode.py
```

---

## 📥 Example Usage

1. Launch the Streamlit app
2. Upload a Dataset CSV file
3. Click "🧹 Clean & Process Data"
4. Preview the cleaned data
5. Download the full Excel file or a sample

---

## 📂 Project Structure

```
├── pycode.py                # Main Streamlit app
├── netflix_titles.csv       # Sample input file
├── requirements.txt         # Python dependencies
└── README.md                # You're reading it!
```

---

## 🧠 How It Works (Behind the Scenes)

### `clean_data(df)`
- Fills missing `object` fields with `"Unknown"`
- Fills numeric `int/float` fields with median values
- Trims and lowers all text columns
- Parses `date_added`, and creates `year_added`, `month_added`
- Splits `duration` into two new columns
- Removes duplicates
- Clips outliers beyond 1.5*IQR

### `to_excel_download(df)`
- Converts cleaned DataFrame into downloadable Excel format using `openpyxl`

---

## ✍️ Author

**Your Name**  
📫 [chakrisomanaboina432@gmail.com](mailto:chakrisomanaboina432@gmail.com)  
🔗[GitHub](https://github.com/somanaboinachakradhar)

---

## 📄 License

MIT License — feel free to use and modify!
