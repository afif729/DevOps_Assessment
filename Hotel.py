Bookings=[["Aman","Standard",2500,5,0],["Vivek","Standard",2500,7,0],["Lalit","Luxury",6500,4,0]]
for _ in Bookings[_]:
  Bookings[_][-1]+=Bookings[_][-2]*Bookings[_][-3]

totalrev=0
for _ in Bookings[_]:
  totalrev+=Bookings[_][-1]
Standard=0
Luxury=0
for _ in Bookings[_]:
  if Bookings[_][1]=="Standard":
    Standard+=1
  else :
    Luxury +=1
highest_Bill=0
for _ in Bookings[_]:
  if highest_Bill < Bookings[_][-1]:
    highest_Bill=Bookings[_][-1]
    highest=Bookings[_][0]
for _ in Bookings[_]:
  print(Bookings[_][0],":",Bookings[_][-1])

print("Guest with Highest Bill : ",highest)
print("No of Standard Rooms : ",Standard)
print("No of Luxury Rooms : ",Luxury)

print("Total Revenue of Hotel : ",totalrev)
