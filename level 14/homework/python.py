#integers = [1, 2, 3, 4, 5]
#last_element = integers.pop()
#print(last_element)

#strings = ["apple", "banana", "cherry"]
#first_element = strings.pop(0)
#print(first_element)


#characters = ['a', 'b', 'c', 'd', 'e']
#index_2_element = characters.pop(2)
#print(index_2_element)


#tuples = [(1, 2), (3, 4), (5, 6)]
#last_tuple = tuples.pop()
#print(last_tuple)


#empty_list = []
#try:
#    element = empty_list.pop()
#except IndexError:
#    print("Can't pop from an empty list!")




#integers = [1, 5, 2, 5, 3, 5, 4, 5, 5]
#count_5 = integers.count(5)
#print("Number of times 5 appears:", count_5)


#strings = ["apple", "banana", "cherry", "avocado"]
#count_a = sum(s.count('a') for s in strings)
#print("Number of times 'a' appears:", count_a)


#booleans = [True, False, True, True, False, True]
#count_true = booleans.count(True)
#print("Number of True values:", count_true)


#nested_list = [[1, 2], [3, 4], [5, 6], [3, 4], [7, 8], [3, 4]]
#sublist_count = nested_list.count([3, 4])
#print("Number of times [3, 4] appears:", sublist_count)



integers = [1, 5, 2, 9, 3, 5, 4, 7]
max_integer = max(integers)
print("Maximum number in the list of integers:", max_integer)


strings = ["apple", "banana", "cherry", "avocado"]
max_length = max(len(s) for s in strings)
print("Maximum string length in the list of strings:", max_length)


ages = [23, 45, 67, 34, 89, 12, 55]
oldest_age = max(ages)
print("Oldest person's age in the list of ages:", oldest_age)


from datetime import datetime

dates = [
    datetime(2023, 5, 17),
    datetime(2021, 6, 24),
    datetime(2024, 1, 5),
    datetime(2022, 11, 30)
]
most_recent_date = max(dates)
print("Most recent date in the list of dates:", most_recent_date)
