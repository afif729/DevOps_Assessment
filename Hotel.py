Bookings = [
    ["Aman", "Standard", 2500, 5, 0],
    ["Vivek", "Standard", 2500, 7, 0],
    ["Lalit", "Luxury", 6500, 4, 0]
]

# Calculate individual bills (Price * Days)
for room in Bookings:
    room[-1] += room[-2] * room[-3]

# Calculate total revenue
totalrev = 0
for room in Bookings:
    totalrev += room[-1]

# Count room types
Standard = 0
Luxury = 0
for room in Bookings:
    if room[1] == "Standard":
        Standard += 1
    else:
        Luxury += 1


highest_Bill = 0
highest = ""
for room in Bookings:
    if highest_Bill < room[-1]:
        highest_Bill = room[-1]
        highest = room[0]

for room in Bookings:
    print(room[0], ":", room[-1])

print("Guest with Highest Bill : ", highest)
print("No of Standard Rooms : ", Standard)
print("No of Luxury Rooms : ", Luxury)
print("Total Revenue of Hotel : ", totalrev)
