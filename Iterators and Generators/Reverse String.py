def reverse_text(text):
    yield text[::-1]

for char in reverse_text("step"):
    print(char, end='')