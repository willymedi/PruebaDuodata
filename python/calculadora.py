from utils import *
showOptions()

option = input("Ingrese operacion: ").strip()
if option!= "1" and option!= "2":
  print("Opcion incorrecta")
  exit()

numbersInput = input("Ingrese operadores separados por espacios: ").strip()
numbers = numbersInput.split(" ")
if len(numbers)== 0 or numbers[0]== "":
  print("No ha ingresado operadores")
  exit()

numbers = transformToListIntegers(numbers)
suma = sum(numbers)
if option=="1":
  print(getSum(numbers))
else:
  print(getMean(numbers))