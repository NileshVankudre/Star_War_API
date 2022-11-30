# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

""" Task1
Introduction
This is a project that pulls data off star-war API
1. Create a class based generator to produce random numbers
2. Use start and stop as instance attributes.
3. Create a class called "Swapi"
4. Add following methods under `Swapi` class
    - get_planet (to get single of planet)
    - get_planets (to get entire list of planets)
"""
"""Task 2
The task 2 goes like following:
Pull data for the the first movie in star wars
Write the json data into a file named output.txt
"""
from util.randgen import produce_characters
import requests

start = 0
stop = 15

obj = produce_characters()
characters = []

for i in range(start, start + 1):
    characters.append(next(obj))

home_url = "https://swapi.dev"
relative = "/api/people/{0}"  # magic string

if __name__ == '__main__':

    print("current module getting executed")
    for num_ in characters:
        absolute_url = home_url + relative.format(num_)
        print(f"fetching details using :- {absolute_url}  =>\n")
        response = requests.get(absolute_url)
        response = response.json()
        print(response)
        print("######" * 20)
