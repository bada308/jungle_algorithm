import random

# 선택 정렬 구현하기
def selection_sort(list):
    for i in range(0, len(list) - 1):
        min_value_idx = i
        for j in range(i + 1, len(list)):
            print(list[min_value_idx], list[j])
            if(list[min_value_idx] > list[j]):
                min_value_idx = j
        list[i], list[min_value_idx] = list[min_value_idx], list[i]
            
    
    
my_list = []
for _ in range(10):
    my_list.append(random.randrange(15))
    
    
print("정렬 전:")
print(my_list)
print()
print("정렬 후:")
selection_sort(my_list)
print(my_list)