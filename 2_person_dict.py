person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person.get("children")[1])
print(person["children"][1])  # same thing


print(type(person["pets"]))
print(person["pets"]["cat"])
for i in person["children"]:
    print(i)

    # print out the pets in this format;
    #'type of pet: dog name of pet: Fido
for i, j in person["pets"].items():
    print(f"type of pet:{i} name of pet: {j}")
