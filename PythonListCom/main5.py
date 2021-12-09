def main():
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"
    vowels = ('a', 'e', 'i', 'o', 'u')
    x=0
    for x in vowels:
        state = state.replace(x, "")
    print(state)
if __name__ == "__main__":
    main()
