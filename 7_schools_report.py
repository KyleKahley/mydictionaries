"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons. This
information can be found in the ValueLabels file.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 50%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""
import json
infile = open('school_data.json', 'r')
schools = json.load(infile)
conference_schools = [372,108,107, 130]
"""""
print(type(schools))

#how many schools are in this file? 
print(len(schools)) #counting the number of dictionaries = number of schools 
#print name school, graduation for conferences, graduation above 80% for women 
for name_school in schools:
    #print(name_school["instnm"]) shows names of all the schools
    print(name)
    conference = name_school["NCAA"]["NAIA conference number football (IC2020)"]
    grad_rate_women = name_school[]
    name = ["instnm"]
    if conference = i in conference_schools:
        print(name)
        print(conference)
"""""

for name_school in schools:
    if name_school["NCAA"]["NAIA conference number football (IC2020)"] in conference_schools:
        if name_school["Graduation rate  women (DRVGR2020)"] > 80: 
            print(name_school["instnm"])
            print(name_school["Graduation rate  women (DRVGR2020)"])
            print()
            print()
    
