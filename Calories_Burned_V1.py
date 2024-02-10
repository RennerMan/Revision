tot_calories = 0
biking_hours = int(input("How many hours did you bike?"))
jogging_hours = int(input("How many hours did you jog?"))
swimming_hours = int(input("How many hours did you swim?"))
tot_calories += 200 * biking_hours + 475 * jogging_hours + 275 * swimming_hours
weight = 3500 / tot_calories * .454
print(f"The total weight loss from someone who bikes for {biking_hours} hours")
print(f"jogs for {jogging_hours} hours and swims for {swimming_hours} hours is {weight.__round__(2)} kgs")
