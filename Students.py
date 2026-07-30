
students = [
    ["Rahul", 20, 19], 
    ["Priya", 20, 14],  
    ["Amit", 20, 16],  
    ["Sneha", 20, 18],   
    ["Ananya", 20, 13]  
]


processed_students = []

for idx, student in enumerate(students):
    name, total, present = student[0], student[1], student[2]
    
   
    percentage = (present / total) * 100
    

    if percentage >= 95:
        category = "Excellent"
    elif 85 <= percentage <= 94:
        category = "Good"
    elif 75 <= percentage <= 84:
        category = "Average"
    else:
        category = "Poor"
        
    processed_students.append([name, total, present, percentage, category])

print("--- Students with Poor Attendance (<75%) ---")
for student in processed_students:
    if student[4] == "Poor":
        print(f"Name: {student[0]}, Attendance: {student[3]}%")
print()


highest_percentage = 0
highest_student = ""

for student in processed_students:
    if student[3] > highest_percentage:
        highest_percentage = student[3]
        highest_student = student[0]

print(f"Highest Attendance: {highest_percentage}% by {highest_student}\n")


processed_students.sort(key=lambda x: x[3], reverse=True)

print("--- All Students Sorted by Attendance ---")
for student in processed_students:
    print(f"Name: {student[0]} | Percentage: {student[3]}% | Category: {student[4]}")
