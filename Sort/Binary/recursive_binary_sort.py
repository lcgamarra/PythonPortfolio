import math


def recursive_binary_search(array_input, lower_index, higher_index):
    # Stop Condition
    if lower_index == higher_index:
        return [array_input[lower_index]]

    middle_index = math.floor((higher_index - lower_index) / 2 + lower_index)
    left_array_higher_index = middle_index
    right_array_lower_index = middle_index + 1

    left_array = recursive_binary_search(array_input, lower_index, left_array_higher_index)
    right_array = recursive_binary_search(array_input, right_array_lower_index, higher_index)

    # Merging arrays
    result_array = [0] * (len(left_array) + len(right_array))
    left_i = 0
    left_max = len(left_array)
    right_i = 0
    right_max = len(right_array)
    result_i = 0
    while left_i < left_max or right_i < right_max:
        if left_i == left_max:
            while right_i < right_max:
                result_array[result_i] = right_array[right_i]
                right_i += 1
                result_i += 1
            return result_array
        elif right_i == right_max:
            while left_i < left_max:
                result_array[result_i] = left_array[left_i]
                left_i += 1
                result_i += 1
            return result_array

        if left_array[left_i] <= right_array[right_i]:
            result_array[result_i] = left_array[left_i]
            left_i += 1
        else:
            result_array[result_i] = right_array[right_i]
            right_i += 1
        result_i += 1

    return result_array


array = [0, 2, 2, 2, 2, 5, 8, 6, 4, 3, 3, 3, 7, 10, 1, 1, 1]
result = recursive_binary_search(array, 0, len(array) - 1)
print(result)
