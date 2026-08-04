class Employee:
    
    company_name = "TechCorp Solutions"
    total_employees = 0
    pf_percentage = 12.0
    MIN_SALARY = 15000
    MAX_SALARY = 500000
    
    def __init__(self, name, emp_id, department, salary, pan_number):
        self.name = name
        self._emp_id = emp_id
        self._department = department
        self._salary = salary
        self.__pan_number = pan_number
        Employee.total_employees += 1
      
    @property    
    def emp_id(self):
        return self._emp_id
    
    @property
    def salary(self):
        return self._salary
        
    @salary.setter
    def salary(self, salary):
        if not isinstance(salary, (int, float)):
            raise TypeError("Salary must be a number")
        elif salary < Employee.MIN_SALARY or salary > Employee.MAX_SALARY :
            raise ValueError(f"Salary must be between {Employee.MIN_SALARY} and {Employee.MAX_SALARY}")
        else :
            self._salary = salary
        
    def apply_hike(self, percent):
        if percent < 0 or percent > 50 :
            raise ValueError("Hike Percentage must be between 0-50")
        else :
            hike = self._salary * (percent / 100)
            self._salary += hike 
        
    def calculate_pf(self):
        return self._salary * (Employee.pf_percentage / 100)
    
    def transfer_department(self, new_dept):
        print(f"{self.name} from {self._department} department has assigned into new department {new_dept}")
        self._department = new_dept
      
    @classmethod    
    def get_total_employees(cls):
        return Employee.total_employees
        
    @staticmethod  
    def is_valid_salary(amount):
        return amount < Employee.MIN_SALARY and amount > Employee.MAX_SALARY
    
    def __str__(self):
        return f"Employee[{self._emp_id}] {self.name} | {self._department} | Rs.{self._salary:,.2f}"
    
    
    """ _department is a protected attribute, in python, protected members is only for convention. They only say
    it is only for inside class but it doesn't either stop accessing it, so protected member can be accessed outside 
    class. But when coming to private attributes(__pan_number), for private members python does name mangling by 
    changing __pan_number to _Employee__pan_number, so accessing through this name will work rather than original name,
    this is meant to discourage accidental access, not to provide true privacy """
        
    
      
    
    
        