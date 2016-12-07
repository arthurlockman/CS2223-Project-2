"""
Name: Arthur Lockman
Assignment: Project 1
The purpose of this project was to test the efficiency of two different algorithms
which determine if two input strings are anagrams of each other. One algorithm
is a brute force algorithm, and the other is a better algorithm designed and
developed by Arthur.
"""

import time
import os

global_dict = "abcdefghijklmnopqrstuvwxyz"


def main():
    """
    This is the main method for Project 1.
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
        calc_probability_dynamic(4, 0.4)
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
    start_time = time.time()
    probability = calc_probability_recursive(n, n, p, 1.0 - p)
    end_time = time.time()
    run_time = end_time - start_time
    print("Probability: " + str(probability) + ", took " + str(run_time) + " seconds")


def calc_probability_recursive(i, j, p, q):
    """

    :param i:
    :param j:
    :param p:
    :param q:
    :return:
    """
    if i == 0:
        return 1
    if j == 0:
        return 0
    return p * calc_probability_recursive(i-1, j, p, q) + q * calc_probability_recursive(i, j-1, p, q)


def calc_probability_dynamic(n, p):
    """

    :param n:
    :param p:
    :return:
    """
    i = n
    j = n
    q = 1.0 - p
    p_stack = []
    q_stack = []


if __name__ == "__main__":
    main()
