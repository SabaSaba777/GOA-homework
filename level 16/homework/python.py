# def find_smallest_element(lst):
#     if not lst:
#         return None  

#     smallest = lst[0]  

#     for element in lst:
#         if element < smallest:
#             smallest = element

#     return smallest


# my_list = [5, 3, 9, 1, 6]
# print(find_smallest_element(my_list))


# def find_largest_element(lst):
#     if not lst:
#         return None  

#     largest = lst[0]

#     for element in lst:
#         if element > largest:
#             largest = element

#     return largest


# my_list = [5, 3, 9, 1, 6]
# print(find_largest_element(my_list))  


# def find_indices(lst, indices):
#     return [index for index in indices if index < len(lst)]


# my_list = ['a', 'b', 'c', 'd', 'e', 'f']
# indices_to_find = [1, 3, 5]


# result_indices = find_indices(my_list, indices_to_find)


# print(result_indices)

# def interleave_lists(int_list, str_list):
#     combined = []
#     max_len = max(len(int_list), len(str_list))
    
#     for i in range(max_len):
#         if i < len(int_list):
#             combined.append(int_list[i])
#         if i < len(str_list):
#             combined.append(str_list[i])
    
#     return combined


# int_list = [1, 2, 3]
# str_list = ['a', 'b', 'c', 'd']


# result = interleave_lists(int_list, str_list)


# print(result)


# def separate_elements(lst):
#     int_list = []
#     str_list = []
    
#     for item in lst:
#         if isinstance(item, int):
#             int_list.append(item)
#         elif isinstance(item, str):
#             str_list.append(item)
    
#     return int_list, str_list


# mixed_list = [1, 'apple', 2, 'banana', 3, 'cherry']


# integers, strings = separate_elements(mixed_list)


# print("Integers:", integers)
# print("Strings:", strings)


# def sum_odd_and_even(lists):
#     odd_sum = 0
#     even_sum = 0
    
#     for lst in lists:
#         for item in lst:
#             if isinstance(item, int): 
#                 if item % 2 == 0:
#                     even_sum += item
#                 else:
#                     odd_sum += item
    
#     return odd_sum, even_sum


# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# list3 = [9, 10, 11, 12]
# list4 = [13, 14, 15, 16]


# odd_sum, even_sum = sum_odd_and_even([list1, list2, list3, list4])


# print("Odd sum:", odd_sum)   
# print("Even sum:", even_sum) 
