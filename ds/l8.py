import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_statistics(data):
 average_score = np.mean(data['Score'])
 max_score = np.max(data['Score'])
 min_score = np.min(data['Score'])
 num_students = len(data)
 return average_score, max_score, min_score, num_students

def create_visualizations(data):
 plt.figure(figsize=(8, 6))
 plt.hist(data['Score'], bins=10, edgecolor='black')
 plt.xlabel('Score')
 plt.ylabel('Frequency')
 plt.title('Exam Score Distribution')
 plt.show()
 
 top_students = data[data['Score'] >= 90]
 plt.figure(figsize=(8, 6))
 plt.bar(top_students['Name'], top_students['Score'], color='green')
 plt.xlabel('Student Name')
 plt.ylabel('Score')
 plt.title('Top-performing Students')
 plt.xticks(rotation=45)
 plt.show()

def main():
 exam_data=pd.read_csv("Exam scores.csv")
 avg_score, max_score, min_score, num_students = calculate_statistics(exam_data)
 print("Average Score:", avg_score)
 print("Maximum Score:", max_score)
 print("Minimum Score:", min_score)
 print("Number of Students:", num_students)

 create_visualizations(exam_data)
if __name__== "__main__":
 main()