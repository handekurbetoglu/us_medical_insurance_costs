import csv
import json

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
children_number = [int(i) for i in children]
charges_number = [float(i) for i in charges]
ages_number = [float(i) for i in ages]




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
        min_age = min(self.patients_ages)
        max_age = max(self.patients_ages)
        print("The youngest person's age is: " + str(min_age) + '\n' + "The oldest person's age is: " + str(max_age))

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
        return {
            "severe_obese_ratio": str(round((severe_obese)/len(bmi_numbers)*100,2)), 
            "over_weighted_ratio": str(round((over_weighted)/len(bmi_numbers)*100,2)), 
            "obese_ratio": str(round((obese)/len(bmi_numbers)*100,2)),
            "under_weighted_ratio": str(round((under_weighted)/len(bmi_numbers)*100,2)),
            "healthy_weighted_ratio": str(round((healthy_weighted)/len(bmi_numbers)*100,2))
        }

    def unique_region(self):
        regions = {}
        for region in self.patients_regions:
            regions[region] = self.patients_regions.count(region)
        print(regions)

    def analyze_smoker_ratio(self):
        smoker_total = 0
        non_smoker_total = 0
        no_info = 0
        for status in self.patients_smoker_statuses:
            if status == "yes":
                smoker_total+=1
            elif status == "no":
                non_smoker_total+=1
            else:
                no_info+=1
        smoker_ratio = round((smoker_total/len(self.patients_smoker_statuses))*100,2)
        nonsmoker_ratio =round((non_smoker_total/len(self.patients_smoker_statuses))*100,2)
        print(str(smoker_ratio) + "% of the population smokes whereas " + str(nonsmoker_ratio) + "% are non-smoker.")

        

##BMI indexes of regions
region_base_bmi = {}
i = 0
while i < len(bmi_numbers):
    if region[i] not in region_base_bmi:
        region_base_bmi[region[i]] = [bmi_numbers[i]]
    elif region[i] in region_base_bmi:
        region_base_bmi[region[i]].append(bmi_numbers[i])
    i+=1
 
#Average BMI indexes of regions
southwest_avg = (round(float(sum(d for d in region_base_bmi["southwest"])) / len(region_base_bmi["southwest"]),2))
southeast_avg = (round(float(sum(d for d in region_base_bmi["southeast"])) / len(region_base_bmi["southeast"]),2))
northwest_avg = (round(float(sum(d for d in region_base_bmi["northwest"])) / len(region_base_bmi["northwest"]),2))
northeast_avg = (round(float(sum(d for d in region_base_bmi["northeast"])) / len(region_base_bmi["northeast"]),2))

print("Southwest region's average BMI: " + str(southwest_avg))
print("Southeast region's average BMI: " + str(southeast_avg))
print("Northwest region's average BMI: " + str(northwest_avg))
print("Northeast region's average BMI : " + str(northeast_avg))

#The average charges dictionary based on regions(charges are stored).
region_base_charge = {}
i = 0
while i < len(bmi_numbers):
    if region[i] not in region_base_charge:
        region_base_charge[region[i]] = [charges_number[i]]
    elif region[i] in region_base_charge:
        region_base_charge[region[i]].append(charges_number[i])
    i+=1


southwest_avg_charge = (round(float(sum(d for d in region_base_charge["southwest"])) / len(region_base_charge["southwest"]),2))
southeast_avg_charge = (round(float(sum(d for d in region_base_charge["southeast"])) / len(region_base_charge["southeast"]),2))
northwest_avg_charge = (round(float(sum(d for d in region_base_charge["northwest"])) / len(region_base_charge["northwest"]),2))
northeast_avg_charge = (round(float(sum(d for d in region_base_charge["northeast"])) / len(region_base_charge["northeast"]),2))

difference = round(((northeast_avg_charge-northwest_avg_charge)*100)/northeast_avg_charge,2)


#The dictionary based on number of children(charges stored).
children_based_charge = {}
i=0
while i < len(charges_number):
    if children_number[i] not in children_based_charge:
        children_based_charge[children_number[i]] = [charges_number[i]]
    elif children_number[i] in children_based_charge:
        children_based_charge[children_number[i]].append(charges_number[i])
    i+=1
