class Node:
    '''
    An oblect for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    '''
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return '%s' % self.data
        

class LinkedList:
    '''
    Singly linked list
    '''

    def __init__(self): 
        self.head = None

    def is_Empty(self):
        return self.head == None

    def size(self):
        '''
        Return the number of nodes in the list
        Takes 0(n) time
        '''

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        
        return count

    def add(self, data):
        '''
        Adds nes node containing data at head of the list 
        '''
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
    

    def search(self, key):
        '''
        Search for the first node containing data that matches the key
        '''
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    # def verify(self, index):
    #     if index is not None:
    #         print(index)
    #     else:
    #         print('not found')

    def insert(self, data, index):
        '''
        insert a new node containing data at index position
        '''
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = Node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current is not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def node_at_index(self, index):
        if index == 0:
            return self.head 
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append('[Head: %s]' % current.data)
            elif current.next_node is None:
                nodes.append('[Tail: %s]' % current.data)
            else:
                nodes.append('[%s]' % current.data)

            current = current.next_node
        return '->'.join(nodes)


# l = LinkedList()
# N = Node(10)
# N2 = Node(20)
# l.head = N
# l.add(N2)
# l.add(30)
# # search = l.search(10)
# # print(search)
# l.insert(15,1)
# print(l)
# l.remove(10)
# print(l)