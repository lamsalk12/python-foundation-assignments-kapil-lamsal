# Define a dictionary of five students and their scores
student_scores = {
    "Anisha": 78,
    "Ravi": 55,
    "Maya": 92,
    "Sagar": 61,
    "Nima": 48
}

# 1. Print every student and their score by looping over key-value pairs
print("All students and scores:")
for student, score in student_scores.items():
    # Print each student's name and score
    print(f"  {student}: {score}")

# 2. Create a dictionary of only students who scored at least 60,
#    using a dictionary comprehension
passing_students = {student: score for student, score in student_scores.items() if score >= 60}

# Print the dictionary of passing students
print(f"Passing students (>= 60): {passing_students}")

# 3. Find the student with the highest score using max() with a key function
top_student = max(student_scores, key=student_scores.get)

# Print the top student and their score
print(f"Highest scorer: {top_student} ({student_scores[top_student]})")

# 4. Calculate the average score across all students
average_score = sum(student_scores.values()) / len(student_scores)

# Print the average score formatted to 2 decimal places
print(f"Average score: {average_score:.2f}")
