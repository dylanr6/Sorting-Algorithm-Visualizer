from algorithms import bubble_sort, selection_sort
import tkinter as tk
import random

root = tk.Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry("800x600")

canvas = tk.Canvas(root, width=780, height=500, bg='white')
canvas.pack(pady=20)

#Function to Plot an Array
def draw_array(array, color_array):
    canvas.delete("all")
    c_width = 780
    c_height = 500
    bar_width = c_width / len(array)
    for i, val in enumerate(array):
        x0 = i * bar_width
        y0 = c_height - val * 4
        x1 = (i + 1) * bar_width
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
    root.update_idletasks()

#Function to Start Sorting using Bubble Sort
def start_bubble_sort():
    color_array = ['blue' for _ in range(len(array))]
    for arr, i, j in bubble_sort(array):
        color_array[i] = 'red'
        color_array[j] = 'red'
        draw_array(arr, color_array)
        color_array[i] = 'blue'
        color_array[j] = 'blue'

#Function to Start Sorting using Selection Sort
def start_selection_sort():
    color_array = ['blue' for _ in range(len(array))]
    for arr, i, j in selection_sort(array):
        color_array[i] = 'red'
        color_array[j] = 'red'
        draw_array(arr, color_array)
        color_array[i] = 'blue'
        color_array[j] = 'blue'

#Randomized Array
array = [random.randint(10, 100) for _ in range(50)]
saved_array = array.copy()

def randomize_array():
    global array, color_array
    array = [random.randint(10, 100) for _ in range(50)]  # Generate new random values
    color_array = ['blue' for _ in range(len(array))]      # Reset colors
    draw_array(array, color_array)                         # Replot the array
    saved_array = array.copy()

#Function to Unsort Array
def unsort_array():
    global array, saved_array
    array = saved_array.copy()
    color_array = ['blue' for _ in range(len(saved_array))] 
    draw_array(saved_array, color_array)

#Create a Frame for the Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

#'Randomize Array' Button
randomize_button = tk.Button(button_frame, text="Randomize Array", command=randomize_array)
randomize_button.pack(side=tk.LEFT, padx=5)

#'Start Bubble Sort' Button
start_bubble_button = tk.Button(button_frame, text="Start Bubble Sort", command=start_bubble_sort)
start_bubble_button.pack(side=tk.LEFT, padx=5)

#'Start Selection Sort' Button
start_selection_button = tk.Button(button_frame, text="Start Selection Sort", command=start_selection_sort)
start_selection_button.pack(side=tk.LEFT, padx=5)

#'Unsort' Button
unsort_button = tk.Button(button_frame, text="Unsort", command=unsort_array)
unsort_button.pack(side=tk.LEFT, padx=5)

color_array = ['blue' for _ in range(len(array))]
draw_array(array, color_array)

root.mainloop()