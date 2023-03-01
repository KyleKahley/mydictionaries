import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

'''''
mydictionary = dict(m=8 , n= 9)
print(mydictionary)
print(f"Number of key-value parts: {len(phonebook)} ")  # this prints the amount of elements in the dictionary, there are three keys value pairs 

print()
print('*****  start section 1 - print dictionary ********')
print()





print()
print('*****  end section 1 ********')
print()






print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'
if name in phonebook:
    print(phonebook[name]) # this shows the value of name / Chris if it's in the phonebook dictionary 
else: 
    print(f"{name} does not exist in the phonebook")







print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()
print(phonebook)
phonebook['Chris'] = '555-4444'
phonebook['Joe'] = '555-0123'
print(phonebook)

""

print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)
del phonebook["Chris"]
print(phonebook)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook: 
    print(f"the key is: {key} and the value is {phonebook[key]}")
for value in phonebook.values():
    print(value)
for k, v in phonebook.items():
    print(f'the key is: {key} and the value is {phonebook[key]}')

for ph_tuple in phonebook.items():
    print(ph_tuple)




print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()
name= 'Chris' #if you switched it to chris it would show key not found

phone= phonebook.get(name, 'key not found')

print (phone) # this prints the value of Chris 
phonebook.clear() # this clears the value of Chris
print(phonebook) # this shows the dictionary after it being cleared 



print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

print(phonebook)
remove = phonebook.pop('Chris', 'not found') # pop method takes out the key and value pair of the dictionary, you can see that it was the full dictionary, we removed the key value pair and then printed the dictionary again and it was removed 

print(remove)
print(phonebook)



print()
print('*****  end section 7 ********')
print()

'''''
print()
print('*****  start section 8 - using popitem ********')
print()


a = phonebook.popitem()
print(a)
print(phonebook)



print()
print('*****  end section 8 ********')
print()
'''''


print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
random_key = random.choice(list_of_keys)

print(phonebook[random_key])

#print(phonebook[random.choice(list(phonebook))]) doing this without variables, uses less computing power
print()
print('*****  end section 9 ********')
print()







'''
