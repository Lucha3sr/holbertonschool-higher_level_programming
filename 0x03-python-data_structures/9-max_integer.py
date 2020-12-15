#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        big_int = my_list[0]
        for i in my_list:
            if i > big_int:
                big_int = i
        return big_int
    else:
        return None
