# Calculadora em Python

print("\n******************* Python Calculatrice *******************")

def addition(x, y):
	return x + y

def soustraction(x, y):
	return x - y

def multiplication(x, y):
	return x * y

def division(x, y):
	return x / y

print("\nChoisissez le numéro d'opération souhaitée: \n")
print("1 - Addition")
print("2 - Soustraction")
print("3 - Multiplication")
print("4 - Division")

choix = input("\nEntrez l'option (1/2/3/4): ")


num1 = int(input("\nEntrez le premier numéro: "))
num2 = int(input("\nEntrez le deuxième numéro: "))

if choix == '1':
	print("\n")
	print(num1, "+", num2, "=", addition(num1, num2))
	print("\n")

elif choix == '2':
	print("\n")
	print(num1, "-", num2, "=", soustraction(num1, num2))
	print("\n")

elif choix == '3':
	print("\n")
	print(num1, "*", num2, "=", multiplication(num1, num2))
	print("\n")

elif choix == '4':
	print("\n")
	print(num1, "/", num2, "=", division(num1, num2))
	print("\n")

else:
	print("\nOption invalide!")

	
	
