#!/usr/bin/python3
"""main program"""
#import packages
from model.colors import Colors
from generator.generate import generate_int
from recursive.search_number import search
from fibonacci.fib import fib

def main():
    #create colors instance
    colors = Colors('html/python_class_question.html')
    #print mean of colors
    print('mean color: {}'.format(colors
          .get_mean_color()))
    #print median of colors
    print('median color: {}'.format(colors
          .get_median_color()))
    #print mode of colors
    print('color mostly worn: {}'.format(colors.
          get_mode_color()))
    #print variance of colors
    print('variance of colors: {}'.format(colors
          .get_variance()))
    #print probablity of picking red at random
    print('probablity of picking red: {}'.format(colors.
          get_prob('RED')))
    #print random int
    print('random integer: {}'.format(generate_int()))
    #search for a number in a list of numbers
    numbers = [7, 90, 5, 20, 3, 4, 8]
    #print index of 3 in @numbers
    print('index of 3: {}'.format(search(3, numbers)))
    #print list of first 50 fibonacci numbers
    print('first 50 fibonacci numbers: {}'.format(fib()))
    #print their length
    print('length of fibonacci: {}'.format(len(fib())))
    #bye
    print('bye')

if __name__ == '__main__':
    main()
