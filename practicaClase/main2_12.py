def main():
    lista = list()
    x,y=0,0
    values= int(input("introduce cuantos valores quieres registrar: "))
    while values<0:
        values = int(input("introduce cuantos valores quieres registrar: "))

    while x < values:
        name,surname,surname2 = input("introduce un nombre:"),input("introduce el primer apellido:"),input("introduce el segundo apellido:")
        tn,age = input("introduce un numero de telefono:"),int(input("introduce tu edad:"))
        code= 0
        while len(tn)<9 or len(tn)>9:
            tn= input("introduce un numero de telefono:")
        while age<0 :
            age = int(input("introduce tu edad:"))
        contact= False
        code = surname[:2] + surname2[:2] + name[:2]
        lista.append(code)
        lista.append(tn)
        lista.append(age)
        lista.append(contact)
        x += 1
    print("\tcodi " + "\ttelefon " + "\tedat " + "\tcontacte ")
    while y< len(lista):
        print(lista[y])
        y += 1

if __name__ == "__main__":
    main()