"""
Name: Arthur Lockman
Assignment: Project 2
The purpose of this project was to use recursion and dynamic programming
to calculate the probability of a baseball team winning a series with n
games needed to win with a given probability.
"""

import time
import os

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
    print('3: Run interactive test suite')
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
    elif choice == '2':
        run_calc_probability_dynamic()
    elif choice == '3':
        run_test_suite()
    elif choice == '9':
        print('Goodbye!')
        exit()
    else:
        print('Oops! That menu option does not exist.')
    print('Press the ANY key to return to the main menu')
    input()
    main_menu()


def run_test_suite():
    """
    Run an interactive test suite on the algorithms.
    :return: none
    """
    print('This test suite will run both algorithms with many different n inputs (p=0.4), and time the results.')
    print('Please input the highest n you wish to test')
    n_max = int(input(' >>  '))
    print('Please input the number of samples to test at each n increment')
    samples = int(input(' >>  '))
    print('Please input the name of the output file you wish to write')
    filename = input(' >>  ')
    output_string = 'n,Recursive Result,Recursive Time,Dynamic Result,Dynamic Time,\n'
    for n in range(1, n_max + 1):
        print('Testing n=' + str(n) + "...")
        for r in range(1, samples + 1):
            print('\tRun ' + str(r) + '... ', end='', flush=True)
            output_line = str(n) + ","
            start_time = time.time()
            probability = calc_probability_recursive(n, n, 0.4, 1.0 - 0.4)
            end_time = time.time()
            run_time = end_time - start_time
            output_line += str(probability) + "," + str(run_time) + ","
            start_time = time.time()
            probability = calc_probability_dynamic(n, n, 0.4, 1.0 - 0.4)
            end_time = time.time()
            run_time = end_time - start_time
            output_line += str(probability) + "," + str(run_time) + ","
            output_string += output_line + "\n"
            print('Done.')
    with open(filename, 'w') as f:
        f.write(output_string)
    print('Done! Output file', filename, 'written.')


def run_calc_probability_recursive():
    """
    Interactively calculate a probability result using the
    recursive algorithm.
    :return: nothing but the printed result
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


def run_calc_probability_dynamic():
    """
    Interactively calculate a probability result using the
    dynamic algorithm.
    :return: nothing but the printed result
    """
    print('Please enter the number of games needed to win the series (n)')
    n = int(input(' >>  '))
    print('Please enter the probability that the Red Sox win the game')
    p = float(input(' >>  '))
    start_time = time.time()
    probability = calc_probability_dynamic(n, n, p, 1.0 - p)
    end_time = time.time()
    run_time = end_time - start_time
    print("Probability: " + str(probability) + ", took " + str(run_time) + " seconds")


def calc_probability_recursive(i, j, p, q, print_table=False):
    """
    Calculate the probability of the red sox winning a series that requires
    a certain number of wins, with a certain probability of winning any
    given game using a recursive programming method.
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
    Calculate the probability of the red sox winning a series that requires
    a certain number of wins, with a certain probability of winning any
    given game using a dynamic programming method.
    :param i: number of wins needed by Red Sox to win series
    :param j: number of wins needed by Yankees to win series
    :param p: probability Sox win given game
    :param q: probability Yankees win given game
    :return: the probability of the Sox winning the series
    """
    prob_table = [[-1 for _ in range(j+1)] for _ in range(i+1)]
    # Construct a table to store the calculated probabilities in and pre-fill
    # the end conditions (0 and 1)
    for idx in range(i-1, -1, -1):
        prob_table[i][idx] = 1.0
        prob_table[idx][i] = 0.0
    # Iterate through the table starting at the ending conditions to calculate the
    # probabilities. Effectively it's generating the dynamic programming table
    # that the recursive function creates as well, but generating it on the fly
    # to arrive at the final value which is the result we're looking for. It stores this
    # in the first row and column of the table, which is what is returned.
    for idx in range(i-1, -1, -1):
        prob_table[idx][idx] = p * prob_table[idx + 1][idx] + q * prob_table[idx][idx + 1]
        for idx1 in range(i-1, -1, -1):
            prob_table[idx1][idx] = p * prob_table[idx1 + 1][idx] + q * prob_table[idx1][idx + 1]
            prob_table[idx][idx1] = p * prob_table[idx + 1][idx1] + q * prob_table[idx][idx1 + 1]
    return prob_table[0][0]

if __name__ == "__main__":
    main()
