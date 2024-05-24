class Book:
    material = 'бумага'
    text = True

    def __init__(self, book_name, author, number_pages, isbn, reservation=False):
        self.book_name = book_name
        self.author = author
        self.number_pages = number_pages
        self.isbn = isbn
        self.reservation = reservation

    def book_details(self):
        details = (f"Название: {self.book_name}, Автор: {self.author}, "
                   f"Страниц: {self.number_pages}, Материал: {self.material}")
        if self.reservation:
            details += ", зарезервирована"
        return details


book1 = Book('Идиот', 'Достоевский', 500, '177777777')
book2 = Book('Собачье сердце', 'Булгаков', 341, '88888999888')
book3 = Book('Портрет Дориана Грея', 'Уайльд', 278, '1777677-01', True)
book4 = Book('Ярмарка тщеславия', 'Теккерей', 190, '000045657')
book5 = Book('Отцы и дети', 'Тургенев', 454, '12324345')


class SchoolBook(Book):

    def __init__(self, book_name, author, number_pages, isbn, subject, student_group, tasks, reservation=False):
        super().__init__(book_name, author, number_pages, isbn, reservation)
        self.subject = subject
        self.student_group = student_group
        self.tasks = tasks

    def book_details(self):
        details = super().book_details()
        details = details.rstrip(", зарезервирована")
        details += (f", Предмет: {self.subject}, Класс: {self.student_group}")
        if self.reservation:
            details += ", зарезервирована"
        return details


school_book1 = SchoolBook('Алгебра', 'Иванов', 124, '177777777', "Математика", 7, True)
school_book2 = SchoolBook('Биология', 'Петров', 85, '88888999888', "Биология", 6, True)
school_book3 = SchoolBook('География', 'Сидоров', 99, '1777677-01', "География", 8, True, True)


books = [book1, book2, book3, book4, book5, school_book1, school_book2, school_book3]

books_list = "\n".join(book.book_details() for book in books)

print(books_list)
