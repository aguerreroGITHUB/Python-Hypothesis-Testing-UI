# Import the necessary modules
import tkinter as tk
from scipy import stats

# Create the main window
root = tk.Tk()
root.title("T-Test")

# Create the labels for the input fields
sample1_mean_label = tk.Label(root, text="Sample 1 mean:", fg='blue')
sample1_stdev_label = tk.Label(root, text="Sample 1 stdev:", fg='blue')
sample2_mean_label = tk.Label(root, text="Sample 2 mean:", fg='red')
sample2_stdev_label = tk.Label(root, text="Sample 2 stdev:", fg='red')

# Create the input fields for the two samples and their means and standard deviations
sample1_mean = tk.Entry(root)
sample1_stdev = tk.Entry(root)
sample2_mean = tk.Entry(root)
sample2_stdev = tk.Entry(root)

# Create the function that will be called when the calculate button is clicked
def calculate():
    # Get the input values
    mean1 = float(sample1_mean.get())
    stdev1 = float(sample1_stdev.get())
    mean2 = float(sample2_mean.get())
    stdev2 = float(sample2_stdev.get())

    # Define the sample sizes (we will assume they are the same size for simplicity)
    sample_size = 100

    # Perform the T test using the scipy stats module
    t, p = stats.ttest_ind_from_stats(mean1, stdev1, sample_size, mean2, stdev2, sample_size)

    # Round results
    t_rounded = round(t, 5)
    p_rounded = round(p, 5)

    # Display the results in the output label
    output_label.config(text=f"T-value: {t_rounded}, P-value: {p_rounded}")
    if (p<0.05):
        result_label.config(text=f"Can reject Null", fg='green')
    else:
        result_label.config(text=f"Can't reject null", fg='red')

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)

# Create the output label
output_label = tk.Label(root, text="")

# Create the result label
result_label = tk.Label(root, text="")

# Arrange the widgets using the grid layout
sample1_mean_label.grid(row=0, column=0)
sample1_mean.grid(row=0, column=1)
sample1_stdev_label.grid(row=1, column=0)
sample1_stdev.grid(row=1, column=1)

sample2_mean_label.grid(row=2, column=0)
sample2_mean.grid(row=2, column=1)
sample2_stdev_label.grid(row=3, column=0)
sample2_stdev.grid(row=3, column=1)

calculate_button.grid(row=4, column=0, columnspan=2)
output_label.grid(row=5, column=0, columnspan=2)
result_label.grid(row=6, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
