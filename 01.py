import math
import data01


# Part 1: Find the total fuel required for all mass

def calculate_fuel(mass):
    return math.floor(float(mass) / 3) - 2


# Convert source data from string to integers and return fuel required for each mass
masses = data01.data.splitlines()
masses = [calculate_fuel(mass) for mass in masses]
masses = [int(mass) for mass in masses]

# Sum and return the total fuel mass
totalMass = sum(masses)
print(f'Solution 1: {int(totalMass)}')

# Part 2: Find the fuel required to convey that fuel, recursively


def calculate_fuel_for_fuel(mass):
    fuel_mass = calculate_fuel(mass)

    if fuel_mass <= 0:
        return 0
    return fuel_mass + calculate_fuel_for_fuel(fuel_mass)


fuel_masses = []
for mass in masses:
    fuel_mass = calculate_fuel_for_fuel(mass)
    fuel_masses.append(mass + fuel_mass)


print(f'Solution 2: {sum(fuel_masses)}')
