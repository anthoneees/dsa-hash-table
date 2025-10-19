class Node:
    def __init__(self, value=None, key=None):
        self.value = value
        self.key = key
        self.next = None

    def __str__(self):
        return f"({self.key}: {self.value})"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, key, value):
        newNode = Node(value, key)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.length += 1
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1

    def getValue(self, key):
        curr = self.head
        while curr is not None:
            if curr.key == key:
                return curr.value
            curr = curr.next

        return None

    def setNode(self, key, value):
        curr = self.head
        while curr is not None:
            if curr.key == key:
                curr.value = value
                return True
            curr = curr.next

        return False

    def remove(self, key):
        prev = None
        curr = self.head

        while curr is not None:
            if curr.key == key:
                if prev is None:
                    self.head = curr.next
                else:
                    prev.next = curr.next

                if curr == self.tail:
                    self.tail = prev

                self.length -= 1
                return
            prev = curr
            curr = curr.next

    def __str__(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(f"{curr.key}: {curr.value}")
            curr = curr.next
        return " -> ".join(elements) if elements else "Empty"


class Table:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.data = [LinkedList() for _ in range(self.capacity)]
        self.size = 0

    def _get_hash(self, key):
        return hash(key) % self.capacity

    def _resize(self, capacity):
        newData = [LinkedList() for _ in range(capacity)]

        for node in self.data:
            temp = node.head
            while temp is not None:
                index = hash(temp.key) % capacity
                newData[index].append(temp.key, temp.value)
                temp = temp.next

        self.data = newData
        self.capacity = capacity

    def insert(self, key, value):
        index = self._get_hash(key)
        node_value = self.data[index].getValue(key)
        if node_value is not None:
            self.data[index].setNode(key, value)
        else:
            self.data[index].append(key, value)
            self.size += 1

            if self.size / self.capacity > 0.7:
                self._resize(self.capacity * 2)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        index = self._get_hash(key)

        return self.data[index].getValue(key) is not None

    def search(self, key):
        if self.size == 0:
            return
        index = self._get_hash(key)

        value = self.data[index].getValue(key)
        if value is not None:
            return value
        return None

    def delete(self, key):
        if self.size == 0:
            return
        index = self._get_hash(key)

        self.data[index].remove(key)
        self.size -= 1

    def __str__(self):
        result = []
        for i, bucket in enumerate(self.data):
            result.append(f"Bucket {i}: {bucket}")
        return "\n".join(result)

    def printValues(self):
        result = []
        for bucket in self.data:
            curr = bucket.head
            while curr:
                result.append(f"{curr.key}: {curr.value}")
                curr = curr.next
        print("\n".join(result))


def test_linked_list():
    print("Testing LinkedList...")
    ll = LinkedList()

    # Append and getValue
    ll.append("a", 1)
    ll.append("b", 2)
    ll.append("c", 3)

    assert ll.length == 3
    assert ll.getValue("a") == 1
    assert ll.getValue("b") == 2
    assert ll.getValue("c") == 3
    assert ll.getValue("d") is None

    # setNode
    assert ll.setNode("b", 20) == True
    assert ll.getValue("b") == 20
    assert ll.setNode("x", 100) == False

    # remove
    ll.remove("b")
    assert ll.length == 2
    assert ll.getValue("b") is None

    ll.remove("a")
    ll.remove("c")
    assert ll.length == 0
    assert ll.head is None and ll.tail is None

    print("LinkedList tests passed!\n")


def test_hash_table():
    print("Testing Table...")
    ht = Table(capacity=5)

    # Insert and search
    ht.insert("apple", 1)
    ht.insert("banana", 2)
    ht.insert("cherry", 3)

    assert len(ht) == 3
    assert "apple" in ht
    assert "banana" in ht
    assert ht.search("cherry") == 3
    assert ht.search("durian") is None

    # Update existing key
    ht.insert("banana", 20)
    assert ht.search("banana") == 20

    # Delete
    ht.delete("apple")
    assert len(ht) == 2
    assert "apple" not in ht

    ht.delete("banana")
    ht.delete("cherry")
    assert len(ht) == 0

    # Test collisions (force small capacity)
    ht_small = Table(capacity=2)
    ht_small.insert("key1", 10)
    ht_small.insert("key2", 20)  # likely same bucket
    ht_small.insert("key3", 30)  # triggers resize
    assert ht_small.capacity >= 4  # should resize
    assert ht_small.search("key1") == 10
    assert ht_small.search("key2") == 20
    assert ht_small.search("key3") == 30

    print("Table tests passed!\n")


if __name__ == "__main__":
    test_linked_list()
    test_hash_table()
    print("All tests passed!")
