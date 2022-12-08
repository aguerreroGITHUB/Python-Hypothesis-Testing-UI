from tkinter import *
import math

# Create the root window
root = Tk()
root.title("Z-Test")
# Function to calculate the Z scores
def calculate_z_scores():
    # Get the values from the input fields
    pop_mean = float(pop_mean_field.get())
    sample_mean = float(sample_mean_field.get())
    sample_std_dev = float(sample_std_dev_field.get())
    sample_size = float(sample_size_field.get())

    # Calculate the Z scores
    z = (sample_mean - pop_mean) / (sample_std_dev / math.sqrt(sample_size))

    # Set the output for Z95
    if z < 1.96 and z > -1.96:
        z95_output_field.config(text="Can't reject null", fg='red')
    else:
        z95_output_field.config(text="Reject null", fg='green')

    # Set the output for Z99
    if z < 2.575 and z > -2.575:
        z99_output_field.config(text="Can't reject null", fg='red')
    else:
        z99_output_field.config(text="Reject null", fg='green')

    # Set the output for the calculated Z score
    z_output_field = Label(root, text=str(z))
    z_output_field.grid(row=4, column=1)

# Population mean 
pop_mean_label = Label(root, text="Population Mean:")
pop_mean_label.grid(row=0, column=0)

pop_mean_field = Entry(root)
pop_mean_field.grid(row=0, column=1)

# Sample mean
sample_mean_label = Label(root, text="Sample Mean:")
sample_mean_label.grid(row=1, column=0)

sample_mean_field = Entry(root)
sample_mean_field.grid(row=1, column=1)

# Sample standard deviation 
sample_std_dev_label = Label(root, text="Sample Standard Deviation:")
sample_std_dev_label.grid(row=2, column=0)

sample_std_dev_field = Entry(root)
sample_std_dev_field.grid(row=2, column=1)

# Sample size 
sample_size_label = Label(root, text="Sample Size:")
sample_size_label.grid(row=3, column=0)

sample_size_field = Entry(root)
sample_size_field.grid(row=3, column=1)

# Create a button to calculate the Z scores
calculate_button = Button(root, text="Calculate Z-Scores", command=calculate_z_scores)
calculate_button.grid(row=4, column=0)

# Z95 output 
z95_output_label = Label(root, text="Z95:")
z95_output_label.grid(row=5, column=0)

z95_output_field = Label(root, text="")
z95_output_field.grid(row=5, column=1)

# Z99 output 
z99_output_label = Label(root, text="Z99:")
z99_output_label.grid(row=6, column=0)

z99_output_field = Label(root, text="")
z99_output_field.grid(row=6, column=1)

# Start the main event loop
root.mainloop()

