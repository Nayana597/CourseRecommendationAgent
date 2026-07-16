import json


# Load all courses from JSON
def load_courses():

    with open("courses.json", "r") as file:

        courses = json.load(file)

    return courses


# Recommend courses
def recommend_courses(goal, skills):

    courses = load_courses()

    recommended_courses = []

    # Store current skills
    known_skills = skills.copy()

    # Sort courses by learning order
    courses.sort(key=lambda course: course["order"])

    for course in courses:

        # Check career goal
        if goal not in course["career_goals"]:
            continue

        # Skip if already known
        if course["course_name"] in known_skills:
            continue

        # Check prerequisites
        prerequisites_completed = True

        for prerequisite in course["prerequisites"]:

            if prerequisite not in known_skills:
                prerequisites_completed = False
                break

        # Recommend only if prerequisites are completed
        if prerequisites_completed:

            recommended_courses.append(course)

            # Assume student completes this course
            known_skills.append(course["course_name"])

    return recommended_courses