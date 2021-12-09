
def main():
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"
    word_list = state.split()
    print(word_list)
    for x in range(len(word_list)):
        if len(word_list[x]) < 5:
            print(word_list[x])



if __name__ == "__main__":
    main()
