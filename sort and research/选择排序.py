def selection_sort(numbers, pass_number):
    for i in range(len(numbers)-1,len(numbers) - 1 - pass_number,-1):
        max_num = max(numbers[0:i])
        index = numbers.index(max_num)
        if max_num != numbers[i]:
            numbers[index],numbers[i] = numbers[i],max_num
    return numbers            
for i in range(1,6):
    print(selection_sort([93, 54, 78, 18, 61, 13], i))
print()
def my_selection_sort(data,step):
    for i in range(len(data) - 1, len(data) - step - 1, -1):
        t_max = data.index(max(data[:i + 1]))
        if t_max != i:
            data[t_max], data[i] = data[i], data[t_max]
    return data
for i in range(1,6):
    print(my_selection_sort([93, 54, 78, 18, 61, 13], i))
print()
def get_position_of_highest(data,index):
    new = data[0:index + 1]
    max_num = max(new)
    index = new.index(max_num)
    return index
letters = ['g', 'y', 'd', 'h', 'w', 't', 'e', 'q', 'c', 'x', 'b', 'f', 'u', 'r', 'k', 'm']
print(get_position_of_highest(letters, 2))
print()
def selection_row(data,index):
    for i in range(index,0,-1):
        max_num = max(data[0:i+1])
        index = data.index(max_num)
        if data[i] != max_num:
            data[i], data[index] = max_num, data[i]
    return data
letters = ['b', 'f', 'u', 'r', 'k']
selection_row(letters, 3)
print(letters)
letters = ['a', 'd', 'h', 'w', 't', 'p']
selection_row(letters, 3)
print(letters)
def my_selection_sort(data):
    for i in range(len(data)-1,0,-1):
        max_num = max(data[0:i+1])
        index = data.index(max_num)
        if max_num != data[i]:
            data[i],data[index] = max_num, data[i]
    return data
letters = ['y', 'd', 'h', 'w']
my_selection_sort(letters)
print(letters)
        
    
    
        
                
