import random

# Questions marked as done (checkmarked)
questions_done = [
    # Intermediate Statistics Problems
    "Lista 1 - #01", "Lista 1 - #02", "Lista 1 - #03", "Lista 1 - #04", "Lista 1 - #05",
    "Lista 2 - #01", "Lista 2 - #02", "Lista 2 - #03", "Lista 2 - #04", "Lista 2 - #05",
    "Lista 2 - #06", "Lista 2 - #07", "Lista 2 - #08",
    "Lista 2.5 - #01", "Lista 2.5 - #02", "Lista 2.5 - #03", "Lista 2.5 - #04", "Lista 2.5 - #05",
    "Lista 2.5 - #06", "Lista 2.5 - #07", "Lista 2.5 - #08", "Lista 2.5 - #09",
    "Lista 3 - #01", "Lista 3 - #02", "Lista 3 - #03", "Lista 3 - #04", "Lista 3 - #05",
    "Lista 3 - #06", "Lista 3 - #07", "Lista 3 - #08", "Lista 3 - #09", "Lista 3 - #10",
    "Lista 3 - #11", "Lista 3 - #12", "Lista 3 - #13",

    # Lists of other courses
    "HW 1 - #01", "HW 1 - #02", "HW 1 - #03", "HW 1 - #04", "HW 1 - #05",
    "HW 1 - #06", "HW 1 - #07", "HW 1 - #08", "HW 1 - #09", "HW 1 - #10",
    "HW 2 - #01", "HW 2 - #02", "HW 2 - #03", "HW 2 - #04", "HW 2 - #05",
    "HW 3 - #01", "HW 3 - #02", "HW 3 - #03", "HW 3 - #04", "HW 3 - #05",
    "HW 4 - #01", "HW 4 - #02", "HW 4 - #03", "HW 4 - #04", "HW 4 - #05",
    "HW 4 - #06", "HW 4 - #07", "HW 4 - #08", "HW 4 - #09", "HW 4 - #10",
    "HW 4 - #11", "HW 4 - #12", "HW 4 - #13",
    "HW 5 - #01", "HW 5 - #02", "HW 5 - #03", "HW 5 - #04", "HW 5 - #05"
]

# Randomly select 3 questions from the done list
random_questions = random.sample(questions_done, 3)

# Display the selected questions
print("Selected Random Questions:")
for question in random_questions:
    print(question)
