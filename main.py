from algorithms import bubble_sort, selection_sort, merge, merge_sort, quick_sort, partition
import tkinter as tk
from tkinter import font
import random, time

root = tk.Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry("800x600")

canvas = tk.Canvas(root, width=780, height=500, bg='white')
canvas.pack(pady=20)

comparisons = 0
swaps = 0

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


### ***FUNCTIONS FOR SORTING***

#Function to Start Sorting using Bubble Sort
def start_bubble_sort():
    global array
    color_array = ['blue' for _ in range(len(array))]
    start = time.time()
    for arr, i, j, comps, swps in bubble_sort(array):
        last_bubble_comparisons = comps
        last_bubble_swaps = swps
        color_array[i] = 'red'
        color_array[j] = 'red'
        draw_array(arr, color_array)
        color_array[i] = 'blue'
        color_array[j] = 'blue'
    end = time.time()
    update_time("Bubble Sort", end - start)
    update_comparisons("Bubble Sort", last_bubble_comparisons)
    update_swaps("Bubble Sort", last_bubble_swaps)

#Function to Start Sorting using Selection Sort
def start_selection_sort():
    global array
    color_array = ['blue' for _ in range(len(array))]
    start = time.time()
    for arr, i, j, comps, swps in selection_sort(array):
        color_array[i] = 'red'
        color_array[j] = 'red'
        draw_array(arr, color_array)
        color_array[i] = 'blue'
        color_array[j] = 'blue'
    end = time.time()
    update_time("Selection Sort", end - start)
    update_comparisons("Selection Sort", comps)
    update_swaps("Selection Sort", swps)

#Function to Start Sorting using Merge Sort
def start_merge_sort():
    global array
    start = time.time()
    for arr, i, j, comps, swps in merge_sort(array, 0, len(array) - 1):
        last_merge_comparisons = comps
        last_merge_swaps = swps
        color_array = ["blue"] * len(array)
        color_array[i] = "red"
        color_array[j] = "red"
        draw_array(arr, color_array)
    end = time.time()
    update_time("Merge Sort", end - start)
    update_comparisons("Merge Sort", last_merge_comparisons)
    update_swaps("Merge Sort", last_merge_swaps)

#Function to Start Sorting using Quick Sort
def start_quick_sort():
    global array
    start = time.time()
    for arr, i, j, comps, swps in quick_sort(array, 0, len(array) - 1):
        last_quick_comaprisons = comps
        last_quick_swaps = swps
        color_array = ["blue"] * len(array)
        color_array[i] = "red"
        color_array[j] = "red"
        draw_array(arr, color_array)
    end = time.time()
    update_time("Quick Sort", end - start)
    update_comparisons("Quick Sort", last_quick_comaprisons)
    update_swaps("Quick Sort", last_quick_swaps)

#Function to Start Sorting using All Sorting Menus in a Row
def start_all_sorts():
    unsort_array()
    start_bubble_sort()
    unsort_array()
    start_selection_sort()
    unsort_array()
    start_merge_sort()
    unsort_array()
    start_quick_sort()


### ***OTHER FUNCTIONS (ARRAY STATE)***

#Randomized Array
array = [random.randint(10, 100) for _ in range(50)]
saved_array = array.copy()

def randomize_array():
    global array, color_array, saved_array
    size = array_size_slider.get()
    array = [random.randint(10, 100) for _ in range(size)]  # Generate new random values
    color_array = ['blue' for _ in range(len(array))]      # Reset colors
    draw_array(array, color_array)                         # Replot the array
    saved_array = array.copy()

    time_label.config(text=
        "Time to Sort:\n"
        "Bubble Sort - ???\n"
        "Selection Sort - ???\n"
        "Merge Sort - ???\n"
        "Quick Sort - ???"
    )
    comparisons_label.config(text=
        "Comparisons:\n"
        "Bubble Sort - ???\n"
        "Selection Sort - ???\n"
        "Merge Sort - ???\n"
        "Quick Sort - ???"
    )
    swaps_label.config(text=
        "Swaps:\n"
        "Bubble Sort - ???\n"
        "Selection Sort - ???\n"
        "Merge Sort - ???\n"
        "Quick Sort - ???"
    )

#Function to Unsort Array
def unsort_array():
    global array, saved_array
    array = saved_array.copy()
    color_array = ['blue' for _ in range(len(saved_array))] 
    draw_array(saved_array, color_array)


### ***STATS FUNCTIONS***

#Function to update time stats
def update_time(algorith_name, time_taken):
    current = time_label.cget("text").split("\n")
    new_lines =[]

    for line in current:
        if line.startswith(algorith_name):
            new_lines.append(f"{algorith_name} - {time_taken:.2f} sec")
        else:
            new_lines.append(line)
    
    time_label.config(text="\n".join(new_lines))

