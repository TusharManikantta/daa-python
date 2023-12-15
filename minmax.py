def find_min_max(input_data, start, end):
    if start == end:
        return input_data[start], input_data[end]
    
    if end - start == 1:
        return min(input_data[start], input_data[end]), max(input_data[start], input_data[end])
    
    mid = (start + end) // 2
    min1, max1 = find_min_max(input_data, start, mid)
    min2, max2 = find_min_max(input_data, mid + 1, end)

    return min(min1, min2), max(max1, max2)

string_input = input("Enter the string: ")
min_char, max_char = find_min_max(string_input, 0, len(string_input) - 1)
print(f"For string: Min char: {min_char}, Max char: {max_char}")


num_input = [int(x) for x in input("Enter the numbers separated by space: ").split()]
min_num, max_num = find_min_max(num_input, 0, len(num_input) - 1)
print(f"For numbers: Min value: {min_num}, Max value: {max_num}")




