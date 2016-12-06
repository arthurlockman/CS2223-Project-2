"""
Name: Arthur Lockman
Assignment: Project 1
The purpose of this project was to test the efficiency of two different algorithms
which determine if two input strings are anagrams of each other. One algorithm
is a brute force algorithm, and the other is a better algorithm designed and
developed by Arthur.
"""

import random
import time
from itertools import permutations
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
    print('Welcome to the anagram algorithm tester!')
    print('Please choose an option: ')
    print('1: Run both algorithms with input strings')
    print('2: Generate sample data, and save it to a file')
    print('3: Run both algorithms with sample data file, and output the time results')
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
        run_with_input_strings()
    elif choice == '2':
        generate_and_save_data()
    elif choice == '3':
        run_test_from_file()
    elif choice == '9':
        print('Goodbye!')
        exit()
    else:
        print('Oops! That menu option does not exist.')
    print('Press the ANY key to return to the main menu')
    input()
    main_menu()


def run_with_input_strings():
    """
    Run both algorithms with user-input strings.
    :return: nothing
    """
    print('Input one string, and then another. This function will '
          'determine if the second string is an anagram of the first.')
    print('Input the first string')
    string1 = input(' >>  ')
    print('Input the second string')
    string2 = input(' >>  ')
    pretty_print_output(string1, string2, is_anagram_better_method(string1, string2), 2)
    pretty_print_output(string1, string2, is_anagram_brute_force(string1, string2), 1)


def generate_and_save_data():
    """
    Generate and save a testing data file based on user input.
    :return: nothing
    """
    print('This selection will generate and save testing data to a file.')
    print('Enter the filename you wish to save testing data to')
    filename = input(' >>  ')
    print('Enter the maximum length of string to generate in the testing data')
    length = int(input(' >>  '))
    print('Enter the number of entries to generate with each length')
    entries = int(input(' >>  '))
    print('Enter 1 if you would like to generate tests that are anagrams, '
          '2 if you would like tests that are not anagrams, or 3 if you would like both')
    test_type = int(input(' >>  '))
    data = ''
    if test_type == 1:
        data += generate_true_test_data(length, entries)
    elif test_type == 2:
        data += generate_false_test_data(length, entries)
    elif test_type == 3:
        data += generate_true_test_data(length, entries)
        data += generate_false_test_data(length, entries)
    with open(filename, 'w') as f:
        f.write(data)
    print('Success! File', filename, 'written with testing data.')


def run_test_from_file():
    """
    Run a test suite defined in a text file generated by the second
    program menu item.
    :return: nothing
    """
    print('This selection will read a testing data file, and run both algorithms on it.')
    print('Enter the filename of the testing file')
    filename = input(' >>  ')
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    print('File loaded.')
    print('Enter the name of the test results file (CSV)')
    out_filename = input(' >>  ')
    with open(out_filename, 'w') as f:
        print('Enter 1 to run the brute force algorithm, 2 to run the better algorithm, and 3 to run both')
        choice = input(' >>  ')
        f.write('String Length,String 1,String 2,Brute Force Result,Brute Force Time,Better Result,'\
                'Better Time,Brute Force Computations,Better Computations\n')
        for line in lines:
            output_line = ''
            line_split = line.replace('\n', '').split(',')
            if choice == '1' or choice == '3':
                brute_res = is_anagram_brute_force(line_split[0], line_split[1])
                pretty_print_output(line_split[0], line_split[1], brute_res, 1)
            else:
                brute_res = (False, 0, 0)
            if choice == '2' or choice == '3':
                better_res = is_anagram_better_method(line_split[0], line_split[1])
                pretty_print_output(line_split[0], line_split[1], better_res, 2)
            else:
                better_res = (False, 0, 0)
            output_line += str(len(line_split[0])) + ',' + line_split[0] + ',' + line_split[1] + ',' + str(
                brute_res[0]) + ',' + str(brute_res[1]) + ',' + str(better_res[0]) + ',' + str(better_res[1]) + \
                ',' + str(brute_res[2]) + ',' + str(better_res[2]) + '\n'
            f.write(output_line)


def pretty_print_output(string1, string2, alg_output, alg_type):
    """
    Prints the output from either of the anagram algorithms.
    :param string1: The first string
    :param string2: The second string
    :param alg_output: output from the algorithm
    :param alg_type: Which type, 1 is brute force, 2 is better
    :return: nothing
    """
    out_string = ''
    if alg_type == 1:
        out_string += 'The brute force algorithm determined that '
    if alg_type == 2:
        out_string += 'The better algorithm determined that '
    out_string += 'the string ' + string2 + ' '
    if alg_output[0]:
        out_string += 'is '
    else:
        out_string += 'is not '
    out_string += 'an anagram of ' + string1 + ' in ' + str(alg_output[1]) + ' seconds '
    out_string += ' (' + str(alg_output[2]) + ' computation loops).'
    print(out_string)


