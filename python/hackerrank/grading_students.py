# https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
            continue

        mod = grade % 10
        if mod < 5:
            grade = grade + 5 - mod if 5 - mod < 3 else grade
        else:
            grade = grade + 10 - mod if 10 - mod < 3 else grade

        result.append(grade)
    return result
