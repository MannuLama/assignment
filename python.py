# 32100036, Mannu Lama
import pandas as pd
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


class HealthcareApp:
    def __init__(self, master):
        self.master = master
        master.title("32100036, Mannu Lama")
        master.geometry("400x300")

        self.data = None

        # Buttons
        tk.Button(master, text="Load Data", command=self.load_data, width=25).pack(pady=5)
        tk.Button(master, text="Process Data", command=self.process_data, width=25).pack(pady=5)
        tk.Button(master, text="Pie Chart (Departments)", command=self.show_pie_chart, width=25).pack(pady=5)
        tk.Button(master, text="Bar Chart (Marital Status)", command=self.show_bar_chart, width=25).pack(pady=5)
        tk.Button(master, text="Dashboard", command=self.show_dashboard, width=25).pack(pady=5)
        tk.Button(master, text="Exit", command=master.quit, width=25).pack(pady=5)

    def load_data(self):
        try:
            self.data = pd.read_csv("nurse_attrition 01 10 2025 (2).csv")
            messagebox.showinfo("Success", "Data loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def process_data(self):
        if self.data is None:
            messagebox.showerror("Error", "Please load data first.")
            return

        summary = {}
        summary['Total Employees'] = int(len(self.data))
        summary['Departments'] = list(self.data['Department'].unique())
        summary['Employees per Department'] = {k: int(v) for k, v in self.data['Department'].value_counts().to_dict().items()}
        summary['Gender Count'] = {k: int(v) for k, v in self.data['Gender'].value_counts().to_dict().items()}
        summary['Age'] = {
            'Min': int(self.data['Age'].min()),
            'Max': int(self.data['Age'].max()),
            'Avg': round(float(self.data['Age'].mean()), 2)
        }
        summary['DistanceFromHome'] = {
            'Min': int(self.data['DistanceFromHome'].min()),
            'Max': int(self.data['DistanceFromHome'].max()),
            'Avg': round(float(self.data['DistanceFromHome'].mean()), 2)
        }
        summary['HourlyRate'] = {
            'Min': round(float(self.data['HourlyRate'].min()), 2),
            'Max': round(float(self.data['HourlyRate'].max()), 2),
            'Avg': round(float(self.data['HourlyRate'].mean()), 2)
        }
        summary['Marital Status %'] = {k: round(float(v), 2) for k, v in (self.data['MaritalStatus'].value_counts(normalize=True)*100).to_dict().items()}
        summary['Avg Work-Life Balance'] = round(float(self.data['WorkLifeBalance'].mean()), 2)
        summary['Total Attrition'] = int(self.data[self.data['Attrition']=="Yes"].shape[0])

        # Nicely format the message
        msg_lines = []
        for k, v in summary.items():
            msg_lines.append(f"{k}: {v}")
        messagebox.showinfo("Summary", "\n".join(msg_lines))

    def show_pie_chart(self):
        if self.data is None:
            messagebox.showerror("Error", "Please load data first.")
            return
        dept_counts = self.data['Department'].value_counts()
        plt.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%')
        plt.title("Employees per Department")
        plt.show()

    def show_bar_chart(self):
        if self.data is None:
            messagebox.showerror("Error", "Please load data first.")
            return
        marital_counts = self.data['MaritalStatus'].value_counts()
        plt.bar(marital_counts.index, marital_counts.values)
        plt.title("Employees by Marital Status")
        plt.xlabel("Marital Status")
        plt.ylabel("Count")
        plt.show()

    def show_dashboard(self):
        if self.data is None:
            messagebox.showerror("Error", "Please load data first.")
            return

        fig, axs = plt.subplots(1, 2, figsize=(10, 5))

        # Attrition Pie
        attr_counts = self.data['Attrition'].value_counts()
        axs[0].pie(attr_counts, labels=attr_counts.index, autopct='%1.1f%%')
        axs[0].set_title("Attrition")

        # Department Bar
        dept_counts = self.data['Department'].value_counts()
        axs[1].bar(dept_counts.index, dept_counts.values)
        axs[1].set_title("Employees per Department")

        plt.suptitle("Dashboard Overview")
        plt.show()


if __name__ == "__main__":
    root = tk.Tk()
    app = HealthcareApp(root)
    root.mainloop()
