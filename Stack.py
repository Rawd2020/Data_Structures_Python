class Stack(object):
    '''A basic stack implementation'''
    def __init__(self, data = []):
        self.data = data
    
    def isEmpty(self):
        return not bool(self.data)

    def push(self, value):
        self.data.append(value)

    def pop(self):
        try:
            return self.data.pop()
        except IndexError:
            return None

    def peek(self):
        try:
            return self.data[-1]
        except IndexError:
            return None


if __name__ == '__main__':
    pass

