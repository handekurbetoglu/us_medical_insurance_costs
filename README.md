# Analysis of Insurance Costs in US 

## Overview
This project analyzes health insurance data to understand the relationships between various factors, such as age, sex, BMI, smoking habits, and region, and their impact on insurance charges. The data is sourced from insurance.csv from kaggle.

## Data Description
The dataset contains the following columns:

age: Age of the individual
sex: Gender of the individual (male/female)
bmi: Body Mass Index (BMI) of the individual
children: Number of children the individual has
smoker: Smoking status (yes/no)
region: Geographic region of residence (northwest, northeast, southwest, southeast)
charges: Medical insurance charges billed to the individual

## Analysis Outline
The project consists of a Python script that:

1. Extracts data from the CSV file into lists.
2. Defines a Patients class to perform data analysis.
3. Analyzes the dataset using various metrics, such as average BMI, smoker ratio, and regional variations.
   
## Data Extraction
The function create_list_data is used to extract data from the insurance.csv file into Python lists for further analysis

## Patients Class
The Patients class is designed to encapsulate the analysis of the extracted data. It provides methods to compute various statistics, such as average age, gender distribution, BMI analysis, and smoker ratio.

### Example Usage
class Patients:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges

    def analyze_ages(self):
        sum_age = sum(self.patients_ages)
        return ("The average age of the patients is :" + str(sum_age / len(self.patients_ages)))
    
    def min_max_ages(self):
        min_age = min(self.patients_ages)
        max_age = max(self.patients_ages)
        print("The youngest person's age is: " + str(min_age) + '\n' + "The oldest person's age is: " + str(max_age))

    def analyze_sexes(self):
        females = self.patients_sexes.count("female")
        males = len(self.patients_ages) - females
        male_percent = round((males/len(self.patients_ages)*100),2)
        female_percent = round(100 - male_percent, 2)
        print(f"The {male_percent}% of the population is male, and {female_percent}% is female.")
        if abs(male_percent - 50) <= 4:
            print("The data is almost evenly distributed sex-wise.")

    def analyze_bmis(self):
        total_bmi = sum(self.patients_bmis)
        print("Average BMI index is: " + str(round(total_bmi / len(self.patients_bmis), 2)))

    def unique_region(self):
        regions = {region: self.patients_regions.count(region) for region in set(self.patients_regions)}
        print(regions)

    def analyze_smoker_ratio(self):
        smoker_total = self.patients_smoker_statuses.count("yes")
        non_smoker_total = self.patients_smoker_statuses.count("no")
        smoker_ratio = round((smoker_total / len(self.patients_smoker_statuses)) * 100, 2)
        nonsmoker_ratio = round((non_smoker_total / len(self.patients_smoker_statuses)) * 100, 2)
        print(f"{smoker_ratio}% of the population smokes whereas {nonsmoker_ratio}% are non-smokers.")

### Analysis Example
The following code demonstrates how to use the Patients class to analyze the data:

    patients_info = Patients(ages_number, sexes, bmi_numbers, children_number, smoker, region, charges_number)

    # Analyze various statistics
    patients_info.analyze_bmis()
    patients_info.analyze_sexes()
    patients_info.min_max_ages()
    patients_info.analyze_smoker_ratio()
    patients_info.unique_region()

## Sample Outputs
**Average BMI Index**: 30.66 (Obese range)
**Sex Distribution**: 50.52% male, 49.48% female
**Regional Distribution:** {'southwest': 325, 'southeast': 364, 'northwest': 325, 'northeast': 324}
**Smoker Ratio:** 20.68% smokers, 79.32% non-smokers


## Region-Based Analysis
Further analysis is conducted to examine regional differences in BMI, smoking ratio, and insurance charges.
  Regional Analysis Results
  Southwest Region: Average BMI - 30.6
  Southeast Region: Average BMI - 33.36
  Northwest Region: Average BMI - 29.2
  Northeast Region: Average BMI - 29.17

## Conclusion
The analysis reveals significant insights into the health conditions of individuals based on various factors, like BMI, smoking habits, and geographic regions. Notably, smoking and high BMI are strong predictors of higher insurance charges.


