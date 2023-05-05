def binary_search(numbers,values):
    min_index = 0
    max_index = len(numbers)-1
    while min_index <= max_index:
        mid_index = (min_index + max_index)//2
        if numbers[mid_index] < values:
            min_index = mid_index + 1
        elif numbers[mid_index] > values:
            max_index = mid_index -1
        else:
            return mid_index
    return -1
numbers = [10, 15, 20, 27, 41, 69]
print(binary_search(numbers, 69))
numbers = [13, 18, 54, 61, 78, 93]
print(binary_search(numbers, 10))
