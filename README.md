# 🤖 Automated Programming Skill Level Predictor (HR-Tech ML)

## 📌 Project Context & Overview
Developed as a B.Tech CSAIML Semester 1 project, this repository implements a Supervised Machine Learning regression framework to evaluate a student's programming skill score (out of 100). This simulates backend screening engines used by technical hiring platforms like HackerRank, LeetCode, or corporate HR assessment portals to filter engineering candidates based on objective metrics.

## 💻 Software Stack
**Language Stack:** Python 3
**Algorithmic Library:** Scikit-learn
**Data Engineering Blocks:** Pandas

## 🧠 Feature Matrix Architecture
The model calculates competency based on these active engineering vectors:
* `Problems_Solved`: Quantitative count of algorithmic problems solved (Continuous)
* `Coding_Hours_Week`: Time metrics dedicated to regular active programming (Continuous)
* `Know_Data_Structures`: Binary metric (1 if student understands DSA concepts, 0 otherwise)
* **Target Variable:** `Skill_Score_Out_Of_100` (Predicted Competency Output)
