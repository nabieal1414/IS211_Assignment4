import argparse
# other imports go here

import random
import time

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    

def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
    time_spent = time.time() - start
    return time_spent


def shellSort(alist):
    start = time.time()
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)

        # print("After increments of size", sublistcount, "The list is",alist)

        sublistcount = sublistcount // 2
    time_spent = time.time() - start
    return time_spent


def gapInsertionSort(alist, start, gap):
    startTime = time.time()
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue
    time_spent = time.time() - startTime
    return time_spent


def python_sort(a_list):
    """
    Use Python built-in sorted function

    :param a_list:
    :return: the sorted list
    """
    start = time.time()
    sorted_list = sorted(a_list)
    time_spent = time.time() - start
    return time_spent


if __name__ == "__main__":
    """Main entry point"""
    list_sizes = [500, 1000, 5000]

    # the_size = list_sizes[0]
    sorting_algos = ['Insertion Sort', 'Shell Sort', 'Gap Insertion Sort', 'Python Sort']
    for index in range(4):
        randomSize = random.randrange(3)
        the_size = list_sizes[randomSize]
        if index == 0:
                total_time = 0
                for i in range(100):
                    mylist500 = get_me_random_list(the_size)
                    total_time += insertion_sort(mylist500)
                
                avg_time = total_time / 100    
                print(f"{sorting_algos[index]} took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
        elif index == 1:
            total_time = 0
            for i in range(100):
                mylist500 = get_me_random_list(the_size)
                total_time += shellSort(mylist500)

            avg_time = total_time / 100    
            print(f"{sorting_algos[index]} took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
        elif index == 2:
            total_time = 0
            for i in range(100):
                mylist500 = get_me_random_list(the_size)
                total_time += gapInsertionSort(mylist500, 0, randomSize)
            avg_time = total_time / 100    
            print(f"{sorting_algos[index]} took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
        elif index == 3:
            total_time = 0
            for i in range(100):
                mylist500 = get_me_random_list(the_size)
                total_time += python_sort(mylist500)

            avg_time = total_time / 100
            print(f"{sorting_algos[index]} took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
            
