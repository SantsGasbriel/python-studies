distance = float(input("Enter a distance in meters: "))
print(f"The measure of {distance}m corresponds to: ")
km = distance / 1000
hm = distance / 100
dam = distance / 10
dm = distance * 10
cm = distance * 100
mm = distance * 1000
print(f"{km}km.\n{hm}hm.\n{dam}dam.\n{dm}dm.\n{cm}cm.\n{mm}mm.")