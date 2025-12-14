# Fynd AI Intern – Take Home Assessment

**Name:** Harsh Maurya  
**Role Applied For:** AI Intern  

---

## 📌 Overview

This repository contains my submission for the **Fynd AI Intern – Take Home Assessment**, consisting of two tasks:

- **Task 1:** Prompt engineering–based rating prediction for Yelp reviews.
- **Task 2:** A fully deployed AI-powered feedback system with separate User and Admin dashboards.

The project focuses on prompt design, evaluation, AI system behavior, and practical deployment.

---

## 🧠 Task 1 – Rating Prediction via Prompting

### Description
Task 1 explores how different prompt designs affect a Large Language Model’s (LLM) ability to classify Yelp reviews into star ratings (1–5).  
Three prompt versions were designed and evaluated based on:

- Prediction accuracy
- JSON validity rate
- Reliability and consistency

### Contents
- **Jupyter Notebook:**  
  `task1_rating_prediction/task1_prompt_experiments.ipynb`

- **Report (PDF):**  
  `reports/Task1_Report.pdf`

The notebook contains all experiments, prompt iterations, evaluation logic, and comparison results.

---

## 🌐 Task 2 – Two-Dashboard AI Feedback System

### User Dashboard (Public-Facing)
Users can:
- Select a star rating
- Write a short review
- Submit feedback and receive an AI-generated response

### Admin Dashboard (Internal-Facing)
The admin dashboard provides:
- A live list of all submissions
- AI-generated summaries
- AI-recommended next actions
- Basic analytics such as average rating and rating distribution

### Shared Data Source
Both dashboards read from and write to a **shared Google Sheet** via a **Google Apps Script web API**, ensuring synchronization despite isolated cloud runtimes.

---

## 🚀 Deployment Links

- **User Dashboard:**  
  _PASTE USER DASHBOARD STREAMLIT URL HERE_

- **Admin Dashboard:**  
  _PASTE ADMIN DASHBOARD STREAMLIT URL HERE_

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Web Framework:** Streamlit  
- **LLM Provider:** OpenRouter (free open-source models)  
- **Data Storage:** Google Sheets via Google Apps Script  
- **Deployment:** Streamlit Community Cloud  

---

## 📁 Repository Structure

task1_rating_prediction/
│ └── task1_prompt_experiments.ipynb
│
task2_dashboards/
│ ├── user_dashboard.py
│ ├── admin_dashboard.py
│ ├── llm_utils.py
│ └── storage.py
│
reports/
│ └── Task1_Report.pdf
│
requirements.txt
README.md


---

## ✅ Notes

- Only free and permitted LLMs were used.
- Both dashboards are fully deployed and publicly accessible.
- The project emphasizes clarity, evaluation, and real-world system constraints.

---

Thank you for reviewing my submission.
