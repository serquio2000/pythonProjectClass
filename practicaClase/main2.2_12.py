def main():
    codeList = list()
    telefonList = list()
    ageList = list()
    contactList = list()
    validateList = list()
    x,y=0,0
    contact= False
    values= int(input("introduce cuantos valores quieres registrar: "))
    while values<0:
        values = int(input("introduce cuantos valores quieres registrar: "))

    while x < values:
        name,surname,surname2 = input("introduce un nombre:"),input("introduce el primer apellido:"),input("introduce el segundo apellido:")
        tn,age = input("introduce un numero de telefono:"),int(input("introduce tu edad:"))
        validate= input("introduce si es correcto o no:")
        if validate[:1] == "y":
            validate = True
        else :
            validate = False
        code= 0
        contact = int(input("introduce si es registro nuevo;1=nuevo, 0=registrado: "))
        while contact >1 and contact <0:
            contact = int(input("introduce si es registro nuevo;1=nuevo, 0=registrado: "))
            if contact == 1:
                contact = True
            else:
                contact = False
        while len(tn)<9 or len(tn)>9:
            tn= input("introduce un numero de telefono:")
        while age<0 :
            age = int(input("introduce tu edad:"))
        code = surname[:2] + surname2[:2] + name[:2]
        codeList.append(code)
        telefonList.append(tn)
        ageList.append(age)
        contactList.append(contact)
        validateList.append(validate)
        x += 1
    print("\tcodi " + "\ttelefon " + "\tedat " + "\tcontacte "+ "\tValidar")
    while y< len(codeList):
        print("\t",codeList[y], telefonList[y],"\t", ageList[y],"\t", contactList[y],"\t\t\t",validateList[y])
        y += 1

if __name__ == "__main__":
    main()