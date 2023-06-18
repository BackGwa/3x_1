from matplotlib import pyplot as plt


def main():
    n = int(input("Please enter the initial value >> "))
    n_list = []

    while(n != 1):
        if(n % 2 == 0):
            n = int(n / 2)
        else:
            n = n * 3 + 1
        n_list += [n]
        
    plt.plot(n_list, 'r--', n_list, 'bs')
    plt.show()


if __name__ == "__main__":
    main()