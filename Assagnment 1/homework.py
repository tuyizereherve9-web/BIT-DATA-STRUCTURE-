# work of field trip attendence

attendance = list(map(int, input("Enter attendance numbers: ").split(",")))
total = sum(attendance)
average = total / len(attendance)
minimum = min(attendance)
maximum = max(attendance)

print("\n--- Field Trip Attendance Report ---")
print(f"Attendance numbers: {attendance}")
print(f"Total Attendance: {total}")
print(f"Average Attendance: {average:.2f}")
print(f"Minimum Attendance: {minimum}")
print(f"Maximum Attendance: {maximum}")

attendance = [1,2,3,4,5]

total = sum(attendance)
average = total / len(attendance)
minimum = min(attendance)
maximum = max(attendance)

report = (
    f"\n--- Field Trip Attendance Report ---\n"
    f"Total students on the trip: {total}\n"
    f"Average students in class: {average:.2f}\n"
    f"Lowest attendance in a class: {minimum}\n"
    f"Highest attendance in a class: {maximum}\n"
)


print(report)

attendance = [1,2,3,4,5]

total = sum(attendance)
average = total / len(attendance)
minimum = min(attendance)
maximum = max(attendance)


threshold = 4
if average > threshold and total > 10:
    status = "Above Standard"
else:
    status = "Below Standard"

print("\n--- Field Trip Attendance Report ---")
print(f"Total students: {total}")
print(f"Average per class: {average:.2f}")
print(f"Lowest class attendance: {minimum}")
print(f"Highest class attendance: {maximum}")
print(f"Status: {status}")

attendance = [1,2,3,4,5]

print("Attendance List:", attendance)


attendance.append(4) 
print("After Adding New class:", attendance)

attendance = [x for x in attendance if x >= 3]
print("After Removing class with < 3 Students:", attendance)

attendance.sort()
print("Sorted Attendance List:", attendance)


import array

attendance_list = [1,2,3,4,5]

attendance_array = array.array('i', attendance_list[:4])  


list_sum = sum(attendance_list)
array_sum = sum(attendance_array)

print("Attendance List:", attendance_list)
print("Sum from List:", list_sum)

print("Attendance Array:", attendance_array.tolist()) 
print("Sum from Array (subset):", array_sum)

if array_sum == list_sum:
    print("Array and List sums are equal.")
else:
    print("Array sum differs from List sum")

attendance_records = [
    {"id": 1, "name": "class 1", "value": 1},
    {"id": 2, "name": "class 2", "value": 2},
    {"id": 3, "name": "class 3", "value": 3},
    {"id": 4, "name": "class 4", "value": 4},
    {"id": 5, "name": "class 5", "value": 5}
]

print("Original Records:")
for record in attendance_records:
    print(record)

for record in attendance_records:
    if record["id"] == 2:
        record["value"] = 4


attendance_records = [record for record in attendance_records if record["id"] != 5]
total = sum(record["value"] for record in attendance_records)

print("\nUpdated Records:")
for record in attendance_records:
    print(record)

print(f"\nTotal Attendance after update & delete: {total}")