#The dictionary based on smoking status(charges stored).
smoking_based_charge = {}
i=0
while i < len(charges_number):
    if smoker[i] not in smoking_based_charge:
        smoking_based_charge[smoker[i]] = [charges_number[i]]
    elif smoker[i] in smoking_based_charge:
        smoking_based_charge[smoker[i]].append(charges_number[i])
    i+=1



#The dictionary that shows the number of children people have per region.
region_based_children = {}
region_based_children['southwest'] = []
region_based_children['northwest'] = []
region_based_children['southeast'] = []
region_based_children['northeast'] = []

i=0
while i < len(children_number):
    region_based_children[region[i]].append(children_number[i])
    i+=1


sum(d for d in region_based_children['southwest'])/len(region_based_children['southwest'])
sum(d for d in region_based_children['southeast'])/len(region_based_children['southeast'])
sum(d for d in region_based_children['northwest'])/len(region_based_children['northwest'])
sum(d for d in region_based_children['northeast'])/len(region_based_children['northeast'])

print("The average number of children per person for people in southwest is " + str(round(sum(d for d in region_based_children['southwest'])/len(region_based_children['southwest']),2)))
print("The average number of children per person for people in southeast is " + str(round(sum(d for d in region_based_children['southeast'])/len(region_based_children['southeast']),2)))
print("The average number of children per person for people in northwest is " + str(round(sum(d for d in region_based_children['northwest'])/len(region_based_children['northwest']),2)))
print("The average number of children per person for people in northeast is " + str(round(sum(d for d in region_based_children['northeast'])/len(region_based_children['northeast']),2)))


#The dictionary that shows the average of people  per region.

region_based_age = {}
region_based_age['southwest'] = []
region_based_age['northwest'] = []
region_based_age['southeast'] = []
region_based_age['northeast'] = []

i=0
while i < len(children_number):
    region_based_age[region[i]].append(ages_number[i])
    i+=1

print("The average age of people in southwest is " + str(round(sum(d for d in region_based_age['southwest'])/len(region_based_age['southwest']),2)))
print("The average age of people in southeast is " + str(round(sum(d for d in region_based_age['southeast'])/len(region_based_children['southeast']),2)))
print("The average age of people in northwest is " + str(round(sum(d for d in region_based_age['northwest'])/len(region_based_children['northwest']),2)))
print("The average age of people in northeast is " + str(round(sum(d for d in region_based_age['northeast'])/len(region_based_age['northeast']),2)))



#region based charges for smokers and non-smokers.

region_based_charges_smoking = {
    'southeast': {'yes': [], 'no': []},
    'northeast': {'yes': [], 'no': []},
    'northwest': {'yes': [], 'no': []},
    'southwest': {'yes': [], 'no': []},
}

i=0
for place in region:
    current_status = smoker[i]
    if smoker[i] == 'yes':
            region_based_charges_smoking[region[i]][smoker[i]].append(charges_number[i])
    elif smoker[i] == 'no':
            region_based_charges_smoking[region[i]][smoker[i]].append(charges_number[i])
    i+=1

average_smoker_southeast = round(sum(d for d in region_based_charges_smoking['southeast']['yes'])/len(region_based_charges_smoking['southeast']['yes']),2)
average_nonsmoker_southeast = round(sum(d for d in region_based_charges_smoking['southeast']['no'])/len(region_based_charges_smoking['southeast']['no']),2)
average_smoker_southwest = round(sum(d for d in region_based_charges_smoking['southwest']['yes'])/len(region_based_charges_smoking['southwest']['yes']),2)
average_nonsmoker_southwest = round(sum(d for d in region_based_charges_smoking['southwest']['no'])/len(region_based_charges_smoking['southwest']['no']),2)

average_smoker_northeast = round(sum(d for d in region_based_charges_smoking['northeast']['yes'])/len(region_based_charges_smoking['northeast']['yes']),2)
average_nonsmoker_northeast = round(sum(d for d in region_based_charges_smoking['northeast']['no'])/len(region_based_charges_smoking['northeast']['no']),2)
average_smoker_northwest = round(sum(d for d in region_based_charges_smoking['northwest']['yes'])/len(region_based_charges_smoking['northwest']['yes']),2)
average_nonsmoker_northwest = round(sum(d for d in region_based_charges_smoking['northwest']['no'])/len(region_based_charges_smoking['northwest']['no']),2)

