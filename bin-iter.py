# Code implementation for binary search with iteration
def binary_search(list_num , to_search):
    first_index = 0
    size = len(list_num)
    last_index = size -1
    mid_index = (first_index + last_index) // 2
    # print(mid_index)
    mid_element = list_num[mid_index]
    # print(mid_element)

    is_found = True
    while is_found:
        if first_index == last_index:
            if mid_element == to_search:
                pass
            else:
                return f"{to_search} does not appear in the list"

        elif mid_element == to_search:
            return f"{mid_element} Occurs in position {mid_index}"

        elif mid_element > to_search:
            new_position = mid_index - 1
            last_index = new_position
            mid_index = (first_index + last_index) // 2
            mid_element = list_num[mid_index]
            if mid_element == to_search:
                return f"{mid_element} occurs in position {mid_index}"

        elif mid_element < to_search:
            new_position = mid_index + 1
            first_index = new_position
            last_index = size - 1
            mid_index = (first_index + last_index) // 2
            mid_element = list_num[mid_index]
            if mid_element == to_search:
                return f"{mid_element} occurs in position {mid_index}"
    return None

list_container = [16 , 18 , 20 , 50 , 60 , 81 , 84 , 89]
print(binary_search(list_container , 81))
print(binary_search(list_container , 10))


