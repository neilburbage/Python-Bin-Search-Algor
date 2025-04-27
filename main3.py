# Code implementation for binary search with recursion
def binary_search(list_num, first_index, last_index, to_search):
    if first_index > last_index:
        return f"{to_search} does not appear in the list"

    mid_index = (first_index + last_index) // 2
    mid_element = list_num[mid_index]

    if mid_element == to_search:
        return f"{mid_element} occurs in position {mid_index}"
    elif mid_element > to_search:
        return binary_search(list_num, first_index, mid_index - 1, to_search)
    else:
        return binary_search(list_num, mid_index + 1, last_index, to_search)

list_container = [1, 9, 11, 21, 34, 54, 67, 90]

print(binary_search(list_container, 0, len(list_container) - 1, 34))
print(binary_search(list_container, 0, len(list_container) - 1, 7))