print(
    "Smokers pay " + str(round((((average_smoker_northeast-average_nonsmoker_northeast)*100)/average_smoker_northeast),2)) + "% more than non-smokers in Northeast"
)

print(
    "Smokers pay " + str(round((((average_smoker_northwest-average_nonsmoker_northwest)*100)/average_smoker_northeast),2)) + "% more than non-smokers in Northwest"
)


#The dictionary that shows gender counts per region.

region_based_sex = {}
region_based_sex['southwest'] = []
region_based_sex['northwest'] = []
region_based_sex['southeast'] = []
region_based_sex['northeast'] = []

i=0

while i< len(children_number):
    region_based_sex[region[i]].append(sexes[i])
    i+=1

print("southwest female count: " + str(region_based_sex['southwest'].count('female')))
print("nortwest female count: " + str(region_based_sex['northwest'].count('female')))
print("southeast female count: " + str(region_based_sex['southeast'].count('female')))
print("northeast female count: "  + str(region_based_sex['northeast'].count('female')))





region_based_smokers_ratio = {}
i = 0
while i < len(bmi_numbers):
    if region[i] not in region_based_smokers_ratio:
        region_based_smokers_ratio[region[i]] = [smoker[i]]
    elif region[i] in region_based_smokers_ratio:
        region_based_smokers_ratio[region[i]].append(smoker[i])
    i+=1



southwest_smokers_ratio = round((region_based_smokers_ratio["southwest"].count('yes')*100)/len(region_based_smokers_ratio["southwest"]),4)
southeast_smokers_ratio = round((region_based_smokers_ratio["southeast"].count('yes')*100)/len(region_based_smokers_ratio["southeast"]),2)
northwest_smokers_ratio = round((region_based_smokers_ratio["northwest"].count('yes')*100)/len(region_based_smokers_ratio["northwest"]),4)
northeast_smoekrs_ratio = round((region_based_smokers_ratio["northeast"].count('yes')*100)/len(region_based_smokers_ratio["northeast"]),2)



smoker_average_charge = (round(float(sum(d for d in smoking_based_charge["yes"])) / len(smoking_based_charge["yes"]),2))
nonsmoker_average_charge = (round(float(sum(d for d in smoking_based_charge["no"])) / len(smoking_based_charge["no"]),2))
charges_difference_smoking = round((((smoker_average_charge - nonsmoker_average_charge)*100)/smoker_average_charge),2)


zero_child = (round(float(sum(d for d in children_based_charge[0])) / len(children_based_charge[0]),2))
one_child = (round(float(sum(d for d in children_based_charge[1])) / len(children_based_charge[1]),2))
two_children = (round(float(sum(d for d in children_based_charge[2])) / len(children_based_charge[2]),2))
three_children =(round(float(sum(d for d in children_based_charge[3])) / len(children_based_charge[3]),2))
four_children =(round(float(sum(d for d in children_based_charge[4])) / len(children_based_charge[4]),2))
five_children = (round(float(sum(d for d in children_based_charge[5])) / len(children_based_charge[5]),2))


patients_info = Patients(ages_number, sexes, bmi_numbers, children_number, smoker, region, charges_number)
patients_info.analyze_bmis()
patients_info.analyze_sexes()
regions = patients_info.unique_region()
ratios = patients_info.analyze_weight()
patients_info.min_max_ages()



"""
print("The " + ratios["under_weighted_ratio"] + "% of the people are listed in under-weight range")
print("The " + ratios["healthy_weighted_ratio"] + "% of the people are listed in healthy range")
print("The " + ratios["over_weighted_ratio"] + "% of the people are listed in over-weighted range")
print("The " + ratios["obese_ratio"] + "% of the people are listed in obese range")
print("The " + ratios["severe_obese_ratio"] + "% of the people are listed in severe obese range")

"""




print("Soutwest region's average charge: " + str(southwest_avg_charge))
print("Southeast region's average charge: " + str(southeast_avg_charge))
print("Northwest region's average charge: " + str(northwest_avg_charge))
print("Northeast region's average charge: " + str(northeast_avg_charge))

patients_info.analyze_smoker_ratio()
print("Population of smokers have the average charge: " + str(smoker_average_charge))
print("Population of non-smokers have the average charge: " + str(nonsmoker_average_charge))
print("Smokers pay " + str(charges_difference_smoking) + "% more than the non-smokers on average.")



