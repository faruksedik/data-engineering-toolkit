# Data Engineering Toolkit

The **Data Engineering Toolkit** is a collection of scripts and resources designed to simplify and demonstrate key data engineering tasks.  

This toolkit covers common processes such as:  
- **Data Cleaning** → Removing duplicates, handling missing values, standardizing columns.  
- **Data Transformation** → Applying transformations and feature engineering.  
- **Data Loading** → Saving processed data to files or databases.  

It provides reusable utilities that can be easily extended to real-world projects.


## Documentation

### 1. Data Cleaning Script (`scripts/data_cleaning.py`)
- **Purpose:** Automates basic data cleansing tasks (removes duplicates and handles missing values).  
- **Usage:**  
  ```bash
  df_clean = clean_data(df)
  ```

### 2. Data Transformation Script (`scripts/data_transformation.py`)
- **Purpose:** Applies transformations to cleaned data (feature creation, aggregations, type conversions).  
- **Usage:**  
  ```bash
  df_transformed = transform_data(df_clean)
  ```

### 3. Data Loading Script (`scripts/data_loading.py`)
- **Purpose:** Saves transformed data to CSV.  
- **Usage:**  
  ```bash
  load_data(df_transformed, "output_data.csv")
  ```

### 4. Main Pipeline Runner (`main.py`)
- **Purpose:** Runs the entire ETL pipeline in one command from CLI.  
- **Usage:**  
  ```bash
  python main.py
  ```

## Code Example(s)

### Running Full Pipeline from CLI

```bash
python main.py
```

## Contribution Guide

We welcome contributions! To contribute follow these steps:

1. **Fork the repository on GitHub.**

2. **Clone your fork locally:**
   ```bash
   git clone https://github.com/faruksedik/data-engineering-toolkit.git
   ```   
3. **Create a new branch for your feature:**
   ```bash
   git checkout -b feature/name-of-feature
   ```
4. **Make your changes and commit:**
   ```bash
   git add .
   git commit -m "Add new feature"
   ```
5. **Push to your fork:**
   ```bash
   git push origin feature/name-of-feature
   ```
6. **Submit a Pull Request from `feature/name-of-feature` to `develop` with details about your changes.**

## License

This project is licensed under the **MIT License**
 

