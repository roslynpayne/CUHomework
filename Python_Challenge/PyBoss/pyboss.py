import os
import csv
import datetime
PyBoss1 = os.path.join('raw_data','employee_data1.csv')
#creating another file so i don't mess up the data trying to overwrite it
FinalBoss1 = os.path.join('raw_data','employee_data1_final.csv')
#state dictionary provided
us_state_abbrev = {
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
#new column headers
Emp_ID = []
First_Name = []
Last_Name = []
DOB = []
SSN = []
STATE = []
#read original csv
with open(PyBoss1) as employee_info:
    csvreader = csv.DictReader(employee_info)
for row in csvreader:
    Emp_ID = Emp_ID + [row['Emp ID']]
# gather names then split them
Full_Name = row['Name'].split(' ')
First_Name = First_Name + [Full_Name[0]]
Last_Name = Last_Name + [Full_Name[1]]
#socials - couldn't figure out how to add the *'s before the last 4
fullssn = row['SSN'].split('-')
last4_ssn = [fullssn[2]]
SSN = SSN + last4_ssn
#states
st = us_state_abbrev[row["State"]]
STATE = STATE + [st]
#DOB
original_dob = datetime.datetime.strptime(row['DOB'], '%Y-%m-%d')
new_dob = original_dob.strftime('%m-%d-%Y')
DOB = DOB + [new_dob]
PyBoss1_reformated = zip(Emp_ID,First_Name,Last_Name,DOB,SSN,STATE)
#final step... creating the new file
with open(FinalBoss1, "w", newline="") as datafile:
    writer = csv.writer(datafile)
writer.writerow(["Emp ID", "First Name", "Last Name",
"DOB", "SSN", "State"])
writer.writerows(PyBoss1_reformated)  