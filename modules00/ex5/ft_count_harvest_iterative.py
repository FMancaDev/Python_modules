#! /usr/bin/env python3

def ft_count_harvest_iterative():
    until_harvest = int(input("Days until harvest: "))
    for count in range(1, until_harvest + 1):
        print("Day", count)
    print("Harvest time!")
