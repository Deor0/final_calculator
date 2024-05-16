import tkinter as tk
from tkinter import messagebox

weightage_participation = 0.05
weightage_coding_practice = 0.05
weightage_labs = 0.10
weightage_project = 0.10
weightage_coding_exam = 0.15
weightage_midterm = 0.15
weightage_final = 0.25

def calculate_needed_final_grade():
    try:
        participation = float(entry_participation.get())
        coding_practice = float(entry_coding_practice.get())
        labs = float(entry_labs.get())
        project = float(entry_project.get())
        coding_exam = float(entry_coding_exam.get())
        mid1 = float(entry_mid1.get())
        mid2 = float(entry_mid2.get())
        desired_grade = float(entry_desired_grade.get())
        
        current_weighted_sum = (participation * weightage_participation +
                                coding_practice * weightage_coding_practice +
                                labs * weightage_labs +
                                project * weightage_project +
                                coding_exam * weightage_coding_exam +
                                mid1 * weightage_midterm +
                                mid2 * weightage_midterm)

        needed_final = (desired_grade - current_weighted_sum) / weightage_final

        if needed_final > mid2 or needed_final > mid1:
            if mid1 < mid2:
                needed_final = (desired_grade - (participation * weightage_participation +
                       coding_practice * weightage_coding_practice +
                       labs * weightage_labs +
                       project * weightage_project +
                       coding_exam * weightage_coding_exam +
                       mid2 * weightage_midterm)) / (weightage_midterm + weightage_final)
            else:
                needed_final = (desired_grade - (participation * weightage_participation +
                       coding_practice * weightage_coding_practice +
                       labs * weightage_labs +
                       project * weightage_project +
                       coding_exam * weightage_coding_exam +
                       mid1 * weightage_midterm)) / (weightage_midterm + weightage_final)

        messagebox.showinfo("Needed Final Grade", f"You need {needed_final:.2f} to get {desired_grade}.")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

def calculate_final_marks():
    try:
        participation = float(entry_participation.get())
        coding_practice = float(entry_coding_practice.get())
        labs = float(entry_labs.get())
        project = float(entry_project.get())
        coding_exam = float(entry_coding_exam.get())
        mid1 = float(entry_mid1.get())
        mid2 = float(entry_mid2.get())
        final = float(entry_final.get())
        

        if final > mid1 and final > mid2:
            if mid1 < mid2:
                mid1 = final
            else:
                mid2 = final

        final_marks = (participation * weightage_participation +
                       coding_practice * weightage_coding_practice +
                       labs * weightage_labs +
                       project * weightage_project +
                       coding_exam * weightage_coding_exam +
                       mid1 * weightage_midterm +
                       mid2 * weightage_midterm +
                       final * weightage_final)

        messagebox.showinfo("Final Marks", f"Your final marks are: {final_marks:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

root = tk.Tk()
root.title("CSC 202 GRADE CALCULATOR")

labels = [
    "Participation",
    "Coding Practice",
    "Labs",
    "Project",
    "Coding Exam",
    "MidTerm 1",
    "MidTerm 2",
    "Final",
    "Desired Final Grade"
]

entries = []

for label_text in labels:
    label = tk.Label(root, text=label_text)
    label.pack()
    entry = tk.Entry(root)
    entry.pack()
    entries.append(entry)

(entry_participation, entry_coding_practice, entry_labs, entry_project,
 entry_coding_exam, entry_mid1, entry_mid2, entry_final, entry_desired_grade) = entries

calculate_final_button = tk.Button(root, text= "Calculate Final Marks", command=calculate_final_marks)
calculate_final_button.pack()

calculate_needed_final_button = tk.Button(root, text= "Calculate Needed Final Grade", command=calculate_needed_final_grade)
calculate_needed_final_button.pack()

root.geometry("500x500")
root.mainloop()
