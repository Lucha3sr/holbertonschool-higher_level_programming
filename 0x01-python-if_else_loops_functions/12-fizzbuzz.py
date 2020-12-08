#!/usr/bin/python3
def fizzbuzz():
    for nbr in range(1, 101):
        if nbr % 3 == 0 and nbr % 5 == 0:
            print("FizzBuzz", end=" ")
        elif nbr % 5 == 0:
            if nbr == 100:
                print("Buzz", end=" ")
            else:
                print("Buzz", end=" ")
        elif nbr % 3 == 0:
            print("Fizz", end=" ")
        else:
            print(nbr, end=" ")
