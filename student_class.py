class Student():

    def __init__(self, name, roll_no, subjects):
        self.name = name
        self.roll_no = roll_no
        self.subjects = subjects
        self.result_dict = {} 

    def get_total_marks(self):
        total_marks = sum(self.result_dict.values())
        print(f"The total marks of {self.name} is {total_marks}")
        return total_marks

