import csv
import os

csvpath = os.path.join('resources', 'employee_data1.csv')
output_path = "employee_data_cleaned.csv"

states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

states_abr = []
names = []
employee_id = []
bday = []
bday_sorted = []
ssn = []
first_name = []
last_name = []

with open(csvpath, newline='') as csvfile:
    csvread = csv.reader(csvfile, delimiter=',')

    for row in csvread:
        names.append(row[1].split(" "))

        employee_id.append(row[0])

        bday.append(row[2].split("-"))
        
        ssn.append(row[3])

        if row[4] != 'State':
            states_abr.append(states[row[4]])

del names[0]
del employee_id[0]
del bday[0]
del ssn[0]

for row in names:
    first_name.append(row[0])
    last_name.append(row[1])

for row in bday:
    bday_sorted.append(row[1]+ "/" + row[2] + "/" + row[0])


for i in range(0, len(ssn)):
    ssn[i] = ssn[i].replace(ssn[i][0:6], "***-**")
    



final = zip(employee_id, first_name, last_name, bday_sorted, ssn, states_abr)


with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["ID", "First Name", "Last Name", "DOB", "SSN", "State"])
    csvwriter.writerows(final)



