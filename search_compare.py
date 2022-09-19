import time
import random


def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    
    time_spent = time.time() - start
    return [found, time_spent]


def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    a_list = sorted(a_list)
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1
    time_spent = time.time() - start

    return [found, time_spent]


def binary_search_iterative(a_list,item):
    start = time.time()
    first = 0

    a_list = sorted(a_list)
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    
    time_spent = time.time() - start

    return [found, time_spent]
    
    
def binary_search_recursive(a_list,item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)


def binary_search_recursive_time(mylist, search):
    start = time.time()
    found = binary_search_recursive(mylist, search)
    time_spent = time.time() - start
    return [found, time_spent]


if __name__ == "__main__":
    """Main entry point"""
    the_size = 500

    total_time = 0
    searches = ['Sequential Search', 'Ordered Sequential Search', 'Binary Search Iterative', 'Binary Search Recrusive']
    for index in range(4):
        if index == 0:
            total_time = 0
            for i in range(100):
                mylist = get_me_random_list(the_size)
                total_time += sequential_search(mylist, -1)[1]

            avg_time = total_time / 100
            print(f"{searches[index]} took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
        elif index == 1:
            total_time = 0
            for i in range(100):
                mylist = get_me_random_list(the_size)
                total_time += ordered_sequential_search(mylist, -1)[1]

            avg_time = total_time / 100
            print(f"{searches[index]} took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
        elif index == 2:
            total_time = 0 
            for i in range(100):
                mylist = get_me_random_list(the_size)
                total_time += binary_search_iterative(mylist, -1)[1]

            avg_time = total_time / 100
            print(f"{searches[index]} took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
        elif index == 3:
            total_time = 0
            for i in range(100):
                mylist = get_me_random_list(the_size)
                total_time += binary_search_recursive_time(mylist, -1)[1]

            avg_time = total_time / 100
            print(f"{searches[index]} took {avg_time:10.7f} seconds to run, on average for a list of {the_size} elements")
