import unittest
from book import Book
from bookstore import BookStore


class BookStoreTests(unittest.TestCase):
    def test_store_name(self):
        store_name = "TESTING STORE"
        store = BookStore(store_name)

        self.assertEqual(store.store_name, store_name)

    def test_add_book(self):
        store = BookStore()
        store.add_book("Test title", 50, 1959)
        self.assertIn("Test title".lower(), store._books)

    def test_books_checkout1(self):
        store = BookStore()
        # Buying The Terrible Privacy of Maxwell Sim, Three Men in a Boat, will cost £24.69
        result = store.check_out(
            ['The Terrible Privacy of Maxwell Sim'.lower(), 'Three Men in a Boat'.lower()])
        self.assertEqual(
            result, "Buying The Terrible Privacy Of Maxwell Sim, Three Men In A Boat, will cost £24.70.")

    def test_books_checkout2(self):
        store = BookStore()
        # Buying The Terrible Privacy of Maxwell Sim, Three Men in a Boat, will cost £24.69
        result = store.check_out(
            ['Still Life With Woodpecker'.lower(), 'Three Men in a Boat'.lower(), 'Great Expectations'.lower()])
        self.assertEqual(
            result, "Buying Still Life With Woodpecker, Three Men In A Boat, Great Expectations, will cost £35.27.")

    def test_books_checkout3(self):
        store = BookStore()
        # Buying The Terrible Privacy of Maxwell Sim, Three Men in a Boat, will cost £24.69
        result = store.check_out(
            ['The Terrible Privacy of Maxwell Sim'.lower(), 'Three Men in a Boat'.lower(), 'Great Expectations'.lower()])
        self.assertEqual(
            result, "Buying The Terrible Privacy Of Maxwell Sim, Three Men In A Boat, Great Expectations, will cost £36.01.")


class BookTest(unittest.TestCase):
    def test_book(self):
        book_name = "Test book"
        book_year = 1985
        book_price = 9.32
        book_obj = Book(book_name, book_price, book_year)

        self.assertEqual(book_name, book_obj.title)
        self.assertEqual(book_year, book_obj.year)
        self.assertEqual(book_price, book_obj.price)

    def test_book_price(self):
        book_name = "Test book"
        book_year = 2005
        book_price = 9.32
        book_obj = Book(book_name, book_price, book_year)

        self.assertEqual(book_name, book_obj.title)
        self.assertEqual(book_year, book_obj.year)
        self.assertEqual(8.388, book_obj.price)

    def test_book_change_discount_year(self):
        book_name = "Test book"
        book_year = 2005
        book_price = 9.32
        book_obj = Book(book_name, book_price, book_year, 2006)

        self.assertEqual(book_name, book_obj.title)
        self.assertEqual(book_year, book_obj.year)
        self.assertEqual(9.32, book_obj.price)

    def test_book_change_discount(self):
        book_name = "Test book"
        book_year = 2005
        book_price = 9.32
        book_obj = Book(book_name, book_price, book_year, discount=75)

        self.assertEqual(book_name, book_obj.title)
        self.assertEqual(book_year, book_obj.year)
        self.assertEqual(2.33, book_obj.price)

    def test_book_change_discount_and_year(self):
        book_name = "Test book"
        book_year = 2005
        book_price = 9.32
        book_obj = Book(book_name, book_price, book_year, 2004, 50)

        self.assertEqual(book_name, book_obj.title)
        self.assertEqual(book_year, book_obj.year)
        self.assertEqual(4.66, book_obj.price)


if __name__ == '__main__':
    unittest.main()
