first_list = [1, 2, 3, 4, 5]
second_list = [4, 5, 6, 7]

print(first_list + list(set(second_list) - set(first_list)))