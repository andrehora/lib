class Book:

    REGULAR: int = 0
    NEW_RELEASE: int = 1
    CHILDREN: int = 2

    def __init__(self, title: str, price_code: int):
        self._title = title
        self._price_code = price_code

    @property
    def title(self) -> str:
        return self._title

    @property
    def price_code(self) -> int:
        return self._price_code

class Rental:

    def __init__(self, book: Book, days_rented: int):
        self._book = book
        self._days_rented = days_rented

    @property
    def book(self) -> Book:
        return self._book

    @property
    def days_rented(self) -> int:
        return self._days_rented
    
    def get_charge(self) -> float:

        amount = 0
        if self.book.price_code == Book.REGULAR:
            amount += 2
            if self.days_rented > 2:
                amount += (self.days_rented - 2) * 1.5
        elif self.book.price_code == Book.NEW_RELEASE:
            amount += self.days_rented * 3
        elif self.book.price_code == Book.CHILDREN:
            amount += 1.5
            if self.days_rented > 3:
                amount += (self.days_rented - 3) * 1.5
                
        return amount
    
    def get_frequent_renter_points(self):

        points = 1
        if self.book.price_code == Book.NEW_RELEASE and self.days_rented > 1:
            points += 1
        return points

class Client:

    def __init__(self, name: str):
        self._name = name
        self._rentals = []

    def add_rental(self, rental: Rental):
        self._rentals.append(rental)

    @property
    def name(self) -> str:
        return self._name

    def statement(self) -> str:

        result = f"Rental summary for {self.name}\n"
        for rental in self._rentals:
            result += f"- {rental.book.title}: {rental.get_charge()}\n"
        
        result += f"Total: {self.get_total_charge()}\n"
        result += f"Points: {self.get_total_frequent_renter_points()}"
        return result
    
    def get_total_charge(self) -> float:

        total_amount = 0
        for rental in self._rentals:
            total_amount += rental.get_charge()
        
        return total_amount
    
    def get_total_frequent_renter_points(self) -> int:

        total_points = 0
        for rental in self._rentals:
            total_points += rental.get_frequent_renter_points()
        
        return total_points