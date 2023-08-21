import pandas as pd
import tkinter as tk
from tkinter import filedialog

def read_csv(file_name):
    return pd.read_csv(file_name, delimiter=";", decimal=",")


def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select your CSV-file", filetypes=[("CSV files", "*.csv")])
    return file_path

file_name = select_file()

if file_name:
    data = read_csv(file_name)

    print("Processing...")
    
    # ---------------- Data Processing ----------------  

    grouped_data = data.groupby("Tittel")["Beløp"].sum().reset_index()

    income = grouped_data[grouped_data["Beløp"] > 0].sort_values(by="Beløp", ascending=False) 
    expenses = grouped_data[grouped_data["Beløp"] < 0].sort_values(by="Beløp")

    processed_data = pd.concat([income, expenses], ignore_index=True)
    total_income = income["Beløp"].sum()
    total_expenses = expenses["Beløp"].sum()
    net_balance = total_income + total_expenses

    summary = pd.DataFrame({
        "Tittel": ["Total Income", "Total Expenses", "Net Balance"],
        "Beløp": [total_income, total_expenses, net_balance]
    })

    processed_data = pd.concat([processed_data, summary], ignore_index=True)

    output_file_name = "Processed_Bank_Statement.csv"
    processed_data.to_csv(output_file_name, index=False, sep=';')

    print(f"Processed data saved to {output_file_name}")
    print("Completed.")
   
else:
    print("No file deteced.")