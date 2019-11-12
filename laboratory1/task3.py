import re
print("Лаштабєг Ася Володимирівна\nЛабораторна робота №1 \nВаріант 16\nОбчислення функції в залежності від значення введеної змінної")
def read (q):
	x = input(q)
	while not re.match(r'(?:[0]\.\d+)|(?:[1-9]\d*(?:\.\d+)?)', x):
		x = input(q)
	return float(x)

def main ():
	x=read("Введіть значення х")
	if(x<3.2):
		F=pow(x,4)+9
		print("Оскільки x<3.2, то F(x)=x^4+9")
	else:
		F=54*pow(x,4)/(-5*x*x+7)
		print("Оскільки x>=3.2, то F(x)=x^4/(-5*x^2+7)")
	print("Тому виходить, що F(x)="+str(F))

main()