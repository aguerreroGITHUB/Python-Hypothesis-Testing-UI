import tkinter as tk
from scipy import stats

# Create the main window
root = tk.Tk()
root.title("A/B Testing Calculator")

# Create the input widgets
sample_size_label = tk.Label(root, text="Sample size:")
sample_size_label.grid(row=0, column=0)

sample_size_entry = tk.Entry(root)
sample_size_entry.grid(row=0, column=1)


group_a_mean_label = tk.Label(root, text="Group A mean:", fg='blue')
group_a_mean_label.grid(row=1, column=0)

group_a_mean_entry = tk.Entry(root)
group_a_mean_entry.grid(row=1, column=1)

group_a_std_label = tk.Label(root, text="Group A standard deviation:", fg='blue')
group_a_std_label.grid(row=2, column=0)

group_a_std_entry = tk.Entry(root)
group_a_std_entry.grid(row=2, column=1)


group_b_mean_label = tk.Label(root, text="Group B mean:", fg='red')
group_b_mean_label.grid(row=3, column=0)

group_b_mean_entry = tk.Entry(root)
group_b_mean_entry.grid(row=3, column=1)

group_b_std_label = tk.Label(root, text="Group B standard deviation:", fg='red')
group_b_std_label.grid(row=4, column=0)

group_b_std_entry = tk.Entry(root)
group_b_std_entry.grid(row=4, column=1)

# Define the function that will be called when the user clicks the "Calculate" button
def calculate():
    # Get the input values
    sample_size = int(sample_size_entry.get())
    group_a_mean = float(group_a_mean_entry.get())
    group_b_mean = float(group_b_mean_entry.get())
    group_a_std = float(group_a_std_entry.get())
    group_b_std = float(group_b_std_entry.get())
    
    # Perform the statistical calculations
    t, p = stats.ttest_ind_from_stats(group_a_mean, group_a_std, sample_size,
                                      group_b_mean, group_b_std, sample_size)
    
    # Display the results to the user
    result_label = tk.Label(root, text=f"p-value: {p:.3f}")
    result_label.grid(row=6, column=0, columnspan=2)
    
    # Announce the test result
    if p < 0.05:
        test_result = tk.Label(root, text=f"Can renect Null Hypothesis", fg='green')
    else:
        test_result = tk.Label(root, text=f"Can't reject Null Hypothesis", fg='red')
    test_result.grid(row=7, column=0, columnspan=2)

# Create the "Calculate" button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=5, column=0, columnspan=2)

# Enter the main event loop for the application
root.mainloop()