#!/usr/bin/python3

""" class MyList that inherits from list """


class MyList(list):
    """
    Customized list class with additional functionality.

    Public Methods:
    - print_sorted(self): Prints the list in ascending order.

    Note: Assumes that all elements of the list are of type int.

    Example Usage:
    >>> my_list = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    >>> print(my_list)
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    >>> my_list.print_sorted()
    [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        Returns:
        None
        """
        # Print the sorted list (ascending order)
        sorted_list = sorted(self)
        print(sorted_list)
