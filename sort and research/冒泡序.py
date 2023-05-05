def bubble_sort(data,pass_num):
    for i in range(pass_num):
        for j in range(0,len(data)-i-1):
            if data[j] > data[j + 1]:
                data[j], data[j+1] = data[j+1],data[j]
    return data
for i in range(1,6):
    print(bubble_sort([54, 26, 93, 17, 77, 20], i))

def bubble_row(data,index):
    for i in range(0,index):
        if data[i] > data[i + 1]:
            data[i],data[i+1] = data[i+1],data[i]
    return data
letters = ['e', 'd', 'c', 'b', 'a']
bubble_row(letters, 3)
print(letters)
letters = ['e', 'd', 'c', 'b', 'a']
bubble_row(letters, 2)
print(letters)


def my_bubble_sort(data):
    for pass_num in range(len(data)-1,0,-1):
        for i in range(0,len(data[0:pass_num])):
            if data[i] > data[i + 1]:
                data[i],data[i+1] = data[i+1],data[i]
    return data
letters = ['e', 'd', 'c', 'b', 'a']
my_bubble_sort(letters)
print(letters)
            
