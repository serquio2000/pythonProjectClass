def main():
    '''
    y= int(input("introduce un valor de y; es hasta donde llega el bucle:"))
    z= int(input("introduce un valor de z; es el valor de inicio del bucle:"))
    q = int(input("introduce un valor de q; es el valor por el que se va a recorrer el bucle:"))
    for x in range(z,y+1,q):
        print(x)'''


''' month = int(input("introduce un numero; refiriendose al mes:"))
  while month < 1 or month > 12:
      month = int(input("introduce un numero; refiriendose al mes:"))

  if month % 2 != 0 and month < 8:
      print("el mes", month, "tiene 31 dias")
  elif month == 2:
      print("el mes", month, "tiene 28 dias")
  elif month == 8:
      print("el mes", month, "tiene 31 dias")
  elif month > 8 and month % 2 == 0:
      print("el mes", month, "tiene 31 dias")
  else:
      print("el mes", month, "tiene 30 dias")
'''
num1 = int(input("introduce un numero:"))
num2 = int(input("introduce un numero:"))
aux = 0
aux = num1
num1 = num2
num2 = aux
print("el numero 1 es:", num1, "el numero 2 es:", num2)
if __name__ == '__main__':
    main()
