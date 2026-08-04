from employee import *

def main():
    print(f"Company name: {Employee.company_name}")
    print(f"Employees Before: {Employee.total_employees}")
    
    try :
        e1 = Employee("Ravi Kumar", 101, "Engineering", 60000.00, "ABCED123F")
        print(e1)
    except ValueError as e :
        print("Error: ", e)
    
    try :
        e2 = Employee("Anitha Sharma", 102, "Finance", 75000.00, "ABCED123F")
        print(e2)
    except ValueError as e :
        print("Error: ", e)
             
    print(f"Employees After: {Employee.total_employees}")
    print(f"PF for e1: {e1.calculate_pf()}")
    print(f"After 10% hike: {e1.apply_hike(10)}")
    e1.transfer_department("Data Science")
    print(f"is_valid_salary(9000): {Employee.is_valid_salary(9000)}")
    
    try : 
        e1.salary = 5000
    except ValueError as e :
        print("Blocked: ", e)
        
    try :
        e1.emp_id = 2
    except AttributeError as e:
        print("Blocked: ", e)
        
    print(f"protected: {e1._department}")
    print(f"private: {e1._Employee__pan_number}")
        
    
if __name__ == "__main__":
    main()