# Q1 ---------------------------------------------------------------

lst = [30, 75, 9, 97, 50, -4, 70, 59]

largest_number = max(lst)
print("Largest number:", largest_number)

smallest_number = min(lst)
lst.remove(smallest_number)
sorted_list = sorted(lst)
first_four_numbers = sorted_list[:4]
print("First 4 numbers:", first_four_numbers)
print("--"*20)

# Q2 ---------------------------------------------------------------

main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python",1]]
count = sum(sublist.count("python") for sublist in main_lst)
print("python is repeated:", count, " times")
print("--"*20)

# Q3 ---------------------------------------------------------------

my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]

sentence = " ".join(my_lst)
print(sentence)
print("--"*20)

# Q4 ---------------------------------------------------------------

my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
new_lst = my_lst[:]
print(new_lst)
print("--"*20)

# Q5 ---------------------------------------------------------------

my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_lst[2], my_lst[4] = my_lst[4], my_lst[2]
print(my_lst)
print("--"*20)

# Q6 ---------------------------------------------------------------

nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
sum_of_nums = sum(nums)
print("Sum of the List", sum_of_nums)
print("--"*20)

# Q7 ---------------------------------------------------------------

tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple1 += (9,)
print("Tuple 1 result: ", tuple1)
print("--"*20)

# Q8 ---------------------------------------------------------------

tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = ('Java', 'C++', 7.8)
new_tuple = tuple1 + tuple2
print("Join 2 tuples result:", new_tuple)
print("--"*20)
