import sys
import math
import random


class Murhsooms:
    def __init__(self, species, breed, humidity, temperature, light):
        self.species = species
        self.breed = breed
        self.humidity = humidity
        self.temperature = temperature
        self.light = light

    def __str__(self):
        pass
    def settings(self):
        pass
    def growth(self):
        pass


species = input("What kind of species are you trying to grow?")
breed = input("What breed of " + species + " are you trying to grow?")
current_grow = []

for i in range(len(current_grow)):
    if current_grow[i] == species:
        print("You are trying to grow " + breed + " " + species + ".")
    else:
        pass


def main():
    pass