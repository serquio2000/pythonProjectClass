def main():
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"
    count,i= 0,0
    for i in range(0,len(state)):
        if state[i] == " ":
            count+=1
    print("espacios en blanco:", count)
if __name__ == "__main__":
    main()
