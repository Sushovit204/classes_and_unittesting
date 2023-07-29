from student_class import Student

def main():
    subject_list = ['maths', 'science', 'computer']

    stud_1 = Student("Vane", 36, subject_list)
    print(f'--Marks for {stud_1.name}--')
    for item in stud_1.subjects:
        value = int(input(f'Enter the marks of {item}: '))
        stud_1.result_dict[item] = value
    stud_1.get_total_marks()
    print("\n--NEXT STUDENT--\n")

    stud_2 = Student("Hawa", 18, subject_list)
    print(f'--Marks for {stud_2.name}--')
    for item in stud_2.subjects:
        value = int(input(f'Enter the marks of {item}: '))
        stud_2.result_dict[item] = value
    stud_2.get_total_marks()
    print("\n--NEXT STUDENT--\n")

    stud_3 = Student("Ghumante", 7, subject_list)
    print(f'--Marks for {stud_3.name}--')
    for item in stud_3.subjects:
        value = int(input(f'Enter the marks of {item}: '))
        stud_3.result_dict[item] = value
    stud_3.get_total_marks()

if __name__ == "__main__":
    main()