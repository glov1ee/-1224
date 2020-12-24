def calculate_math(f):
	x = a/b + c
	if b == 0:
		return "Нельзя делить на ноль"

f = input("input f: ")
f = f.split(" ")
for number in range(3):
	print (float(f[number]))
	print (calculate_math(float(f[number])))