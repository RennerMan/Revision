lightning_time = float(input("How many seconds were there approximately\
 between the lightning and thunder?")).__round__(2)
sound = 340 * lightning_time / 1000
print(f"The lightning was around {sound.__round__(2)} kilometers away")
