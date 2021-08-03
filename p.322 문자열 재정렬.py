s = input()
alphabet_list = []
total = 0

for i in s:
    if i.isalpha():
        alphabet_list.append(i)
    else: total += int(i)

alphabet_list.sort()

string = ""
for i in alphabet_list:
    string += i
print(string + str(total) if total != 0 else string)