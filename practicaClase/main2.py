def main():
    num = int(input("introduce un numero: "))
    resultado, suma = 0, 0
    while num < 0:
        num = int(input("introduce un numero: "))
    while num >= resultado + suma:
        resultado = suma + resultado
        print(suma, "->", resultado)
        suma += 1
if __name__ == '__main__':
    main()
