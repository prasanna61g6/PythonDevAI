from user import *

class Member(User):
    
    MAX_BORROW_LIMIT = 5
    
    def __init__(self, name = None, contact_info = None):
        super().__init__(name, contact_info)
        self._borrowed_books_count = 0
        
    def display_dashboard(self):
        print("---Member Dashboard---")
        print(f"Name : {self._name}")
        print(f"Books Borrowed : {self._borrowed_books_count}")
        
    def can_borrow_books(self):
        return self._borrowed_books_count < Member.MAX_BORROW_LIMIT
        
    def increment_borrow_count(self):
        self._borrowed_books_count += 1
        
    def decrement_borrow_count(self):
        self._borrowed_books_count -= 1
        
    @property
    def borrowed_book_count(self):
        return self._borrowed_books_count