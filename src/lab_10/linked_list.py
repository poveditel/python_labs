from typing import Any


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next: "Node" | None = None


class SinglyLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size = 0

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            # Список пуст
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError("Индекс вне диапазона")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        new_node = Node(value)
        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self._size += 1

    def remove_at(self, idx: int) -> None:
        if idx < 0 or idx >= self._size:
            raise IndexError("Индекс вне диапазона")

        if idx == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        node_to_remove = current.next
        current.next = node_to_remove.next

        if node_to_remove == self.tail:
            self.tail = current

        self._size -= 1

    def remove(self, value: Any) -> None:
        if self.head is None:
            return  # Список пуст

        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return

        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next

        if current.next is not None:
            node_to_remove = current.next
            current.next = node_to_remove.next

            if node_to_remove == self.tail:
                self.tail = current

            self._size -= 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        values = list(self)
        return f"SinglyLinkedList({values})"

    def display(self) -> str:
        if self.head is None:
            return "None"

        result = ""
        current = self.head
        while current is not None:
            result += f"[{current.value}]"
            if current.next is not None:
                result += " -> "
            else:
                result += " -> None"
            current = current.next
        return result