def update_comparisons(algorith_name, comparisons):
    current = comparisons_label.cget("text").split("\n")
    new_lines = []
    
    for line in current:
        if line.startswith(algorith_name):
            new_lines.append(f"{algorith_name} - {comparisons}")
        else:
            new_lines.append(line)
    
    comparisons_label.config(text="\n".join(new_lines))

def update_swaps(algorith_name, swaps):
    current = swaps_label.cget("text").split("\n")
    new_lines = []
    
    for line in current:
        if line.startswith(algorith_name):
            new_lines.append(f"{algorith_name} - {swaps}")
        else:
            new_lines.append(line)
    
    swaps_label.config(text="\n".join(new_lines))

### ***UI FRAMES/BUTTONS***

#Create a Frame for the Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

#Create a Slider for the Array Size
array_size_slider = tk.Scale(root, from_=10, to=100, orient=tk.HORIZONTAL, label="Array Size", length=300)
array_size_slider.set(50)
array_size_slider.pack(pady=10)

#Font for Titles
title_font = font.Font(family="Arial", size=10, weight="bold")

#Create a Frame to show timer stats
time_frame = tk.Frame(root, bd=2, relief="solid", width=170, height=120, padx=10, pady=10)
time_frame.place(x=20, y=10)
time_frame.pack_propagate(False)

time_title = tk.Label(time_frame, text="Time to Sort:", font=title_font)
time_title.pack(anchor="w")

time_label = tk.Label(
    time_frame,
    text="Bubble Sort - ???\nSelection Sort - ???\nMerge Sort - ???\nQuick Sort - ???",
    justify="left",
    font=("Arial", 10)
)
time_label.pack(anchor="w")

#Create a Frame to show Comparisons stats
comparisons_frame = tk.Frame(root, bd=2, relief="solid", width=170, height=120, padx=10, pady=10)
comparisons_frame.place(x=20, y=160)
comparisons_frame.pack_propagate(False)

comparisons_title = tk.Label(comparisons_frame, text="Comparisons:", font=title_font)
comparisons_title.pack(anchor="w")

comparisons_label = tk.Label(
    comparisons_frame,
    text="Bubble Sort - ???\nSelection Sort - ???\nMerge Sort - ???\nQuick Sort - ???",
    justify="left",
    font=("Arial", 10)
)
comparisons_label.pack(anchor="w")

#Create a Frame to show Swaps stats
swaps_frame = tk.Frame(root, bd=2, relief="solid", width=170, height=120, padx=10, pady=10)
swaps_frame.place(x=20, y=310)
swaps_frame.pack_propagate(False)

swaps_title = tk.Label(swaps_frame, text="Swaps:", font=title_font)
swaps_title.pack(anchor="w")

swaps_label = tk.Label(
    swaps_frame,
    text="Bubble Sort - ???\nSelection Sort - ???\nMerge Sort - ???\nQuick Sort - ???",
    justify="left",
    font=("Arial", 10)
)
swaps_label.pack(anchor="w")

#'Start All Sorts' Button
randomize_button = tk.Button(button_frame, text="Start All Sorts", command=start_all_sorts)
randomize_button.pack(side=tk.LEFT, padx=5)

#'Randomize Array' Button
randomize_button = tk.Button(button_frame, text="Randomize Array", command=randomize_array)
randomize_button.pack(side=tk.LEFT, padx=5)

#'Start Bubble Sort' Button
start_bubble_button = tk.Button(button_frame, text="Start Bubble Sort", command=start_bubble_sort)
start_bubble_button.pack(side=tk.LEFT, padx=5)

#'Start Selection Sort' Button
start_selection_button = tk.Button(button_frame, text="Start Selection Sort", command=start_selection_sort)
start_selection_button.pack(side=tk.LEFT, padx=5)

#'Start Merge Sort' Button
start_merge_button = tk.Button(button_frame, text="Start Merge Sort", command=start_merge_sort)
start_merge_button.pack(side=tk.LEFT, padx=5)

#'Start Quick Sort' Button
start_merge_button = tk.Button(button_frame, text="Start Quick Sort", command=start_quick_sort)
start_merge_button.pack(side=tk.LEFT, padx=5)

#'Unsort' Button
unsort_button = tk.Button(button_frame, text="Unsort", command=unsort_array)
unsort_button.pack(side=tk.LEFT, padx=5)


color_array = ['blue' for _ in range(len(array))]
draw_array(array, color_array)

root.mainloop()