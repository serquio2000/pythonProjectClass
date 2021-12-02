def main():
    aux=0
    n1,n2 = int(input("introduce un numero")),int(input("introduce un numero"))
    while n1<0 and n1>n2 :
        n1, n2 = int(input("introduce un numero")), int(input("introduce un numero"))
    aux=n1
    for n1 in range(n1,n2+1,1):
       if  n1% aux == 0:
           print(n1)



if __name__ == '__main__':
    main()