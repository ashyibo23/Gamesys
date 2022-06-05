from bookstore import BookStore
# Still Life With Woodpecker
# Three Men in a Boat
# Great Expectations

def main():
    my_store = BookStore("My Book Store")

    while True:
        choice = input("""
              Main menu:
1. List down all books
2. Purchas book(s)
3. Add a book in store
4. Change discount
5. Change discount for total
6. Exit

Please enter your choice: """)

        if choice == "1":
            print(my_store)
        elif choice == "2":
            to_be_checked_out = my_store.purchase()

            go_ahead = input(
                "Do you want to go for checkout!, Press 1 to proceed otherwise any other thing will cancel checkout: ")
            if go_ahead == "1":
                text = my_store.check_out(to_be_checked_out)
                print("Thank you for checking out, following are details:")
                print(text)

        elif choice == "3":
            name = input("Please enter title of new book: ")
            price = float(
                input("Please enter only numbers for price of new book: "))
            year = int(
                input("Please enter only numbers for year of new book: "))
            discount = float(
                input("Please enter only numbers for discount of new book(-1 for default): "))
            year = int(
                input("Please enter only numbers for max year of new book to give discount: "))

            if discount == "-1" and year != "-1":
                my_store.add_book(name, price, year,
                                  minimum_year_discount=year)
            elif year == "-1" and discount != "-1":
                my_store.add_book(name, price, year, discount=discount)
            elif discount != "-1" and year != "-1":
                my_store.add_book(
                    name, price, year, minimum_year_discount=year, discount=discount)
            else:
                my_store.add_book(name, price, year)
        elif choice == "4":
            discount = float(
                input("Please enter only numbers for new discount on total price: "))
            my_store.change_discount(discount)
        elif choice == "5":
            price = float(
                input("Please enter only numbers for new price to give discount on: "))
            my_store.change_discount(price)
        elif choice == "6":
            print("Thank you!")
            break
        else:
            print("Invalid option selected!")


main()
