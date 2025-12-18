#!/usr/bin/env python

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from lab_10.structures import Stack, Queue
from lab_10.linked_list import SinglyLinkedList


def demo_stack():
    print("=== Stack Demo ===")
    stack = Stack()

    print("Добавляем элементы: 1, 2, 3")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Стек: {stack}")
    print(f"Размер: {len(stack)}")

    print(f"Верхний элемент: {stack.peek()}")

    print("Извлекаем элементы:")
    while not stack.is_empty():
        item = stack.pop()
        print(f"  Извлечен: {item}")
    print()


def demo_queue():
    print("=== Queue Demo ===")
    queue = Queue()

    print("Добавляем элементы: 'первый', 'второй', 'третий'")
    queue.enqueue("первый")
    queue.enqueue("второй")
    queue.enqueue("третий")
    print(f"Очередь: {queue}")
    print(f"Размер: {len(queue)}")

    print(f"Первый элемент: {queue.peek()}")

    print("Извлекаем элементы:")
    while not queue.is_empty():
        item = queue.dequeue()
        print(f"  Извлечен: {item}")
    print()


def demo_linked_list():
    print("=== SinglyLinkedList Demo ===")
    ll = SinglyLinkedList()

    print("Добавляем элементы в конец: 1, 2, 3")
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(f"Список: {ll}")
    print(f"Красивый вывод: {ll.display()}")
    print(f"Размер: {len(ll)}")

    print("\nДобавляем элемент в начало: 0")
    ll.prepend(0)
    print(f"Список: {ll}")
    print(f"Красивый вывод: {ll.display()}")

    print("\nВставляем элемент 1.5 по индексу 2")
    ll.insert(2, 1.5)
    print(f"Список: {ll}")
    print(f"Красивый вывод: {ll.display()}")

    print("\nУдаляем элемент 1.5")
    ll.remove(1.5)
    print(f"Список: {ll}")
    print(f"Красивый вывод: {ll.display()}")

    print("\nУдаляем элемент по индексу 0")
    ll.remove_at(0)
    print(f"Список: {ll}")
    print(f"Красивый вывод: {ll.display()}")

    print("\nИтерация по списку:")
    for i, value in enumerate(ll):
        print(f"  Индекс {i}: {value}")
    print()


if __name__ == "__main__":
    demo_stack()
    demo_queue()
    demo_linked_list()
