#! /usr/bin/env python3

def ft_water_reminder():
    water = int(input("Days since last watering: "))
    if water > 2:
        print("Water the Plants!")
    else:
        print("Plants are fine")
