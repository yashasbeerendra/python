letters = input().split(',')
my_list = []
for i in letters:
    if letters.count(i) > 1:
        if i not in my_list:
            my_list.append(i)

print(my_list[1])
