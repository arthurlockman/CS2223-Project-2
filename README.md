
Algorithms Project 2
===

The purpose of this assignment is to compare the performance of a recursive algorithm with a dynamically-developed iterative algorithm to compute the same result. These algorithms compute the odds of a baseball team (the Red Sox) winning a series of games against another team (the Yankees) with a given probability that the Sox win any given game in the series.

*This document is written assuming this code is being run on the WPI CCC machines. It may vary on other computers with different Python installations, but the procedure should be largely the same.* 

## Project Setup

This project does not require any non-standard libraries to run. It can be run on CCC by typing

```
-bash-4.1$ python3.4 ./project2.py
```

Sometimes this command will fail, and drop into a python prompt instead of running the program (this is due to a configuration error on the CCC servers). To bypass this and run the program, follow these steps:

```
-bash-4.1$ python3.4
Python 3.4.1 (default, Aug 28 2014, 13:51:39)
[GCC 4.7.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import project1
>>> project2.main()
```

By importing and running the project in the python interpreter, the configuration issue can be bypassed and the program can be run.

## Project Usage

Once the project is running, the code will present a menu which will allow the user to perform its main functions.

```
Welcome to the baseball probability calculator!
Please choose an option:
1: Compute the probability of the Red Sox winning a series with a recursive algorithm
2: Compute the probability of the Red Sox winning a series with a dynamic algorithm
3: Run interactive test suite
---
9: Exit the program
 >>
```

The first option will allow the user to compute the probability of the Sox winning a series. It will ask for an *n* input and a probability of them winning a single game, and output the resulting probability and the time that it took for the algorithm to arrive at that result.

```
Welcome to the baseball probability calculator!
Please choose an option:
1: Compute the probability of the Red Sox winning a series with a recursive algorithm
2: Compute the probability of the Red Sox winning a series with a dynamic algorithm
3: Run interactive test suite
---
9: Exit the program
 >>  1
Please enter the number of games needed to win the series (n)
 >>  6
Please enter the probability that the Red Sox win the game
 >>  0.65
Enter 1 to print the dynamic programming table P(i, j), or 0 to skip
 >>  0
Probability: 0.8513162760788868, took 0.00034999847412109375 seconds
Press the ANY key to return to the main menu
```

The second option does the same thing, but with the dynamic algorithm instead. 

```
Welcome to the baseball probability calculator!
Please choose an option:
1: Compute the probability of the Red Sox winning a series with a recursive algorithm
2: Compute the probability of the Red Sox winning a series with a dynamic algorithm
3: Run interactive test suite
---
9: Exit the program
 >>  2
Please enter the number of games needed to win the series (n)
 >>  10
Please enter the probability that the Red Sox win the game
 >>  0.25
Probability: 0.008903279303922318, took 7.414817810058594e-05 seconds
Press the ANY key to return to the main menu
```

The third menu option allows for running both algorithms with different sized input series (different *n* values) in an automated way. It will run with *n* values from 1 to a user-input max, and run a certain number of samples at each increment. It will write the output with timing information and calculation results to a user-specified CSV file on disk. The output data is graphable in Excel or any other spreadsheet program that can read CSV.

```
Welcome to the baseball probability calculator!
Please choose an option:
1: Compute the probability of the Red Sox winning a series with a recursive algorithm
2: Compute the probability of the Red Sox winning a series with a dynamic algorithm
3: Run interactive test suite
---
9: Exit the program
 >>  3
This test suite will run both algorithms with many different n inputs (p=0.4), and time the results.
Please input the highest n you wish to test
 >>  5
Please input the number of samples to test at each n increment
 >>  2
Please input the name of the output file you wish to write
 >>  out.csv
Testing n=1...
        Run 1... Done.
        Run 2... Done.
Testing n=2...
        Run 1... Done.
        Run 2... Done.
Testing n=3...
        Run 1... Done.
        Run 2... Done.
Testing n=4...
        Run 1... Done.
        Run 2... Done.
Testing n=5...
        Run 1... Done.
        Run 2... Done.
Done! Output file out.csv written.
Press the ANY key to return to the main menu
```

The final menu option (9) will exit the program.