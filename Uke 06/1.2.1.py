
string = "bccacbcccccccccccaccca"
dictionary = {chr(i):i for i in range(0,127)}

last = 127
a = ""
result = []

for c in string:
	ac = a + c
	if ac in dictionary:
		a = ac
	else:
		result.append(dictionary[a])
		dictionary[ac] = last
		last += 1
		a = c

if a != '':
	result.append(dictionary[a])

print(result)