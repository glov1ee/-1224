"""
	ДЗ
	1. Вывести, какой является линза
	2. Вернуть положительное фокусное расстояние 
	2.1 Функция abs() - почитать и использовать
"""
def calculate_dptr(D):
	s = ''
	if D == 0:
		print("На ноль делить нельзя")
		D = float(input("Выберите D: "))
		calculate_dptr(D)
		pass
	if D < 0:
		s = "Розсіювальна лінза"
	elif D > 0:
		s = "Збираюча лінза"
	F = 1 / D
	return abs(F), s

D = float(input("Выберите D: ")) 
print(calculate_dptr(D)) #  list l = []
#mutable # tuple t = () #unmutable