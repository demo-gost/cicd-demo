def predict_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "FAIL"


if __name__ == "__main__":
    student_marks = 78

    grade = predict_grade(student_marks)

    print("Student Marks:", student_marks)
    print("Student Grade:", grade)