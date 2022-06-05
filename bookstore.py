from book import Book


class BookStore:
    def __init__(self, store_name="Book Library", discount_on_total=5, max_total_for_discount=30) -> None:
        self._books = {}
        self.store_name = store_name

        self.__discount_on_total = 1 - (discount_on_total/100)
        self.__max_total_for_discount = max_total_for_discount

        self.__initialize_book_store_at_start()

    def change_discount(self, new_discount):
        self.__discount_on_total = 1 - (new_discount)

    def change_total_for_discount(self, new_total):
        self.__max_total_for_discount = new_total

    def add_book(self, title, price, year, minimum_year_discount=2000, discount=10, initialize=False):
        if title in self._books:
            print(
                "This book is already in store, considering we can have only 1 book at a time!")
        else:
            new_book = Book(title, price, year,
                            minimum_year_discount, discount)

            self._books[title.lower()] = new_book

            if not initialize:
                print(f"Book: {title} added in store!")

    def delete_book(self, title, checkout=False):
        if title in self._books:
            temp = self._books[title]
            del self._books[title]
            if not checkout:
                print(f"Book: {title} deleted from store!")
            return temp
        else:
            print("There is no book by this name in our store!")

    def __initialize_book_store_at_start(self):
        print("INITIALIZING STORE AT START!")
        books = [("Moby Dick", 1851, 15.20),
                 ("The Terrible Privacy of Maxwell Sim", 2010, 13.14),
                 ("Still Life With Woodpecker", 1980, 11.05),
                 ("Sleeping Murder", 1976, 10.24),
                 ("Three Men in a Boat", 1889, 12.87),
                 ("The Time Machine", 1895, 10.43),
                 ("The Caves of Steel", 1954, 8.12),
                 ("Idle Thoughts of an Idle Fellow", 1886, 7.32),
                 ("A Christmas Carol", 1843, 4.23),
                 ("A Tale of Two Cities", 1859, 6.32),
                 ("Great Expectations", 1861, 13.21)]

        for each in books:
            self.add_book(each[0], each[-1], each[1], initialize=True)

        print("Book store initialized at start!")

    def __str__(self) -> str:
        text = f"\nIn '{self.store_name}', following books are available:\n"

        for values in self._books.values():
            text += "- " + str(values) + "\n"

        return text

    def purchase(self):
        purchases = []

        while True:
            print(self)

            book_name = input(
                "Please enter book name(-1 to checkout): ").lower().strip()
            if book_name == "-1":
                break

            if book_name in purchases:
                print("You have already added this book in order list!")

            else:
                if book_name not in self._books:
                    print("Sorry, we do not have this book in our store!")
                else:
                    purchases.append(book_name)
                    print("Book added in order list!")

        return purchases

    def check_out(self, books):
        total_price = 0

        for each in books:
            book = self.delete_book(each, checkout=True)
            if book is not None:
                total_price += book.price

        if total_price > self.__max_total_for_discount:
            total_price = total_price * self.__discount_on_total

        text = "Buying "
        for each in books:
            text += each.title() + ", "

        text += f"will cost £{total_price:.2f}."

        return text
