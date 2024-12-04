class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
            self.head = None

    def add(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        
        current = self.head
        while current.next:
            current = current.next
        else: current.next = Node(val)

    def display(self):
        if self.head:
            current = self.head
            while current:
                print(f"{current.val}->", end='')
                current = current.next
            print()    

    def remove(self, val):
        if self.head:
            # if head needs to be removed - point on new head
            if self.head.val == val:
                self.head = self.head.next
                return
            
            current = self.head
            # while node isn`t found and while not the end of a list
            while current and current.next.val != val:
                current = current.next
            # if node found -> remove
            if current.next:
                current.next = current.next.next

    def lenght(self):
        if self.root:
            count = 0
            current = self.head
            while current:
                count += 1
                current = current.next
            return count

    def reverse(self):
        if self.head:

            current = self.head
            prev = None

            while current:
                # temporary store next node to iterate
                next_node = current.next
                # reverse next
                current.next = prev
                prev = current
                # step
                current = next_node
            # point on the new head 
            self.head = prev

    def contains(self, val):
        if self.head:
            current = self.head
            while current:
                if current.val == val:
                    return True
                current = current.next
            return False

    def clear(self):
        self.head = None


# end of linked list

import hashlib

# Создаем хеш-объект


hash_object = hashlib.sha256()

# start of hashset
class HashMap:
    def __init__(self, length=100):
        self.box = [None] * length
        self.length = length
        self.keys = []

    def add(self, key):
        hash = self.my_hash(key)
        if self.box[hash] is None:
            self.box[hash] = key
            self.keys.append(key)
        else:
            print("Коллизия(занято)")

    def get(self, key):
        hash = self.my_hash(key)
        return self.box[hash]

    def display(self):
        for i in (self.keys):
            print(f"{i} : {self.get(i)}", end="|")

    def my_hash(self, key):
        hashh = hash(key)
        print("Хеш-значение:", hashh, "Index: ", hashh % self.length)
        return hashh % self.length
    
object = HashMap()
object.add('cat')
object.add('hello')
object.add('keyy')
object.add('keyy')
object.add('point')
object.add('aboba')
object.add('hay')
object.display()


