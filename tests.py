from model import Book, Rental, Client

def test_statement():
    book1 = Book("Refactoring", Book.REGULAR)
    book2 = Book("Clean Code", Book.NEW_RELEASE)
    
    r1 = Rental(book1, 3)
    r2 = Rental(book2, 5)
    
    c = Client("Fulano")
    c.add_rental(r1)
    c.add_rental(r2)
    
    expected_report = (
        "Rental summary for Fulano\n"
        "- Refactoring: 3.5\n"
        "- Clean Code: 15\n"
        "Total: 18.5\n"
        "Points: 3"
    )
    
    assert c.statement() == expected_report

def test_get_charge():
    book1 = Book("Refactoring", Book.REGULAR)
    book2 = Book("Clean Code", Book.NEW_RELEASE)
    
    r1 = Rental(book1, 3)
    r2 = Rental(book2, 5)
    
    assert r1.get_charge() == 3.5
    assert r2.get_charge() == 15.0

def test_get_frequent_renter_points():
    book1 = Book("Refactoring", Book.REGULAR)
    book2 = Book("Clean Code", Book.NEW_RELEASE)
    
    r1 = Rental(book1, 3)
    r2 = Rental(book2, 5)
    
    assert r1.get_frequent_renter_points() == 1
    assert r2.get_frequent_renter_points() == 2

def test_get_total_frequent_renter_points():
    book1 = Book("Refactoring", Book.REGULAR)
    book2 = Book("Clean Code", Book.NEW_RELEASE)
    
    r1 = Rental(book1, 3)
    r2 = Rental(book2, 5)
    
    c = Client("Fulano")
    c.add_rental(r1)
    c.add_rental(r2)
    
    assert c.get_total_frequent_renter_points() == 3

def test_get_total_charge():
    book1 = Book("Refactoring", Book.REGULAR)
    book2 = Book("Clean Code", Book.NEW_RELEASE)
    
    r1 = Rental(book1, 3)
    r2 = Rental(book2, 5)
    
    c = Client("Fulano")
    c.add_rental(r1)
    c.add_rental(r2)
    
    assert c.get_total_charge() == 18.5