import numpy as np

# Creating a 2D numpy array to represent student scores in three subjects
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

# Display the original scores
student_averages = np.mean(scores, axis=1)
print("Average score for each student:", student_averages)

# Average score for each subject
subject_averages = np.mean(scores, axis=0)
print("Average score for each subject:", subject_averages)

#Average score for all students
total_scores = np.sum(scores, axis=1)
top_student_index = np.argmax(total_scores)
print("Student with highest total score (row index):", top_student_index)

# To add a bonus of 5 points to the third subject for all students
scores[:, 2] += 5
print("Updated scores after bonus:\n", scores)
