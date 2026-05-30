import pandas as pd

# Load dataset
data = pd.read_csv("skills.csv")

# User input
career = input("Enter target career: ")

student_skills = input(
    "Enter your skills separated by commas: "
).split(",")

student_skills = [skill.strip() for skill in student_skills]

# Find selected career
career_data = data[data["Career"] == career]

if career_data.empty:
    print("Career not found!")
else:
    required_skills = career_data.iloc[0]["Skills"].split(",")

    missing_skills = []

    for skill in required_skills:
        if skill.strip() not in student_skills:
            missing_skills.append(skill.strip())

    coverage = (
        (len(required_skills) - len(missing_skills))
        / len(required_skills)
    ) * 100

    print("\nRequired Skills:")
    print(required_skills)

    print("\nMissing Skills:")
    print(missing_skills)

    print(f"\nSkill Coverage: {coverage:.2f}%")