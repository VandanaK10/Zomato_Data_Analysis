# Zomato Data Cleaning and Preprocessing

This project demonstrates how to clean and preprocess the Zomato restaurant dataset using Python and Pandas in a Jupyter Notebook.

## 📁 Files

- `zomato_data_cleaning.ipynb`: Jupyter Notebook with step-by-step data cleaning.
- `requirements.txt`: Python dependencies to run the notebook.
- `README.md`: Project overview and usage instructions.

## 📊 Dataset

Ensure that the file `zomato.csv` is present in the same directory. This dataset is expected to contain restaurant data with features such as location, cost, ratings, etc.

## 🔧 Features of the Notebook

- Drops irrelevant or redundant columns
- Renames key columns for clarity
- Cleans cost and rating columns
- Handles missing values appropriately
- Outputs a cleaned dataset as `zomato_data_analysis.csv`

## 🚀 How to Run

```bash
pip install -r requirements.txt
jupyter notebook zomato_data_cleaning.ipynb
```

## 🧪 Output

- A cleaned version of the original dataset saved as `zomato_data_analysis.csv`.

## 📌 Notes

- The column `approx_cost(for two people)` is cleaned to produce a `cost_per_person` column.
- The `rate` column is transformed into a numeric `rating`.
