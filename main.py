from algorithms import bubble_sort
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
def start_sort():
    color_array = ['blue' for _ in range(len(array))]
    for arr, i, j in bubble_sort(array):
        color_array[i] = 'red'
        color_array[j] = 'red'
        draw_array(arr, color_array)
        color_array[i] = 'blue'
        color_array[j] = 'blue'

#Random Array
array = [random.randint(10, 100) for _ in range(50)]

#'Start Bubble Sort' Button
start_button = tk.Button(root, text="Start Bubble Sort", command=start_sort)
start_button.pack(pady=10)

color_array = ['blue' for _ in range(len(array))]
draw_array(array, color_array)

root.mainloop()