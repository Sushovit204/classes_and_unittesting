import unittest

from student_class import Student

class TestStudent(unittest.TestCase):
    
    def test_get_total_marks(self):

        subject_list = ["maths", "science", "computer"]
        test_stud = Student("test_student", 15, subject_list)

        test_stud.result_dict={"maths":40,
                               "science":45,
                               "computer":50,}
        
        total_marks = test_stud.get_total_marks()

        self.assertEqual(total_marks, 135)

if __name__ == "__main__":
    unittest.main()