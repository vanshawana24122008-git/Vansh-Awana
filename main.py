# STEP 1: Import the tools we need
import pandas as pd
from sklearn.linear_model import LinearRegression

# STEP 2: Create a simple, readable table of student programming data
# Features: Problems Solved, Coding Hours/Week, Know_Data_Structures (1=Yes, 0=No)
# Target: Skill_Score_Out_Of_100
data = {
    'Problems_Solved': 
    'Coding_Hours_Week': 
    'Know_Data_Structures': 
    'Skill_Score_Out_Of_100': [15, 35, 65, 85, 25, 98]
}

# Convert this data into a structured table (DataFrame)
df = pd.DataFrame(data)

print("--- Automated Programming Skill Dataset ---")
print(df)
print("\n-------------------------------------------")

# STEP 3: Separate our inputs (X) from what we want to predict (y)
X = df[['Problems_Solved', 'Coding_Hours_Week', 'Know_Data_Structures']]
y = df['Skill_Score_Out_Of_100']

# STEP 4: Create and train the Machine Learning model
model = LinearRegression()
model.fit(X, y)

print("[Success] The model has learned the skill evaluation patterns!")

# STEP 5: Test the model with a completely new student configuration!
# Let's predict the score of a student who solved 80 problems, codes 10 hours a week, and knows DSA (1)
new_student = [[80, 10, 1]]

predicted_score = model.predict(new_student)

# Clip the score between 0 and 100 just in case the math overshoots
final_score = max(0, min(100, predicted_score[0]))

print(f"\nPredicted Programming Skill Score for this student: {final_score:.2f} / 100")