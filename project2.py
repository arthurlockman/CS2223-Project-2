"""
Name: Arthur Lockman
Assignment: Project 1
The purpose of this project was to test the efficiency of two different algorithms
which determine if two input strings are anagrams of each other. One algorithm
is a brute force algorithm, and the other is a better algorithm designed and
developed by Arthur.
"""
# TODO: doc header

import time
import os


class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


dynamic_table = []


def main():
    """
    This is the main method for Project 2.
    """
    main_menu()


def main_menu():
    """
    Display the main menu to the user.
    :return: nothing
    """
    os.system('clear')
    print('Welcome to the baseball probability calculator!')
    print('Please choose an option: ')
    print('1: Compute the probability of the Red Sox winning a series with a recursive algorithm')
    print('2: Compute the probability of the Red Sox winning a series with a dynamic algorithm')
    print('---')
    print('9: Exit the program')
    get_menu_choice(input(' >>  '))


def get_menu_choice(choice):
    """
    Perform an action based on a menu choice.
    :param choice: The chosen menu item
    :return: nothing
    """
    choice = choice.lower()
    if choice == '1':
        run_calc_probability_recursive()
    if choice == '2':
        calc_probability_dynamic(4, 4, 0.4, 0.6)
    elif choice == '9':
        print('Goodbye!')
        exit()
    else:
        print('Oops! That menu option does not exist.')
    print('Press the ANY key to return to the main menu')
    input()
    main_menu()


def run_calc_probability_recursive():
    """
    Interactively calculate a probability result.
    :return:
    """
    print('Please enter the number of games needed to win the series (n)')
    n = int(input(' >>  '))
    print('Please enter the probability that the Red Sox win the game')
    p = float(input(' >>  '))
    print('Enter 1 to print the dynamic programming table P(i, j), or 0 to skip')
    print_table = int(input(' >>  '))
    if print_table == 1:
        print_table = True
        global dynamic_table
        dynamic_table = [x[:] for x in [[1.0] * n] * n]
    else:
        print_table = False
    start_time = time.time()
    probability = calc_probability_recursive(n, n, p, 1.0 - p, print_table)
    end_time = time.time()
    run_time = end_time - start_time
    print("Probability: " + str(probability) + ", took " + str(run_time) + " seconds")
    if print_table:
        table_to_csv(dynamic_table)


def calc_probability_recursive(i, j, p, q, print_table=False):
    """
    Calculate the probability of the red sox winning a series that requires
    a certain number of wins, with a certain probability of winning any
    given game.
    :param print_table: whether or not to print the recursive function table
    :param i: number of wins needed by Red Sox to win series
    :param j: number of wins needed by Yankees to win series
    :param p: probability Sox win given game
    :param q: probability Yankees win given game
    :return: the probability of the Sox winning the series
    """
    global dynamic_table
    if i == 0:
        if print_table:
            dynamic_table[i - 1][j - 1] = 1
        return 1
    if j == 0:
        if print_table:
            dynamic_table[i - 1][j - 1] = 0
        return 0
    return_value = p * calc_probability_recursive(i - 1, j, p, q,
                                                  print_table) + q * calc_probability_recursive(i, j - 1, p, q,
                                                                                                print_table)
    if print_table:
        dynamic_table[i - 1][j - 1] = round(return_value, 2)
    return return_value


def table_to_csv(table):
    """

    :param table:
    :return:
    """
    header = ['j\\i']
    counter = 1
    for _ in table:
        header.append(counter)
        counter += 1
    print(','.join([str(item) for item in header]))
    counter = 1
    for i in table:
        i = [counter] + i
        print(','.join([str(item) for item in i]))
        counter += 1


def calc_probability_dynamic(i, j, p, q):
    """

    :param i:
    :param j:
    :param p:
    :param q:
    :return:
    """
    root = Tree(None, None, None)
    print(root, i, j, p, q)


if __name__ == "__main__":
    main()
