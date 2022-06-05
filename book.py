class Book:
    def __init__(self, title, price, year, minimum_year_discount=2000, discount=10) -> None:
        self.__title = title
        self.__price = price
        self.__year = year
        self.__minimum_year_discount = minimum_year_discount
        self.__discount = discount

    @property
    def price(self):
        if self.__year > self.__minimum_year_discount:
            return self.__price * (1-(self.__discount/100))
        else:
            return self.__price

    @property
    def title(self):
        return self.__title

    @property
    def year(self):
        return self.__year

    def __str__(self) -> str:
        return f"{self.__title} ({self.__year}) £{self.price:.2f}"
