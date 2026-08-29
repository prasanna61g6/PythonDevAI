from user import *

class Librarian(User):
    
    def __init__(self, name, contact_info, employee_number):
        super().__init__(name, contact_info)
        self._employee_number = employee_number
        
    def display_dashboard(self):
        print("----Librarian Dashboard----")
        print(f"Name : {self._name}")
        print(f"Employee : {self._employee_number}")
        
    def can_borrow_books(self):
        return True
    
    def add_new_book(self):
        pass
    
    def remove_book(self):
        pass 