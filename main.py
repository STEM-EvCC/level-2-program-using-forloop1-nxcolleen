mission_names = ['Apollo_11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

amount_of_missions = len(mission_names)
successes = sum(mission_success)
success_percent = (successes / amount_of_missions) * 100
before_2000 = [x for x in mission_years if x < 2000]
for x in mission_years:
    if x >= 2000:
        mission_names.remove('Curiosity Rover')
print("Total number of missions: " + str(amount_of_missions))
print("Number of successful missions: " + str(successes))
print(f"Success rate: {success_percent:.2f}%")
print("Missions launched before the year 2000:")
print(mission_names)
print(before_2000)
exit()

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
for x in "banana":
    print(x)

for x in range(6):
    print(x)
    if x == 4:
        break # else does not print
else:
    print("Finished Printing")
adjective = ["tasty", "big", "juicy"]
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    for y in adjective:
        print(x, y)

for x in range(6):
    pass

for fizzbuss in range(100):
    if fizzbuzz % 3 and fizzbuzz % 5 == 0:
        print("Fizzbuzz")
    if fizzbuzz % 3 == 0:
        print("Fizz")
    if fizzbuzz % 5 == 0:
        print("Buzz")
    else:
        print(str(fizzbuzz))
    variable = 12.234567
    print(f"This is the value {variable:.2f}%")