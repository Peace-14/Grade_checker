user_name = input("Please enter your name: ")
name=user_name.capitalize()
print("Hello",name)

# Function to get grade based on score
def get_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B+"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C+"
    elif score >= 40:
        return "C"
    elif score >= 30:
        return "D+"
    elif score >= 20:
        return "D"
    else:
        return "NG"

# List of subjects
subjects = ["Math", "English", "Science", "History", "Computer"]

# Loop through subjects and get scores
for subject in subjects:
    try:
        score = float(input(f"Enter your score for {subject}: "))
        grade = get_grade(score)
        print(f"{subject}: Your grade is {grade}")
    except ValueError:
        print(f"{subject}: Please enter a number.")