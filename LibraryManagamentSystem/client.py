from user import *
from member import *
from librarian import *

def main():
    
    m1 = Member("Siddhi", 6778788567)
    # print(m1.name)
    m1.display_dashboard()
    
    l1 = Librarian("Prasanna", 78897597, 123)
    # print(l1.name)
    l1.display_dashboard()
    # print(m1._user_id)
    
if __name__ == "__main__":
    main()