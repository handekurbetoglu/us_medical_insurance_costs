import csv

ages = []
sexes = []
bmis = []
children = []
smoker = []
region = []
charges = []


with open('insurance.csv', 'r+') as insurance_file:
    csv_dict = csv.DictReader(insurance_file)