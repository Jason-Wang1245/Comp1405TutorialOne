# intiial message
print("Welcome to the grade calculation program.")
# get first grade and weight from user
midtermOneGrade = float(
    input("Please enter the grade of your first midterm(%): "))
midtermOneWeight = float(
    input("Please enter the weight of your first midterm(%): ")) / 100
# get second grade and weight from user
midtermTwoGrade = float(
    input("Please enter the grade of your second midterm(%): "))
midtermTwoWeight = float(
    input("Please enter the weight of your second midterm(%): ")) / 100
# get third grade and weight from user
midtermThreeGrade = float(
    input("Please enter the grade of your third midterm(%): "))
midtermThreeWeight = float(
    input("Please enter the weight of your third midterm(%): ")) / 100
# get final exam grade and weight from user
finalExamGrade = float(
    input("Please enter the grade of your final exam(%): "))
finalExamWeight = float(
    input("Please enter the weight of your final exam(%): ")) / 100

# calculation for the average grade as a percentage
finalGrade = (midtermOneGrade * midtermOneWeight) + (midtermTwoGrade * midtermTwoWeight) + \
    (midtermThreeGrade * midtermThreeWeight) + \
    (finalExamGrade * finalExamWeight)
# output average grade to the user
print(f"Your average grade is {finalGrade}%.")
