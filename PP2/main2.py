def main():

    suma=0
    n1,n2 = int(input("introduce un numero")),int(input("introduce un numero"))
    while n1>n2 :
        n1, n2 = int(input("introduce un numero")), int(input("introduce un numero"))
    for n1 in range(n1,n2+1,1):
        suma = suma + n1
        print(suma)



if __name__ == '__main__':
    main()