from abc import ABC, abstractmethod

class User(ABC):
    
    _id_count = 0
    _total_users = 0
    
    def __init__(self, name = None, contact_info = None):
        User._id_count += 1
        User._total_users += 1
        self._user_id = f"U_{User._id_count}"
        self._name = name 
        self._contact_info = contact_info
        
    @property
    def user_id(self):
        return self._user_id
    
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @property
    def contact_info(self):
       return self._contact_info
        
    @contact_info.setter
    def contact_info(self, new_contact_info):
        self._contact_info = new_contact_info
        
    @classmethod
    def get_total_users(cls):
        return User._total_users
        
    @abstractmethod
    def display_dashboard():
        pass
    
    @abstractmethod
    def can_borrow_books():
        pass
    

        
        