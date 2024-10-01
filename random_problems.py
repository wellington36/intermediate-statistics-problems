import random

# Questions marked as done (checkmarked)
questions_done = [
    # Intermediate Statistics Problems
    "Lista 1 - #1", "Lista 1 - #2", "Lista 1 - #3", "Lista 1 - #4", "Lista 1 - #5",
    "Lista 2 - #1", "Lista 2 - #2", "Lista 2 - #3", "Lista 2 - #4", "Lista 2 - #5",
    "Lista 2 - #6", "Lista 2 - #7", "Lista 2 - #8",
    "Lista 3 - #1", "Lista 3 - #2", "Lista 3 - #3", "Lista 3 - #4", "Lista 3 - #5",
    "Lista 3 - #6", "Lista 3 - #7", "Lista 3 - #8", "Lista 3 - #9", "Lista 3 - #10",
    "Lista 3 - #11", "Lista 3 - #12", "Lista 3 - #13"

    # Lists of other courses
    "HW 1 - #1", "HW 1 - #2", "HW 1 - #3", "HW 1 - #4", "HW 1 - #5",
    "HW 1 - #6", "HW 1 - #7", "HW 1 - #8", "HW 1 - #9", "HW 1 - #10",
    "HW 2 - #1", "HW 2 - #2", "HW 2 - #3", "HW 2 - #4", "HW 2 - #5",
    "HW 3 - #1", "HW 3 - #2", "HW 3 - #3", "HW 3 - #4", "HW 3 - #5",
    "HW 4 - #1", "HW 4 - #2", "HW 4 - #3", "HW 4 - #4", "HW 4 - #5",
    "HW 4 - #6", "HW 4 - #7", "HW 4 - #8", "HW 4 - #9", "HW 4 - #10",
    "HW 4 - #11", "HW 4 - #12", "HW 4 - #13"
]

# Randomly select 3 questions from the done list
random_questions = random.sample(questions_done, 3)

# Display the selected questions
print("Selected Random Questions:")
for question in random_questions:
    print(question)
