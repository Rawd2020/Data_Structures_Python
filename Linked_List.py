class Node(object):
    '''This data node object will be used by the Linked_List class.'''
    def __init__(self, data = None, ref = None):
        self.data = data
        self.ref = ref


class Linked_List(object):
    '''A basic linked list implementation.'''
    def __init__(self, head = None):
        self.head = head
    
    def insert(self, data):
        new_node = Node(data = data, ref = self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.ref
        return count

    def search(self, query_data):
        current = self.head
        found = False
        while current and not found:
            if current.data == query_data:
                found = True
            else:
                current = current.ref
        if current is None:
            raise ValueError("Data not found in list.")
        return current

    def delete(self, query_data):
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.data == query_data:
                found = True
            else:
                previous = current
                current = current.ref
        if current is None:
            raise ValueError("Data not found in list.")
        elif previous is None:
            self.head = current.ref
        else:
            previous.ref = current.ref

    def __str__(self):
        data = ''
        current = self.head
        while current:
            data += '"' + str(current.data) + '",'
            current = current.ref
        return data[0:-1]

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.ref


if __name__ == '__main__':
    pass

