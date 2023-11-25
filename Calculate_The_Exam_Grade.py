while True:
    grade = input("*Enter the exam grade from 0 to 10 to evaluate the result or type 'Exit' to exit: ")
    grade = grade.lower()
    if grade == "exit":
        print("Terminate the Execution")
        break

    grade = int(grade)

    def calculation(grade):
        if grade >= 9 and grade <= 10:
            result = "excellent"
        elif grade >= 7 and grade <= 8:
            result = "outstanding"
        elif grade >= 5 and grade <= 6:
            result = "acceptable"
        elif grade >= 3 and grade <= 4:
            result = "insufficient"
        elif grade >= 0 and grade <= 2:
            result = "deficient"
        else:
            result = "transcription error"

        return result

    print(calculation(grade))