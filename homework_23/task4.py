lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]

max_length_list = max(lists, key=lambda x: len(x))
min_length_list = min(lists, key=lambda x: len(x))

print("All lists:", lists)
print("Max length list:", max_length_list)
print("Min length list:", min_length_list)
