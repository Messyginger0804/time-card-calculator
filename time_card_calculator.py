import tkinter as tk
from tkinter import ttk

def calculate_hours():
    total_hours = 0
    for day in days:
        start_time = start_vars[day].get()
        end_time = end_vars[day].get()
        break_time = break_vars[day].get()
        
        if start_time and end_time:
            start = convert_time_to_hours(start_time)
            end = convert_time_to_hours(end_time)
            hours_worked = end - start - (break_time / 60)  # Convert break time from minutes to hours
            day_totals[day].set(f"{hours_worked:.2f}")
            total_hours += hours_worked

    total_hours_var.set(f"{total_hours:.2f}")

def convert_time_to_hours(time_str):
    time_parts = time_str.split()
    hour_min = time_parts[0].split(':')
    hour = int(hour_min[0])
    if time_parts[1] == 'PM' and hour != 12:
        hour += 12
    elif time_parts[1] == 'AM' and hour == 12:
        hour = 0
    return hour + int(hour_min[1]) / 60  # Convert to decimal

# Create the main window
root = tk.Tk()
root.title("Free Time Card Calculator")

# Variables
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
start_vars = {day: tk.StringVar() for day in days}
end_vars = {day: tk.StringVar() for day in days}
break_vars = {day: tk.IntVar(value=0) for day in days}
day_totals = {day: tk.StringVar(value="0.00") for day in days}
total_hours_var = tk.StringVar(value="0.00")

# Create the UI
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Day").grid(column=0, row=0)
ttk.Label(frame, text="Starting Time").grid(column=1, row=0)
ttk.Label(frame, text="Ending Time").grid(column=2, row=0)
ttk.Label(frame, text="Break Deduction (min)").grid(column=3, row=0)
ttk.Label(frame, text="Total (hrs)").grid(column=4, row=0)

for i, day in enumerate(days):
    ttk.Label(frame, text=day).grid(column=0, row=i + 1)
    ttk.Entry(frame, textvariable=start_vars[day]).grid(column=1, row=i + 1)
    ttk.Entry(frame, textvariable=end_vars[day]).grid(column=2, row=i + 1)
    ttk.Entry(frame, textvariable=break_vars[day]).grid(column=3, row=i + 1)
    ttk.Label(frame, textvariable=day_totals[day]).grid(column=4, row=i + 1)

ttk.Button(frame, text="Calculate", command=calculate_hours).grid(column=0, row=len(days) + 1, columnspan=5)
ttk.Label(frame, text="Total Hours:").grid(column=0, row=len(days) + 2)
ttk.Label(frame, textvariable=total_hours_var).grid(column=1, row=len(days) + 2, columnspan=4)

# Run the application
root.mainloop()
