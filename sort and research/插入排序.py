def insertion_sort(numbers, pass_number):
    for i in range(1,pass_number+1):
        j = i
        while numbers[j] < numbers[j - 1] and j >= 1:
            numbers[j],numbers[j-1] = numbers[j-1],numbers[j]
            j -= 1
    return numbers
for i in range(1,6):
    print(insertion_sort([54, 26, 93, 17, 77, 20], i))
def shifting(data,index):
    while data[index] < data[index-1] and index -1 >= 0:
        data[index], data[index-1] = data[index-1],data[index]
        index -= 1
    data[index] = data[index+1]
    return data
letters = ['b', 'c', 'k', 'a', 'z', 'n', 'j', 's']
shifting(letters, 3)
print(letters)
letters = ['a', 'c', 'f', 'b', 'g']
shifting(letters, 3)
print(letters)
print()
def insertion_row(data,index):
    while data[index] < data[index - 1] and index-1 >= 0:
        data[index-1],data[index] = data[index], data[index-1]
        index -= 1
    return data
letters = ['h', 't', 'w', 'e', 'q', 'c', 'x']
insertion_row(letters, 3)
print(letters)
letters = ['g', 'a', 'd', 'h', 'y']
insertion_row(letters, 1)
print(letters)
def my_insertion_sort(data):
    for index in range(1,len(data)):
        i = index
        while data[i] < data[i-1] and i-1 >= 0:
            data[i-1],data[i] = data[i],data[i-1]
            i -= 1
    return data
letters = ['x', 'b', 'f', 'u', 'r', 'k']
my_insertion_sort(letters)
print(letters)
            
