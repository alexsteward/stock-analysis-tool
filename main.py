# main.py

import tkinter as tk
from tkinter import ttk, messagebox
from src.data_fetch import fetch_stock_data
from src.analysis import calculate_moving_average
from src.visualization import plot_stock_data
import pandas as pd

class StockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Market Analysis Tool")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Add a title label
        ttk.Label(root, text="Stock Market Analysis Tool", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Ticker Input
        ttk.Label(root, text="Stock Ticker:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.ticker_entry = ttk.Entry(root)
        self.ticker_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Start Date Input
        ttk.Label(root, text="Start Date (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.start_date_entry = ttk.Entry(root)
        self.start_date_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # End Date Input
        ttk.Label(root, text="End Date (YYYY-MM-DD):").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.end_date_entry = ttk.Entry(root)
        self.end_date_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Moving Average Input
        ttk.Label(root, text="Moving Average Window:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.window_entry = ttk.Entry(root)
        self.window_entry.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        # Save Results Option
        self.save_results_var = tk.BooleanVar()
        ttk.Checkbutton(root, text="Save Results to File", variable=self.save_results_var).grid(row=5, column=0, columnspan=2, pady=5)

        # Submit Button
        self.submit_button = ttk.Button(root, text="Analyze", command=self.analyze_stock)
        self.submit_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Status Label
        self.status_label = ttk.Label(root, text="", foreground="green")
        self.status_label.grid(row=7, column=0, columnspan=2, pady=5)

    def analyze_stock(self):
        # Get input values
        ticker = self.ticker_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        window = self.window_entry.get()

        if not ticker or not start_date or not end_date or not window:
            messagebox.showerror("Input Error", "All fields must be filled out.")
            return

        try:
            window = int(window)
        except ValueError:
            messagebox.showerror("Input Error", "Moving average window must be an integer.")
            return

        try:
            # Fetch and analyze data
            data = fetch_stock_data(ticker, start_date, end_date)
            moving_avg = calculate_moving_average(data, window=window)
            data['Moving Average'] = moving_avg

            # Save results if selected
            if self.save_results_var.get():
                data.to_csv(f"{ticker}_analysis.csv")
                self.status_label.config(text="Results saved to file.")

            # Plot the results
            plot_stock_data(data, ticker)
            self.status_label.config(text="Analysis complete.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockApp(root)
    root.mainloop()