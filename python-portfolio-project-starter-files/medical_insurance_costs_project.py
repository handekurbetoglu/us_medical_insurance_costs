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
        return regions

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


    def children_count(self):
        no_child = 0
        one = 0
        two = 0
        three = 0
        four = 0
        five = 0
        five_plus = 0
        for value in self.patients_num_children:
            if value == 1:
                one+=1
            elif value == 2:
                two+=1
            elif value == 3:
                three+=1
            elif value == 4:
                four+=1
            elif value ==5:
                five+=1
            elif value == 0:
                no_child +=1
            else:
                five_plus +=1
        perc_none = round((no_child/len(children_number)*100),2)
        perc_one = round((one/len(children_number)*100),2)
        perc_two = round((two/len(children_number)*100),2)
        perc_three = round((three/len(children_number)*100),2)
        perc_four = round((four/len(children_number)*100),2)
        perc_five = round((five/len(children_number)*100),2)
        perc_more = round((five_plus/len(children_number)*100),2)
        print("The " +
        str(perc_none) + "% of the people have no child, "
        + str(perc_one) + " people have one child, "
        + str(perc_two) + "% of the people have two children, "
        + str(perc_three) + "% of the people have three children, "
        + str(perc_four) + "% of the people have four children, "
        + str(perc_five) + "% of the people have five children, "
        + str(perc_more) + "% of the people have more than five children."
        )

