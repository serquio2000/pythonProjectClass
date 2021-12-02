def main():
    llista = ['apple',1,2.5]
    print(llista)
    print(llista[2])
    for x in llista:
        print(x)
    print("--------")
    llista.append(True)
    print(llista)
    llista[3] = False
    print(llista)
    llista.insert(2,20)
    print(llista)
    llista.remove(False)
    print(len(llista))
    del llista[0]
    print(len(llista))
    llista.clear()
    print(llista)
if __name__ == '__main__':
    main()

