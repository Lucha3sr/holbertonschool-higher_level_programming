#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    total_elements = len(my_list)
    if idx < 0:
        return (my_list)
    elif idx > total_elements - 1:
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
