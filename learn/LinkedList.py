class Build:
    def __init__(self, data, next_node=None):
        #class to create nodes
        self.data = data
        self.next_node = next_node
class Head:
    def __init__(self, head=None):
        # head - star of the list
        self.head = head
    
    # add new nod
    def insert(self, data):
        node = Build(data)
        #if head not created yet -> create
        if self.head == None:
            self.head = node
            #esc after creating head
            return
        
        # start with head
        current = self.head
        # while not end of the list
        while current.next_node != None:
            # step forward
            current = current.next_node
        else:
            #if it`s end add created node
            current.next_node = node

    def display(self):
        #start with head
        current_node = self.head
        while current_node != None:
            # if not end print value and step forward
            print(current_node.data, end='-->')
            current_node = current_node.next_node
        print("END")

    #find node and it`s index
    def find_index(self, indx):
        current_node = self.head
        index = 0
        while current_node != None:
            if index == indx:
                return current_node.data 
            # if not end do step forward
            current_node = current_node.next_node
            index += 1

    def find_element(self, element):
        current_node = self.head
        index = 0
        while current_node != None:
            if current_node.data == element:
                return index
            # if not end do step forward
            current_node = current_node.next_node
            index += 1

    # remove node and change link to next node
    def remove_by_index(self, indx):
        current_node = self.head
        index = 0
        previous = None
        while current_node != None:
            if index == indx:
                previous.next_node = current_node.next_node
                break
            # if not end do step forward
            previous = current_node
            current_node = current_node.next_node
            index += 1

    def remove_by_el(self, element):
        current_node = self.head
        previous = None
        while current_node != None:
            if current_node.data == element:
                previous.next_node = current_node.next_node
                break
            # if not end do step forward
            previous = current_node
            current_node = current_node.next_node



linked_list = Head()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)


linked_list.display()
print(f"Removing element with index 2...(its {linked_list.find_index(2)})")
linked_list.remove_by_index(2)
linked_list.display()
print("Element removed")

print()

print(f"Removing element with value 2...")
linked_list.remove_by_el(2)
linked_list.display()
print("Element removed")