class Book:
    def __init__(self, content: str):
        self.content = content


class BaseFormatter:
    def format(self, book: Book) -> str:
        return book.content


class WebFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"{book.content}"


class Printer:
    def __init__(self, formatter: BaseFormatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        return self.formatter.format(Book)