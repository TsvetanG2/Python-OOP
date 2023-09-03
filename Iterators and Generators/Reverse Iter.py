class reverse_iter:
    def __init__(self, obj):
        self.iter_obj = obj
        self.start_index = len(self.iter_obj) - 1 #Последният елемент от колекцията
        self.end_index = 0
        self.current_index = self.start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < self.end_index:
            raise StopIteration
        temp_index = self.current_index
        self.current_index -= 1
        return self.iter_obj[temp_index]

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)