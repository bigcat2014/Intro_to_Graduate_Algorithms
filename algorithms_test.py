#!/usr/bin/env python3

import argparse
import os
from timeit import timeit

from fib import FIB1, FIB2
from lis import LIS

FLAGS = None

# <editor-fold desc='Command Line'>


def add_positional_arguments(parser):
    pass


def add_optional_arguments(parser):
    parser.add_argument(
        '-f',
        dest='fibonacci',
        default=False,
        help='Run the fibonacci sequence tests.',
        action='store_true'
    )
    parser.add_argument(
        '-l',
        dest='increasing_subsequence',
        default=False,
        help='Run the longest increasing subsequence tests.',
        action='store_true'
    )
    parser.add_argument(
        '-c',
        dest='common_subsequence',
        default=False,
        help='Run the longest common subsequence tests.',
        action='store_true'
    )


def parse_args():
    global FLAGS

    parser = argparse.ArgumentParser(
        description="""
            A program for testing the different algorithms implemented
            for the Intro to Graduate Algorithms Udacity course.
        """
    )

    add_positional_arguments(parser)
    add_optional_arguments(parser)
    FLAGS, _ = parser.parse_known_args()

# </editor-fold>


# <editor-fold desc='Wrapper Functions'>

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

# </editor-fold>


def main():
    if FLAGS.fibonacci:
        print('Running Fibonacci test...')

        fib1_of_0 = wrapper(FIB1, 0)
        fib1_of_10 = wrapper(FIB1, 10)
        fib1_of_30 = wrapper(FIB1, 30)

        fib2_of_0 = wrapper(FIB2, 0)
        fib2_of_10 = wrapper(FIB2, 10)
        fib2_of_30 = wrapper(FIB2, 30)
        fib2_of_100 = wrapper(FIB2, 100)

        print('FIB1(0) time: {time}'.format(time=timeit(fib1_of_0, number=1)))
        print('FIB1(10) time: {time}'.format(
            time=timeit(fib1_of_10, number=1)))
        print('FIB1(30) time: {time}\n'.format(
            time=timeit(fib1_of_30, number=1)))

        print('FIB1(0) time: {time}'.format(time=timeit(fib2_of_0, number=1)))
        print('FIB1(10) time: {time}'.format(
            time=timeit(fib2_of_10, number=1)))
        print('FIB1(30) time: {time}'.format(
            time=timeit(fib2_of_30, number=1)))
        print('FIB1(100) time: {time}\n'.format(
            time=timeit(fib2_of_100, number=1)))

    if FLAGS.increasing_subsequence:
        print('Running Longest Increasing Subsequence test...')

        wrapped_lis = wrapper(LIS, [5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3])
        print('LIS([5, 7, 4, -3, 9, 1, 10, 4, 5, 8, 9, 3]) time: {time}\n'.format(
            time=timeit(wrapped_lis, number=1)
        ))

    if FLAGS.common_subsequence:
        print('Running Longest Common Subsequence test...')

        print('LCS(None) time: {time}\n'.format(time=0))


if __name__ == '__main__':
    parse_args()
    main()
