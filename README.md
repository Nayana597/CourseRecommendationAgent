# 🎓 Course Recommendation Agent

## 📌 Project Overview

The Course Recommendation Agent is a Streamlit-based web application that recommends a personalized learning path for students based on their educational background, current skills, and career goals.

The application analyzes the student's profile and generates an ordered list of recommended courses along with recommendation reasons, prerequisites, estimated duration, and career guidance.

---

## ✨ Features

- 👤 Student Profile Input
- 🎯 Career Goal Selection
- 💻 Current Skills Selection
- 📚 Personalized Learning Path
- ✅ Recommendation Based on Career Goal
- 📖 Course Description
- 💡 Recommendation Reason
- ⏳ Estimated Course Duration
- 🔗 Prerequisite Display
- 🚀 Next Steps Guidance
- ⭐ Overall Recommendation

---

## 🛠️ Technologies Used

- Python
- Streamlit
- JSON

---

## 📂 Project Structure

```
CourseRecommendationAgent/
│
├── app.py
├── recommender.py
├── courses.json
├── student_profiles.json
├── requirements.txt
└── README.md
```

---

## 📖 How It Works

1. Enter the student name.
2. Select educational background.
3. Choose career goal.
4. Select current skills.
5. Click **Recommend Learning Path**.
6. The application analyzes the profile and recommends suitable courses in the correct learning order.
7. It also provides:
   - Recommendation reason
   - Course description
   - Estimated duration
   - Prerequisites
   - Next steps
   - Overall recommendation

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/CourseRecommendationAgent.git
```

Move into the project folder:

```bash
cd CourseRecommendationAgent
```

Install the required package:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

---

## 📸 Sample Output

The application displays:

- Student Summary
- Personalized Learning Path
- Course Recommendation Reason
- Course Description
- Prerequisites
- Estimated Duration
- Next Steps
- Overall Recommendation

---

## 📁 Sample Data

The project contains:

- **courses.json** – Course catalogue with descriptions, prerequisites, durations, and recommendation reasons.
- **student_profiles.json** – Sample student profiles for testing.

---

## 🔮 Future Enhancements

- AI-based recommendations using Gemini API
- User authentication
- Database integration
- Course completion tracking
- Resume-based course recommendation
- Progress dashboard

---

## 👩‍💻 Author

**Nayana K**

Electronics and Communication Engineering Graduate

Interested in Software Development, Java, Python, and AI Applications.

---

## 📄 License

This project is created for educational and learning purposes.