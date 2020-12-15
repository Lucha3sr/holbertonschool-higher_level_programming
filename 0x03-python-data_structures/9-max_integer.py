#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        big_int = my_list[0]
        for i in my_list:
            if big_int < i:
                big_int = i
                return big_int
                return None
