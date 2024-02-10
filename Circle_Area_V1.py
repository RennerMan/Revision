circle_radius = float(input("how many cm is the radius of the circle?"))
surf_area = 4 * 3.14159 * circle_radius * circle_radius
volume = 4/3 * 3.14159 * circle_radius * circle_radius * circle_radius
print(f"The surface area of the circle is {surf_area.__round__(2)}cm")
print(f"The volume of the circle is {volume.__round__(2)}cm")