#It is the dictionary where the whole given data belonging to a patient is stored.
    def create_dictionary(self):
        i=0
        list_dictionary = {}
        while i < len(self.patients_ages):
            list_dictionary[i+1] = [self.patients_ages[i], self.patients_sexes[i], self.patients_bmis[i], self.patients_num_children[i], 
                 self.patients_smoker_statuses[i], self.patients_regions[i], self.patients_charges[i]]
            i+=1
        
        charge_smoker_sex = {}
        charge_smoker_sex["female"] = []
        charge_smoker_sex["male"] = []
        
        i=0
        while i < len (self.patients_ages):
            if list_dictionary[i+1][1] =='female' and list_dictionary[i+1][4] == 'yes':
                charge_smoker_sex["female"].append(list_dictionary[i+1][-1])
            elif list_dictionary[i+1][1] =='male' and list_dictionary[i+1][4] == 'yes':
                charge_smoker_sex["male"].append(list_dictionary[i+1][-1])
            i+=1


        avg_female_smoker = (round(float(sum(d for d in charge_smoker_sex["female"])/ len(charge_smoker_sex["female"])),2))
        avg_male_smoker = (round(float(sum(d for d in charge_smoker_sex["male"])/ len(charge_smoker_sex["male"])),2))
        print("Female smokers pay average " + str(avg_female_smoker) + "$.")
        print("Male smokers pay average " + str(avg_male_smoker) + "$.")
        

    def smokers_age_effect(self):
        i=0
        dict_age_based_smoker = {}
        dict_age_thirty = {}
        dict_age_forty = {}
        dict_age_fifty = {}
        dict_age_fiftyplus = {}

        while i < len(self.patients_charges):
            if self.patients_smoker_statuses[i] == "yes" and self.patients_ages[i] <= 30:
                if  self.patients_smoker_statuses[i] not in dict_age_thirty:
                   dict_age_thirty[ self.patients_smoker_statuses[i]] = [self.patients_charges[i]]
                elif  self.patients_smoker_statuses[i] in dict_age_thirty:
                    dict_age_thirty[ self.patients_smoker_statuses[i]].append(self.patients_charges[i])
                elif  self.patients_smoker_statuses[i] == "no":
                    pass
            i+=1

        i=0
        while i < len(self.patients_charges):
            if  self.patients_smoker_statuses[i] == "yes" and 30 < self.patients_ages[i] and self.patients_ages[i] <= 40:
                if  self.patients_smoker_statuses[i] not in dict_age_forty:
                    dict_age_forty[ self.patients_smoker_statuses[i]] = [self.patients_charges[i]]
                elif   self.patients_smoker_statuses[i] in dict_age_forty:
                    dict_age_forty[self.patients_smoker_statuses[i]].append(self.patients_charges[i])
                elif  self.patients_smoker_statuses[i] == "no":
                    pass
            i+=1

        i=0
        while i < len(self.patients_charges):    
            if self.patients_smoker_statuses[i] == "yes" and 40 < self.patients_ages[i] and self.patients_ages[i] <= 50:
                if self.patients_smoker_statuses[i] not in dict_age_fifty:
                    dict_age_fifty[self.patients_smoker_statuses[i]] = [self.patients_charges[i]]
                elif  self.patients_smoker_statuses[i] in dict_age_fifty:
                    dict_age_fifty[self.patients_smoker_statuses[i]].append(self.patients_charges[i])
                elif  self.patients_smoker_statuses[i] == "no":
                    pass
            i+=1
        
        i=0
        while i < len(self.patients_charges):
            if self.patients_smoker_statuses[i] == "yes" and 40 < self.patients_ages[i] and self.patients_ages[i] > 50:
                if self.patients_smoker_statuses[i] not in dict_age_fiftyplus:
                    dict_age_fiftyplus[self.patients_smoker_statuses[i]] = [self.patients_charges[i]]
                elif  self.patients_smoker_statuses[i] in dict_age_fiftyplus:
                    dict_age_fiftyplus[self.patients_smoker_statuses[i]].append(self.patients_charges[i])
                elif  self.patients_smoker_statuses[i] == "no":
                    pass
            i+=1
        dict_age_based_smoker["-30"] = dict_age_thirty
        dict_age_based_smoker["31-40"] = dict_age_forty
        dict_age_based_smoker["41-50"] = dict_age_fifty
        dict_age_based_smoker["50+"] = dict_age_fiftyplus

        average_smoker_thirty = (round(float(sum(d for d in dict_age_thirty["yes"])) / len(dict_age_thirty["yes"]),2))
        average_smoker_forty = (round(float(sum(d for d in dict_age_forty["yes"])) / len(dict_age_forty["yes"]),2))
        average_smoker_fifty = (round(float(sum(d for d in dict_age_fifty["yes"])) / len(dict_age_fifty["yes"]),2))
        average_smoker_fiftyplus = (round(float(sum(d for d in dict_age_fiftyplus["yes"])) / len(dict_age_fiftyplus["yes"]),2))

        print("Smokers upto 31 years old pay on average: " + str(average_smoker_thirty) + "$")
        print("Smokers aged 31 and 40 pay on average: " + str(average_smoker_forty) + "$")
        print("Smokers aged 41 and 50 pay on average: " + str(average_smoker_fifty) + "$")
        print("Smokers aged 51 and over pay on average: " + str(average_smoker_fiftyplus) + "$")


        i=0
        dict_age_based_nonsmoker = {}
        dict_age_nonsmoker_thirty = {}
        dict_age_nonsmoker_forty = {}
        dict_age_nonsmoker_fifty = {}
        dict_age_nonsmoker_fiftyplus = {}

        while i < len(self.patients_charges):
            if self.patients_smoker_statuses[i] == "no" and self.patients_ages[i] <= 30:
                if  self.patients_smoker_statuses[i] not in dict_age_nonsmoker_thirty:
                   dict_age_nonsmoker_thirty[ self.patients_smoker_statuses[i]] = [self.patients_charges[i]]
                elif  self.patients_smoker_statuses[i] in dict_age_nonsmoker_thirty:
                    dict_age_nonsmoker_thirty[ self.patients_smoker_statuses[i]].append(self.patients_charges[i])
                elif  self.patients_smoker_statuses[i] == "yes":
                    pass
            i+=1

        i=0
        while i < len(self.patients_charges):
            if  self.patients_smoker_statuses[i] == "no" and 30 < self.patients_ages[i] and self.patients_ages[i] <= 40:
                if  self.patients_smoker_statuses[i] not in dict_age_nonsmoker_forty:
                    dict_age_nonsmoker_forty[ self.patients_smoker_statuses[i]] = [self.patients_charges[i]]
                elif   self.patients_smoker_statuses[i] in dict_age_nonsmoker_forty:
                    dict_age_nonsmoker_forty[self.patients_smoker_statuses[i]].append(self.patients_charges[i])
                elif  self.patients_smoker_statuses[i] == "yes":
                    pass
            i+=1

        i=0
        while i < len(self.patients_charges):    
            if self.patients_smoker_statuses[i] == "no" and 40 < self.patients_ages[i] and self.patients_ages[i] <= 50:
                if self.patients_smoker_statuses[i] not in dict_age_nonsmoker_fifty:
                    dict_age_nonsmoker_fifty[self.patients_smoker_statuses[i]] = [self.patients_charges[i]]
                elif  self.patients_smoker_statuses[i] in dict_age_nonsmoker_fifty:
                    dict_age_nonsmoker_fifty[self.patients_smoker_statuses[i]].append(self.patients_charges[i])
                elif  self.patients_smoker_statuses[i] == "yes":
                    pass
            i+=1
        
        i=0
        while i < len(self.patients_charges):
            if self.patients_smoker_statuses[i] == "no" and 40 < self.patients_ages[i] and self.patients_ages[i] > 50:
                if self.patients_smoker_statuses[i] not in dict_age_nonsmoker_fiftyplus:
                    dict_age_nonsmoker_fiftyplus[self.patients_smoker_statuses[i]] = [self.patients_charges[i]]
                elif  self.patients_smoker_statuses[i] in dict_age_nonsmoker_fiftyplus:
                    dict_age_nonsmoker_fiftyplus[self.patients_smoker_statuses[i]].append(self.patients_charges[i])
                elif  self.patients_smoker_statuses[i] == "yes":
                    pass
            i+=1
        dict_age_based_nonsmoker["-30"] = dict_age_nonsmoker_thirty
        dict_age_based_nonsmoker["31-40"] = dict_age_nonsmoker_forty
        dict_age_based_nonsmoker["41-50"] = dict_age_nonsmoker_fifty
        dict_age_based_nonsmoker["50+"] = dict_age_nonsmoker_fiftyplus

        average_nonsmoker_thirty = (round(float(sum(d for d in dict_age_nonsmoker_thirty["no"])) / len(dict_age_nonsmoker_thirty["no"]),2))
        average_nonsmoker_forty = (round(float(sum(d for d in dict_age_nonsmoker_forty["no"])) / len(dict_age_nonsmoker_forty["no"]),2))
        average_nonsmoker_fifty = (round(float(sum(d for d in dict_age_nonsmoker_fifty["no"])) / len(dict_age_nonsmoker_fifty["no"]),2))
        average_nonsmoker_fiftyplus = (round(float(sum(d for d in dict_age_nonsmoker_fiftyplus["no"])) / len(dict_age_nonsmoker_fiftyplus["no"]),2))
        print("Smokers pay on average " + str(round(((((average_smoker_thirty)-(average_nonsmoker_thirty))*100)/average_smoker_thirty),2)) + "% more than non-smokers in age group of 0 and 30")
        print("Smokers pay on average " + str(round(((((average_smoker_forty)-(average_nonsmoker_forty))*100)/average_smoker_forty),2)) + "% more than non-smokers in age group of 31 and 40.")
        print("Smokers pay on average " + str(round(((((average_smoker_fifty)-(average_nonsmoker_fifty))*100)/average_smoker_fifty),2)) + "% more than non-smokers in age group of 41 and 50.")
        print("Smokers pay on average " + str(round(((((average_smoker_fiftyplus)-(average_nonsmoker_fiftyplus))*100)/average_smoker_fiftyplus),2)) + "% more than non-smokers in age group of 51 and over.")



