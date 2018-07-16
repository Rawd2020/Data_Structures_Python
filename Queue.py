class Queue(object):
    '''A basic queue implementation.'''
    def __init__(self, data = []):
        self.data = data

    def isEmpty(self):
        return not bool(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        try:
            value = self.data[0]
            self.data = self.data[1:]
            return value
        except IndexError:
            return None

    def size(self):
        return len(self.data)

    def peek(self):
        try:
            return self.data[0]
        except IndexError:
            return None


if __name__ == '__main__':
    pass

