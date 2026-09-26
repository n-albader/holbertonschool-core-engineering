#!/usr/bin/env python3

"""Defines the VerboseList class"""


class VerboseList(list):
    """A list that print messages when modified"""

    def append(self, item):
        """Add an item and print a notification"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print the number of items added"""
        count = len(iterable)
        super().extend(iterable)
        print("Extend the list with [{}] item.".format(count))

    def remove(self, item):
        """Remove and item and print a notification"""
        print("Remove [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Remove and retern an item with a notification"""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
