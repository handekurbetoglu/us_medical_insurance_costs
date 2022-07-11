import csv

ages = []
sexes = []
bmis = []
children = []
smoker = []
region = []
bmi_numbers = []
charges = []

def create_list_data(converted_list, insurance_csv, column_name):
    with open('insurance.csv', 'r+') as insurance_csv:
        csv_dict = csv.DictReader(insurance_csv)
        for row in csv_dict:
            converted_list.append(row[column_name])
        return converted_list

create_list_data(ages, 'insurance.csv', 'age')
create_list_data(sexes, 'insurance.csv', 'sex')
create_list_data(bmis, 'insurance.csv', 'bmi')
create_list_data(children, 'insurance.csv', 'children')
create_list_data(smoker, 'insurance.csv', 'smoker')
create_list_data(region, 'insurance.csv', 'region')
create_list_data(charges, 'insurance.csv', 'charges')

bmi_numbers = [float(i) for i in bmis]


class Patients:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, 
                 patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges

    def analyze_ages(self):
        sum_age = 0 
        for age in self.patients_ages:
            sum_age += age
        return ("The average age of the patients is :" + str(sum_age / len(self.patients_ages)))
    
    def min_max_ages(self):
        min_age = min(self.patients_ages())
        max_age = max(self.patients_ages())
        return ("The youngest person's age is: " + str(min_age) + '\n' + "The oldest person's age is: " + str(max_age))

    def analyze_sexes(self):
        females=0
        males=0
        for sex in self.patients_sexes:
            if sex == "male":
                males +=1
            elif sex == "female":
                females +=1
        print("The " + str(round((males/len(self.patients_ages)*100),2)) + "% of the population is male, and " + str(round(100-((males/len(self.patients_ages)*100)),2)) + "% of the poulation is female")
        if abs(round((males/len(self.patients_ages)*100),2) - 50) <= 4:
            print("The data is almost evenly distributed in sex-wise")

    def analyze_bmis(self):
        total_bmi = 0
        for bmi in self.patients_bmis:
            total_bmi += bmi
        print("Average bmi index is: " + str(round(total_bmi/ len(self.patients_bmis),2)))

    def analyze_weight(self):
        under_weighted = 0
        healthy_weighted = 0
        over_weighted = 0
        obese = 0
        severe_obese = 0
        for bmi in self.patients_bmis:
            if bmi >= 40:
                severe_obese +=1
            elif bmi > 30:
                obese +=1
            elif bmi >= 25:
                over_weighted +=1
            elif bmi >= 18.5:
                healthy_weighted +=1
            elif bmi < 18.5:
                under_weighted +=1
        print("The " + str(round((under_weighted)/len(bmi_numbers)*100,2)) + "% of the people are listed in under-weight range")
        print("The " + str(round((healthy_weighted)/len(bmi_numbers)*100,2)) + "% of the people are listed in healthy range")
        print("The " + str(round((over_weighted)/len(bmi_numbers)*100,2)) + "% of the people are listed in over-weighted range")
        print("The " + str(round((obese)/len(bmi_numbers)*100,2)) + "% of the people are listed in obese range")
        print("The " + str(round((severe_obese)/len(bmi_numbers)*100,2)) + "% of the people are listed in severe obese range")



patients_info = Patients(ages, sexes, bmi_numbers, children, smoker, region, charges)
patients_info.analyze_bmis()
patients_info.analyze_sexes()
patients_info.analyze_weight()
patients_info.percentage_weight()