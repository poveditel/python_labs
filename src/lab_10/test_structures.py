#!/usr/bin/env python

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lab_10.structures import Stack, Queue
from lab_10.linked_list import SinglyLinkedList, Node


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_init(self):
        self.assertEqual(len(self.stack), 0)
        self.assertTrue(self.stack.is_empty())

    def test_push_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(len(self.stack), 3)
        self.assertFalse(self.stack.is_empty())

        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

        self.assertEqual(len(self.stack), 0)
        self.assertTrue(self.stack.is_empty())

    def test_peek(self):
        self.assertIsNone(self.stack.peek())

        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(len(self.stack), 2)

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.stack.pop()


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_init(self):
        self.assertEqual(len(self.queue), 0)
        self.assertTrue(self.queue.is_empty())

    def test_enqueue_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertEqual(len(self.queue), 3)
        self.assertFalse(self.queue.is_empty())

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)

        self.assertEqual(len(self.queue), 0)
        self.assertTrue(self.queue.is_empty())

    def test_peek(self):
        self.assertIsNone(self.queue.peek())

        self.queue.enqueue(1)
        self.queue.enqueue(2)

        self.assertEqual(self.queue.peek(), 1)
        self.assertEqual(len(self.queue), 2)

    def test_dequeue_empty(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()


class TestNode(unittest.TestCase):
    def test_init(self):
        node = Node(42)
        self.assertEqual(node.value, 42)
        self.assertIsNone(node.next)


class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = SinglyLinkedList()

    def test_init(self):
        self.assertIsNone(self.ll.head)
        self.assertIsNone(self.ll.tail)
        self.assertEqual(len(self.ll), 0)

    def test_append(self):
        self.ll.append(1)
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.tail.value, 1)
        self.assertIsNone(self.ll.head.next)
        self.assertEqual(len(self.ll), 1)

        self.ll.append(2)
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.tail.value, 2)
        self.assertEqual(self.ll.head.next.value, 2)
        self.assertIsNone(self.ll.tail.next)
        self.assertEqual(len(self.ll), 2)

    def test_prepend(self):
        self.ll.prepend(1)
        self.assertEqual(self.ll.head.value, 1)
        self.assertEqual(self.ll.tail.value, 1)
        self.assertIsNone(self.ll.head.next)
        self.assertEqual(len(self.ll), 1)

        self.ll.prepend(0)
        self.assertEqual(self.ll.head.value, 0)
        self.assertEqual(self.ll.tail.value, 1)
        self.assertEqual(self.ll.head.next.value, 1)
        self.assertIsNone(self.ll.tail.next)
        self.assertEqual(len(self.ll), 2)

    def test_insert(self):
        self.ll.insert(0, 1)
        self.assertEqual(list(self.ll), [1])

        self.ll.insert(0, 0)
        self.assertEqual(list(self.ll), [0, 1])

        self.ll.insert(2, 2)
        self.assertEqual(list(self.ll), [0, 1, 2])

        self.ll.insert(1, 0.5)
        self.assertEqual(list(self.ll), [0, 0.5, 1, 2])

        with self.assertRaises(IndexError):
            self.ll.insert(-1, -1)
        with self.assertRaises(IndexError):
            self.ll.insert(10, 10)

    def test_remove_at(self):
        for i in range(5):
            self.ll.append(i)
        self.assertEqual(list(self.ll), [0, 1, 2, 3, 4])

        self.ll.remove_at(2)
        self.assertEqual(list(self.ll), [0, 1, 3, 4])

        self.ll.remove_at(0)
        self.assertEqual(list(self.ll), [1, 3, 4])

        self.ll.remove_at(2)
        self.assertEqual(list(self.ll), [1, 3])

        self.ll.remove_at(0)
        self.ll.remove_at(0)
        self.assertEqual(len(self.ll), 0)
        self.assertIsNone(self.ll.head)
        self.assertIsNone(self.ll.tail)

        with self.assertRaises(IndexError):
            self.ll.remove_at(0)

    def test_remove(self):
        for i in [1, 2, 3, 2, 4]:
            self.ll.append(i)
        self.assertEqual(list(self.ll), [1, 2, 3, 2, 4])

        self.ll.remove(2)
        self.assertEqual(list(self.ll), [1, 3, 2, 4])

        self.ll.remove(5)
        self.assertEqual(list(self.ll), [1, 3, 2, 4])

        empty_ll = SinglyLinkedList()
        empty_ll.remove(1)
        self.assertEqual(len(empty_ll), 0)

    def test_iter(self):
        values = [1, 2, 3, 4, 5]
        for value in values:
            self.ll.append(value)

        iterated_values = list(self.ll)
        self.assertEqual(iterated_values, values)

    def test_repr(self):
        self.assertEqual(repr(self.ll), "SinglyLinkedList([])")

        self.ll.append(1)
        self.ll.append(2)
        self.assertEqual(repr(self.ll), "SinglyLinkedList([1, 2])")

    def test_display(self):
        self.assertEqual(self.ll.display(), "None")

        self.ll.append(1)
        self.assertEqual(self.ll.display(), "[1] -> None")

        self.ll.append(2)
        self.assertEqual(self.ll.display(), "[1] -> [2] -> None")


if __name__ == "__main__":
    unittest.main()
