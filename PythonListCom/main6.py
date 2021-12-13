
def main():
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"
    count=[i for i in state.split() if len(i) < 5]
    print(count)


if __name__ == "__main__":
    main()
