import re
print("Лаштабєг Ася Володимирівна\nЛабораторна робота №2 \nВаріант 16 \nЗнаходження найменшого додатнього числа")
def read (q):
	x = input(q)
	while not re.match(r'[1-9]\d*', x):
		x = input(q)
	return float(x)

def main ():
	N = read("Введіть натуральне число")
	if N > 0:
		K = 1
		while K**2 <= N:
			K += 1
	print("Найменше додатнє число: " +str(K))
	return 0

main ()