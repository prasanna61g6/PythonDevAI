class Student:
    
    college_name = "Aditya Institute of Technology"
    total_students = 0
    PASS_MARK = 35
    MAX_SUBJECTS = 5
    
    def __init__(self, name, roll_number, branch) :
        self.name = name
        self._roll_number = roll_number
        self._branch = branch 
        self.__marks = {} 
        Student.total_students += 1
        
    @property
    def roll_number(self) :
        return self._roll_number
    
    @property
    def average(self) :
        if len(self.__marks) == 0 :
            return 0.0
        
        total = sum(self.__marks.values())
        return total / len(self.__marks)
    
    @property
    def grade(self) :
        if(self.average >= 90) : 
            return 'A+'
        elif(self.average  >= 75 and self.average < 90) :
            return 'A'
        elif(self.average >= 60 and self.average < 75) :
            return 'B'
        elif(self.average >= 35 and self.average < 60) :
            return 'C'
        else :
            return 'F'
        
    def add_marks(self, subject, mark) :
        if not isinstance(mark, (int, float)) :
            raise TypeError("Marks must be a number")
        if mark < 0 and mark > 100 :
            raise ValueError("Marks must be between 0 and 100")
        if subject not in self.__marks and len(self.__marks) >= Student.MAX_SUBJECTS:
            raise ValueError("Maximum subjects exceeded")
        self.__marks[subject] = mark 
        
    def get_marks(self) :
        return dict(self.__marks)
    
    def has_passed(self) :
        if len(self.__marks) == 0 :
            return False
        
        for mark in self.__marks.values() :
            if mark > Student.PASS_MARK :
                return True 
            return False 
        
    def change_branch(self, new_branch) :
        old_branch = self._branch
        self._branch = new_branch
        return (f"{self.name} is shifted from {old_branch} to {self._branch}")
        
    @classmethod
    def get_total_students(cls) :
        return Student.total_students
        
    @staticmethod
    def is_valid_mark(mark) :
        if mark >=0 and mark <= 100 :
            return True
            
    def __str__(self) :
        return (f"Student[{self._roll_number}] "
            f"{self.name} | "
            f"{self._branch} | "
            f"Avg: {self.average:.2f} | "
            f"Grade: {self.grade}")
        
    """ Average and grade are never stored in variables, they are always calculated by accessing current marks.
        This design prevents stale data because, if marks changes then average and grades get reflected automatically 
        without anyone explicitly recalculating them"""
        
            