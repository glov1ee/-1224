def calculate_force(d, b):
	f = b - d
	if d == 0:
		print("На ноль делить нельзя")
		d = float(input("d: "))
		f = b - d
		calculate_force(d, b)
	elif f == 0:
		print("На ноль делить нельзя:")
		b = float(input("b: "))
		f = b - d
		calculate_force(d, b)
	D = 1/d + 1/f
	return D

d = float(input("d: "))
b = float(input("Расстояние от предмета до экрана: "))
print (calculate_force(d, b))