class Deque:

    def __init__(self):
        self._data = []

    def is_empty(self):
        if len(self._data) == 0:
            return 0
        else:
            return 1
                  
    def add_first(self, value):
        self._data.insert(0, value)
        print(self._data, 'first element added')

    def add_last(self, value):
        self._data.append(value)
        print(self._data, 'last element added')

    def del_first(self):
        if self.is_empty() == 1:
            print('first element deleted which is ', self._data.pop(0))
            print(self._data)
                 
        else:
            print('The stack is empty')

    def del_last(self):
        if self.is_empty() == 1:
            print('last element deleted which is', self._data.pop())
            print(self._data) 
        else:
            print('The stack is empty')
            
d = Deque()
d.add_first(2)
d.add_first(1)
d.add_last(3)
d.add_last(4)
d.del_first()
d.del_last()


        
        
