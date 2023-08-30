#!/usr/bin/python3
"""singly-linked definatn"""


class Node:
    """Node class body"""

    def __init__(self, data, next_node=None):
        """Node constructor
        Args:
            data (int): This is the data of the new Node
            next_node (Node): This is the next node of the new Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """The setter and getter of a Node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """The getter and setter of a Node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly-linked definatn"""

    def __init__(self):
        """SinglyLinkedList constructor"""
        self.__head = None

    def sorted_insert(self, value):
        """We insert a new Node to the SinglyLinked list
        at the correct ordered numerical position
        Args:
            value (Node): This is the new Node to be inserted
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """We define the print() rep. of a SinglyLinked list"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