#The bmi index dictionary based on regions(bmi indexes are stored).
region_base_dict = {}
i = 0
while i < len(bmi_numbers):
    if region[i] not in region_base_dict:
        region_base_dict[region[i]] = [bmi_numbers[i]]
    elif region[i] in region_base_dict:
        region_base_dict[region[i]].append(bmi_numbers[i])
    i+=1
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



smoker_average_charge = (round(float(sum(d for d in smoking_based_charge["yes"])) / len(smoking_based_charge["yes"]),2))
nonsmoker_average_charge = (round(float(sum(d for d in smoking_based_charge["no"])) / len(smoking_based_charge["no"]),2))
charges_difference_smoking = round((((smoker_average_charge - nonsmoker_average_charge)*100)/smoker_average_charge),2)

southwest_avg = (round(float(sum(d for d in region_base_dict["southwest"])) / len(region_base_dict["southwest"]),2))
southeast_avg = (round(float(sum(d for d in region_base_dict["southeast"])) / len(region_base_dict["southeast"]),2))
northwest_avg = (round(float(sum(d for d in region_base_dict["northwest"])) / len(region_base_dict["northwest"]),2))
northeast_avg = (round(float(sum(d for d in region_base_dict["northeast"])) / len(region_base_dict["northeast"]),2))

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
patients_info.children_count()



print("The " + ratios["under_weighted_ratio"] + "% of the people are listed in under-weight range")
print("The " + ratios["healthy_weighted_ratio"] + "% of the people are listed in healthy range")
print("The " + ratios["over_weighted_ratio"] + "% of the people are listed in over-weighted range")
print("The " + ratios["obese_ratio"] + "% of the people are listed in obese range")
print("The " + ratios["severe_obese_ratio"] + "% of the people are listed in severe obese range")



print("Soutwest region's average BMI: " + str(southwest_avg))
print("Southeast region's average BMI: " + str(southeast_avg))
print("Northwest region's average BMI: " + str(northwest_avg))
print("Northeast region's average BMI : " + str(northeast_avg))

patients_info.analyze_smoker_ratio()
print("Population of smokers have the average charge: " + str(smoker_average_charge))
print("Population of non-smokers have the average charge: " + str(nonsmoker_average_charge))
print("Smokers pay " + str(charges_difference_smoking) + "% more than the non-smokers on average.")
patients_info.smokers_age_effect()

patient_dictionary = patients_info.create_dictionary()


