import random
import json

stateorcountries = input("Would you like to practice states or countries? (s or c) ")
countries = []
capitals = []

if stateorcountries == 'c':
    file = open("countries.txt", "r")
    countries_capitals = file.readlines()
    for line in countries_capitals:
        line = line.strip()
        word = line.split("@")
        countries.append(word[0])
        capitals.append(word[1])
    file.close()
else:
    file = open("states.json", "r")
    countries_capitals = json.load(file)
    for country in countries_capitals.keys():
        countries.append(country)
    for capital in countries_capitals.values():
        capitals.append(capital)
    file.close()

def qanda(index):
    answer = input(f"What is the capital of {incorrect_countries[index]}? ")
    if answer.lower() == incorrect_capitals[index].lower():
        return True
    else:
        return

def straight(index):
    if qanda(index):
        print("Correct!")
        incorrect_countries.pop(index)
        incorrect_capitals.pop(index)
    else:
        print(f"Incorrect, the answer was {incorrect_capitals[index]}.")
    if len(incorrect_countries) == 0:
        print("You got all of the capitals correct! Good job!")
    return None

continues = "y"
incorrect_countries = countries
incorrect_capitals = capitals
correct_countries = []
while continues == 'y':
    index = random.choice(range(0,len(incorrect_countries)))
    straight(index)
    continues = input("Would you like another question? (y or n) ")
    if len(incorrect_countries) == 0:
        print("You got all of them correct! Good job!")
        countinues = 'n'
    correct_countries.append(countries[index-1])

file = open("known_countries.txt", "w")
for country in countries:
    if country in correct_countries:
        file.write(country)
        file.write('\n')
file.close()
