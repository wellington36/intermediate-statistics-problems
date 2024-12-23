import random

N = 6    # weight of lists
Q = 1    # number of problems to select

# All questions marked as done (checkmarked)
all_questions_list = [
    # Intermediate Statistics Problems
    "Lista 4 - #01", "Lista 4 - #02", "Lista 4 - #03", "Lista 4 - #04",
    "Lista 5 - #01", "Lista 5 - #02", "Lista 5 - #03", "Lista 5 - #04"
]

all_questions_HW = [
    # Lists of other courses
    "HW 6 - #01", "HW 6 - #02", "HW 6 - #03", "HW 6 - #04", "HW 6 - #05",
    "HW 6 - #06", "HW 6 - #07",
    "HW 7 - #01", "HW 7 - #02", "HW 7 - #03", "HW 7 - #04", "HW 7 - #05",
    "HW 7 - #06", "HW 7 - #07", "HW 7 - #08", "HW 7 - #09", "HW 7 - #10",
    "HW 7 - #11", "HW 7 - #12", "HW 7 - #13",
    "HW 8 - #01", "HW 8 - #02", "HW 8 - #03", "HW 8 - #04", "HW 8 - #05",
    "HW 8 - #06", "HW 8 - #07",
    "HW 9 - #01", "HW 9 - #02", "HW 9 - #03", "HW 9 - #04", "HW 9 - #05",
    "HW 9 - #06",
    "HW 10 - #01", "HW 10 - #02", "HW 10 - #03", "HW 10 - #04", "HW 10 - #05",
    "HW 10 - #06", "HW 10 - #07", "HW 10 - #08", "HW 10 - #09", "HW 10 - #10",
    "HW 10 - #11", "HW 10 - #12", "HW 10 - #13"
]

# Selection of questions
questions_list = [
    # Intermediate Statistics Problems
    "Lista 4 - #01", "Lista 4 - #02", "Lista 4 - #04",
    "Lista 5 - #01", "Lista 5 - #03", "Lista 5 - #04"
]

questions_HW = [
    # Lists of other courses
    "HW 6 - #01", "HW 6 - #02", "HW 6 - #03", "HW 6 - #04", "HW 6 - #05",
    "HW 6 - #06", "HW 6 - #07",
    "HW 7 - #01", "HW 7 - #02", "HW 7 - #03", "HW 7 - #04", "HW 7 - #05",
    "HW 7 - #06", "HW 7 - #07", "HW 7 - #08", "HW 7 - #11", "HW 7 - #12",
    "HW 7 - #13",
    "HW 8 - #01", "HW 8 - #02", "HW 8 - #03", "HW 8 - #04", "HW 8 - #05",
    "HW 8 - #07",
    "HW 9 - #01", "HW 9 - #02", "HW 9 - #03", "HW 9 - #04", "HW 9 - #05",
    "HW 9 - #06",
    "HW 10 - #01", "HW 10 - #02", "HW 10 - #03", "HW 10 - #04", "HW 10 - #05",
    "HW 10 - #06", "HW 10 - #07", "HW 10 - #08", "HW 10 - #09", "HW 10 - #11",
    "HW 10 - #12", "HW 10 - #13"
]


# Randomly select Q questions from the done problems
random_questions = random.sample(N*questions_list + questions_HW, Q)

while (len(set(random_questions)) != len(random_questions)):
    random_questions = random.sample(N*questions_list + questions_HW, Q)

# Display the selected questions
print("Selected Random Questions:")
for question in random_questions:
    print(question)
