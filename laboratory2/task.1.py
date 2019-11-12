import re
print("Лаштабєг Ася Володимирівна\nЛабораторна робота №2 \nВаріант 16 \nЗнаходження суми чисел у степені")
def read1 (q):
	x = input(q)
	while not re.match(r'[1-9]\d*', x):
		x = input(q)
	return float(x)
def read2 (j):
	y = input(j)
	while not re.match(r'(?:[0]\.\d+)|(?:[1-9]\d*(?:\.\d+)?)', y):
		y = input(j)
	return float(y)
def main ():
	n = read1("Введіть кількість доданків")
	x = read2("Введіть значчення доданку")
	sum = 0
	i = 1
	for i in (1, n+1):
		sum += x**i
		i += 1
		print("Шукана сума: " + str(sum))

main ()