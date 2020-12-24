def calculate_force(d,f):
	if d == 0 or f == 0:
		print("На ноль делить нельзя")
		d = float(input("d:"))
		f = float(input("f:"))
		pass
	D = 1/d + 1/f
	return D

d = input("d:")
while d == "":
	print("d - не может быть пустой строкой")
	d = float(input("d:"))
d = float(d)
f = float(input("f:"))
while f == "":
	print("f - не может быть пустой строкой")
	f = float(input("f:"))
f = float(f)
print(calculate_force(d,f))


