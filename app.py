import streamlit as st
from recommender import recommend_courses

# -------------------- Page Configuration --------------------

st.set_page_config(
    page_title="Course Recommendation Agent",
    page_icon="🎓",
    layout="wide"
)

# -------------------- Title --------------------

st.markdown(
    "<h1 style='text-align:center;'>🎓 Course Recommendation Agent</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h4 style='text-align:center; color:gray;'>Get a personalized learning path based on your profile</h4>",
    unsafe_allow_html=True
)

st.info(
    "Fill in your educational background, current skills and career goal. "
    "Click **Recommend Learning Path** to generate a personalized learning roadmap."
)

st.write("")

# -------------------- Student Profile --------------------

st.subheader("👤 Student Profile")

col1, col2 = st.columns(2)

with col1:

    name = st.text_input("Student Name")

    background = st.selectbox(
        "Educational Background",
        [
            "ECE",
            "CSE",
            "Mechanical",
            "Civil",
            "BCA",
            "BSc",
            "Commerce"
        ]
    )

with col2:

    goal = st.selectbox(
        "Career Goal",
        [
            "AI Engineer",
            "Backend Developer",
            "Full Stack Developer",
            "Data Scientist",
            "Data Analyst"
        ]
    )

    skills = st.multiselect(
        "Current Skills",
        [
            "Python Basics",
            "Java Programming",
            "HTML",
            "CSS",
            "JavaScript",
            "SQL",
            "Data Structures",
            "Machine Learning"
        ]
    )

st.write("")

# -------------------- Recommendation Button --------------------

if st.button("Recommend Learning Path", use_container_width=True):

    if name.strip() == "":

        st.warning("Please enter your name.")

    else:

        st.success(f"Learning path generated successfully for {name}.")

        st.write("")

        # -------------------- Student Summary --------------------

        st.subheader("📋 Student Summary")

        st.markdown(f"**👤 Student Name:** {name}")
        st.markdown(f"**🎓 Educational Background:** {background}")
        st.markdown(f"**🎯 Career Goal:** {goal}")

        if len(skills) == 0:
            st.markdown("**💻 Current Skills:** None")
        else:
            st.markdown(f"**💻 Current Skills:** {', '.join(skills)}")

        st.divider()

        # -------------------- Learning Path --------------------

        st.header("📚 Personalized Learning Path")

        recommended_courses = recommend_courses(goal, skills)

        if len(recommended_courses) == 0:

            st.success("You already have all the required skills for this career path.")

        else:

            step = 1
            total_weeks = 0

            for course in recommended_courses:

                weeks = int(course["duration"].split()[0])
                total_weeks += weeks

                with st.container(border=True):

                    st.subheader(f"Step {step}: {course['course_name']}")

                    st.write(f"**Level:** {course['level']}")
                    st.write(f"**Estimated Duration:** {course['duration']}")

                    st.write("**Why was this course recommended?**")
                    st.info(course["recommendation_reason"])

                    st.write("**Course Description:**")
                    st.write(course["description"])

                    if len(course["prerequisites"]) > 0:

                        st.write("**Prerequisites:**")

                        for prerequisite in course["prerequisites"]:
                            st.write(f"• {prerequisite}")

                    else:

                        st.write("**Prerequisites:** None")

                st.write("")
                step += 1

            # -------------------- Next Steps --------------------

            st.divider()

            st.header("🚀 Next Steps")

            if goal == "AI Engineer":

                st.success(
                    "✔ Complete Python Basics\n\n"
                    "✔ Learn Data Structures\n\n"
                    "✔ Learn Machine Learning\n\n"
                    "✔ Learn Deep Learning\n\n"
                    "✔ Build AI projects."
                )

            elif goal == "Backend Developer":

                st.success(
                    "✔ Learn Java Programming\n\n"
                    "✔ Practice SQL\n\n"
                    "✔ Learn Data Structures\n\n"
                    "✔ Learn Spring Boot\n\n"
                    "✔ Build REST API projects."
                )

            elif goal == "Full Stack Developer":

                st.success(
                    "✔ Learn HTML\n\n"
                    "✔ Learn CSS\n\n"
                    "✔ Learn JavaScript\n\n"
                    "✔ Learn React\n\n"
                    "✔ Build Full Stack projects."
                )

            elif goal == "Data Scientist":

                st.success(
                    "✔ Learn Python Basics\n\n"
                    "✔ Learn SQL\n\n"
                    "✔ Learn Data Structures\n\n"
                    "✔ Learn Machine Learning\n\n"
                    "✔ Practice using real datasets."
                )

            elif goal == "Data Analyst":

                st.success(
                    "✔ Learn Python Basics\n\n"
                    "✔ Learn SQL\n\n"
                    "✔ Learn Data Visualization\n\n"
                    "✔ Build data analysis projects."
                )

            # -------------------- Overall Recommendation --------------------

            st.divider()

            st.header("⭐ Overall Recommendation")

            st.info(
                f"""
Based on your **{background}** background and your goal of becoming a **{goal}**, this learning path is recommended for your current skill level.

📅 **Estimated Time to Complete:** **{total_weeks} Weeks**

Follow the recommended order, complete hands-on projects after each course, and regularly practice your skills to become job-ready.
"""
            )

# -------------------- Footer --------------------

st.divider()

st.caption("Developed by Nayana K | Course Recommendation Agent | Python + Streamlit")