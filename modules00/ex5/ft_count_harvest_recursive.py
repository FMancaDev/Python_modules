#! /usr/bin/env python3

def ft_harvest_recursive():
    until_harvest = int(input("Days until harvest: "))

    def loop_days(current_day):
        if (current_day > until_harvest):
            print("Harvest time!")
            return
        print(f"Day {current_day}")
        loop_days(current_day + 1)
    loop_days(1)
