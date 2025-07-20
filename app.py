import streamlit as st

# Title
st.title("Grade Checker")

# Get user name and capitalize
user_name = st.text_input("Please enter your name:")
if user_name:
    name = user_name.capitalize()
    st.write(f"Hello, {name}!")

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

st.write("Enter your scores:")

# Create inputs and display grades
for subject in subjects:
    score = st.number_input(f"{subject} score", min_value=0.0, max_value=100.0, step=0.1, key=subject)
    grade = get_grade(score)
    st.write(f"{subject}: Your grade is **{grade}**")
