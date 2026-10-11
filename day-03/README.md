# Facility Data Analysis Using Python

## Project Objective
Analyze facility data to identify data-quality issues, calculate key statistics, discover patterns, and visualize cleanliness, waste levels, footfall, and complaints.

## Technologies Used
Python, Pandas, NumPy, Matplotlib, Jupyter Notebook.

## Dataset Description
`facility_data.csv` contains 100 facility records with 9 columns, including location, cleanliness score, odor score, waste level, water availability, footfall, complaints, and inspection date.

## Project Workflow
1. Import libraries
2. Load the original dataset
3. Explore dataset structure and data types
4. Check missing values and duplicate records
5. Identify invalid cleanliness scores
6. Investigate potential outliers in footfall and complaints
7. Clean missing and invalid score values
8. Convert inspection dates to datetime format
9. Save the cleaned dataset
10. Calculate summary statistics
11. Analyze waste levels and water availability
12. Compare average cleanliness by location
13. Identify key findings
14. Create and save five visualizations

## Actual Results From This Project
- Original dataset records: 100
- Dataset columns: 9
- Missing values after cleaning: 0
- Duplicate rows after cleaning: 0
- Facilities reporting unavailable water: 26%
- Facilities with high waste levels: 33%
- Highest average cleanliness: Residential (9.00)
- Lowest average cleanliness: Industrial (5.43)
- Potential outliers identified: Footfall of 5,000 and complaints of 100
- Visualizations created: 5

## How to Run
1. Clone or download the repository.
2. Open a terminal in the repository folder.
3. Install the required libraries:

   `pip install pandas numpy matplotlib jupyter`

4. Run `jupyter notebook`.
5. Open `data-cleaning/data_cleaning.ipynb` from the `day-03` folder.
6. Run the cleaning notebook cells from top to bottom.
7. Open `analysis/analysis.ipynb` and run its cells.
8. Open `visualizations/facility_visualizations.ipynb` and run its cells.

The cleaning notebook creates `cleaned_facility_data.csv`, which is used by the analysis and visualization notebooks.

### VS Code
Open the repository folder in VS Code, open each notebook, select a Python kernel, and run the cells from top to bottom using **Run All** or **Shift + Enter**.

## Expected Files
- `dataset/facility_data.csv`
- `dataset/cleaned_facility_data.csv`
- `data-cleaning/data_cleaning.ipynb`
- `analysis/analysis.ipynb`
- `visualizations/facility_visualizations.ipynb`
- `visualizations/01_cleanliness_by_location.png`
- `visualizations/02_facilities_by_waste_level.png`
- `visualizations/03_footfall_distribution.png`
- `visualizations/04_footfall_vs_complaints.png`
- `visualizations/05_complaints_boxplot.png`
- `README.md`

## Conclusion
The project demonstrates data cleaning, exploratory data analysis, statistical summaries, and visualization. The findings highlight differences in cleanliness across locations, water availability concerns, waste-management issues, and unusual values that require further investigation.