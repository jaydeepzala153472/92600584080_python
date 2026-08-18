student = {
    "Name" : "jaydeep",
    "Age" : 20,
    "Course" : "MCA",
    "Marks" : 85
    }

print("dictionary: ",student)

print("Keys: ",student.keys())
print("Values: ",student.values())
print("Items: ",student.items())
print("Name: ",student.get("Name"))

student["city"] = "Rajkot"
print("After adding city: ", student)

student["marks"] = 89
print("Afetr updating marks: ",student)

student.pop("Age")
print("After removing age: ",student)

print("\n Dictionary Elements: ")
for key, value in student.items():
    print(key,  ":", value)
