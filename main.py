string_list = ["food is good","water","air"]

print(string_list)

for i in string_list:
  print(i)

my_list = [1, 2, 3, 4, 5]
print(len(my_list))

new_list = my_list.copy()

print(string_list[2])

my_list.remove(2)
string_list.remove("water")
print(string_list)

second_list = [6,7,8]

third_list = my_list + second_list
another_list = string_list + third_list

print(another_list)
