import math

# Welcome the user to the sphere calculator
print("Welcome to the Sphere Calculator!")

# Get the radius from the user
radius = float(input("Enter the radius of the sphere: "))

# Calculate the volume using the formula
volume = (4 / 3) * math.pi * radius**3

# Calculate the surface area using the formula
surface_area = 4 * math.pi * radius**2

# Display the results with clear labels
print("Volume of the sphere:", volume)
print("Surface area of the sphere:", surface_area)

# Add a closing message
print("Thank you for using the Sphere Calculator!")
