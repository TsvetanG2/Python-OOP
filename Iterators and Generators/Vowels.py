class vowels:

    def __init__(self, sentence: str):
        self.sentence = sentence
        self.current_index = -1
        self.all_vowels = ['a', 'e', 'i', 'o', 'y', 'u']
        self.end_index = len(self.sentence) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        if self.current_index > self .end_index:
            raise StopIteration
        current_element = self.sentence[self.current_index]
        if current_element.lower() in self.all_vowels:
            return current_element
        return next(self)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