def is_anagram_brute_force(string1, string2):
    """
    Detect whether or not string2 is an anagram of string1 using
    a brute force algorithm. This algorithm is slightly optimized
    in order to save memory. Rather than generating every single permutation
    at the start, it uses the permutations function in python as an iterator
    and one by one iterates through the permutations. This does not keep each
    iteration in memory, it only keeps one at a time, allowing for this method
    to be tested with much larger strings.
    :param string1: The first string to test.
    :param string2: The second string to test.
    :return: A tuple, the first value is a boolean of whether or not the
    second string is an anagram of the first. The second value is a float
    of the runtime of the operation. The third value is the number of loops
    that were completed to compute the result.
    """
    is_anagram = False
    num_loops = 0
    start_time = time.time()
    perm_iterator = permutations(string1)
    for permutation in perm_iterator:
        num_loops += 1
        if ''.join(permutation) == string2:
            is_anagram = True
            break
    end_time = time.time()
    return is_anagram, (end_time - start_time), num_loops


def is_anagram_better_method(string1, string2):
    """
    Detect whether or not string2 is an anagram of string1 using
    my devised method. This method involves counting the occurrences
    of each letter in each of the two input strings, and storing them
    in a dictionary. Then, the two dictionaries are compared, and if
    the counts for each of the letters for both strings is equal
    the string is counted as an anagram. To increase efficiency in
    detecting non-anagrams, if a letter count is found to be wrong
    the algorithm immediately returns false rather than checking all
    of the remaining letters.
    :param string1: The first string to test.
    :param string2: The second string to test.
    :return: A tuple, the first value is a boolean of whether or not the
    second string is an anagram of the first. The second value is a float
    of the runtime of the operation. The third value is the number of 
    loops that were completed to compute the result.
    """
    start_time = time.time()
    string1_letter_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
                            'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
                            'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
                            'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
                            'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
                            'z': 0}
    string2_letter_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
                            'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
                            'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
                            'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
                            'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
                            'z': 0}
    is_anagram = True
    num_loops = 0
    for i in string1:
        string1_letter_count[i] += 1
        num_loops += 1
    for i in string2:
        string2_letter_count[i] += 1
        num_loops += 1
    for i in global_dict:
        num_loops += 1
        if string1_letter_count[i] != string2_letter_count[i]:
            is_anagram = False
            break
    end_time = time.time()
    return is_anagram, (end_time - start_time), num_loops


def generate_true_test_data(length, number):
    """
    Generate testing data for the anagram algorithm. This method
    generates a large number of test anagram strings for the algorithm
    to be tested against. It is different each time it is run, due
    to its use of the built-in pseudo random number generator.
    :param length: Generate strings in length from 1 to this length.
    :param number: Generate this number of strings at each length.
    :return: A string containing all of the test string data.
    """
    return_string = []
    for i in range(1, length + 1):
        for j in range(1, number + 1):
            initial_string = ""
            for k in range(1, i + 1):
                initial_string += random.choice(global_dict)
            string_list = list(initial_string)
            random.shuffle(string_list)
            jumbled_string = ''.join(string_list)
            anagram_string = initial_string + ',' + jumbled_string
            return_string.append(anagram_string)
    return '\n'.join(return_string) + '\n'


def generate_false_test_data(length, number):
    """
    Generate testing data for the anagram algorithm. This method
    generates a large number of test incorrect anagram strings for the algorithm
    to be tested against. It is different each time it is run, due
    to its use of the built-in pseudo random number generator.
    :param length: Generate strings in length from 1 to this length.
    :param number: Generate this number of strings at each length.
    :return: A string containing all of the test string data.
    """
    return_string = []
    for i in range(1, length + 1):
        for j in range(1, number + 1):
            initial_string = ''
            for k in range(1, i + 1):
                initial_string += random.choice(global_dict)
            jumbled_string = ''
            for k in range(1, i + 1):
                jumbled_string += random.choice(global_dict)
            anagram_string = initial_string + ',' + jumbled_string
            return_string.append(anagram_string)
    return '\n'.join(return_string) + '\n'


def effAnaBtr(s1, s2):
    pretty_print_output(s1, s1, is_anagram_better_method(s1, s1), 2)


def effAnaBF(s1, s2):
    pretty_print_output(s1, s1, is_anagram_brute_force(s1, s1), 1)


if __name__ == "__main__":
    main()