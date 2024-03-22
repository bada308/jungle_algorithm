import random

def insertion_sort(list):
    for i in range(1, len(list)):
        while i > 0 and list[i] < list[i-1]:
            list[i], list[i-1] = list[i-1], list[i]
            i -= 1
            
# 재귀로 구현하기

def insertion_sort_recursion(list, n = 1):
    if n == len(list):
        return
    i = n
    while i > 0 and list[i] < list[i-1]:
            list[i], list[i-1] = list[i-1], list[i]
            i -= 1
    insertion_sort_recursion(list, n + 1)
            
my_list = []
for _ in range(10):
    my_list.append(random.randrange(15))
    
    
print("정렬 전:")
print(my_list)
print()
print("정렬 후:")
insertion_sort(my_list)
print(my_list)
print()

my_list2 = []
for _ in range(10):
    my_list2.append(random.randrange(15))

print("[재귀] 정렬 전:")
print(my_list2)
print()
print("[재귀] 정렬 후:")
insertion_sort_recursion(my_list2)
print(my_list2)