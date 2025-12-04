from algorithms import bubble_sort, selection_sort, merge, merge_sort, quick_sort, partition
import tkinter as tk
import random, time

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
    global array
    color_array = ['blue' for _ in range(len(array))]
    start = time.time()
    for arr, i, j in bubble_sort(array):
        color_array[i] = 'red'
        color_array[j] = 'red'
        draw_array(arr, color_array)
        color_array[i] = 'blue'
        color_array[j] = 'blue'
    end = time.time()

    update_stats("Bubble Sort", end - start)

#Function to Start Sorting using Selection Sort
def start_selection_sort():
    global array
    color_array = ['blue' for _ in range(len(array))]
    start = time.time()
    for arr, i, j in selection_sort(array):
        color_array[i] = 'red'
        color_array[j] = 'red'
        draw_array(arr, color_array)
        color_array[i] = 'blue'
        color_array[j] = 'blue'
    end = time.time()

    update_stats("Selection Sort", end - start)

#Function to Start Sorting using Merge Sort
def start_merge_sort():
    global array
    start = time.time()
    for arr, i, j in merge_sort(array, 0, len(array) - 1):
        color_array = ["blue"] * len(array)
        color_array[i] = "red"
        color_array[j] = "red"
        draw_array(arr, color_array)
    end = time.time()

    update_stats("Merge Sort", end - start)

#Function to Start Sorting using Quick Sort
def start_quick_sort():
    global array
    start = time.time()
    for arr, i, j in quick_sort(array, 0, len(array) - 1):
        color_array = ["blue"] * len(array)
        color_array[i] = "red"
        color_array[j] = "red"
        draw_array(arr, color_array)
    end = time.time()

    update_stats("Quick Sort", end - start)

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

    stats_label.config(text=
        "Time to Sort:\n"
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

#Function to update time stats
def update_stats(algorith_name, time_taken):
    current = stats_label.cget("text").split("\n")
    new_lines =[]

    for line in current:
        if line.startswith(algorith_name):
            new_lines.append(f"{algorith_name} - {time_taken:.2f} sec")
        else:
            new_lines.append(line)
    
    stats_label.config(text="\n".join(new_lines))

#Create a Frame for the Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

#Create a Slider for the Array Size
array_size_slider = tk.Scale(root, from_=10, to=100, orient=tk.HORIZONTAL, label="Array Size", length=300)
array_size_slider.set(50)
array_size_slider.pack(pady=10)

#Create a Frame to show timer stats
stats_frame = tk.Frame(root, bd=2, relief="solid", padx=10, pady=10)
stats_frame.place(x=20, y=10)

stats_label = tk.Label(
    stats_frame,
    text="Time to Sort:\nBubble Sort - ???\nSelection Sort - ???\nMerge Sort - ???\nQuick Sort - ???",
    justify="left",
    font=("Arial", 10)
)
stats_label.pack()

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