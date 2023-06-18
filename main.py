from os import mkdir, path
from matplotlib import pyplot as plt


def main():
    n = int(input("Please enter the initial value >> "))
    n_list = [n]

    while(n != 1):
        if(n % 2 == 0):
            n = int(n / 2)
        else:
            n = n * 3 + 1
        n_list += [n]
        
    savefile(n_list)
    plt.plot(n_list, 'r--', n_list, 'bs')
    plt.show()


def savefile(n_list):
    if(not path.exists('outputs')):
        mkdir('outputs')
    file = open(f'outputs/{n_list[0]}.csv', 'a', encoding='UTF-8')
    
    file.writelines(list(map(convert, n_list)))
    file.close()


def convert(item):
    return str(item) + '\n'


if __name__ == "__main__":
    main()