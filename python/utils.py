def showOptions():
  print('''
Operaciones disponibles
1. Suma
2. Promedio
''')

def transformToListIntegers(numbers):
  try:
    return [int(number) for number in numbers]
  except ValueError:
    print("No es un numero valido")
    exit()

def getSum(numbers):
  return sum(numbers)

def getMean(numbers):
  return sum(numbers) / len(numbers)