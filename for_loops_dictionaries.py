students = {
    "male": ["Stacy", "Jackie", "Ryan", "Kim"],
    "female": ["Monique", "Della", "Cicely", "Franjesca", "Syrah"]
}

#for key in students.keys():
#    print(key)

#Print all names in Students' dictionary that has an "a" in it
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)