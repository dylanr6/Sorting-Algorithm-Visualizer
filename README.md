## Sorting Algorithm Visualizer
A GUI that shows bars being sorted in real time, built using Python and Tkinter. 
This visualizer animates some popular sorting algorithms in real-time, displaying comparisons,swaps, and execution time for each algorithm.

#Features
-GUI built with Tkinter
-Real-time animations for each sorting algorithm
-Performance Metrics:
    -Total execution time
    -Number of comparisons
    -Number of swaps
-Adjustable array size
-Re-randomization of the array with the click of a button
-Unsort the array at any time to test multiple algorithms on the same array, and compare results.
-Currently contains 4 implemented algorithms:
 -Bubble Sort
 -Selection Sort
 -Merge Sort
 -Quick Sort
-"Start All Sorts" button which completes all of the available sorting algorithms one after the other, allowing the user to view each unique animation and compare the results for each algorithm using the metrics in the left-sided stats panels.

#How to use
-Choose the array size and click "Randomize Array" (or skip this step if you would like to use the initially generated array)
-Select a sorting algorithm.
-Watch the algorithm animate in real time.
-View a list of live updates for:
    -Time to sort
    -Comparisons
    -Swaps
-Click "Unsort" to revert the array back to its unsorted form, allowing you to retry using the same or a different algorithm.
-Re-size or re-randomize the array whenever you like using the array size slider and the "Randomize Array" button.

#Algorithms Included
Bubble Sort
-Sinmple comparison-based algorithm which repeatedly swaps adjacent elements.

Selection Sort
-Finds the smallest element and swaps it into the correct position.

Merge Sort
-A divide-and-conquer algorithm which uses recursive array merging.

Quick Sort
-An efficient partition-based sorting algorithm.

#What did I use to create the Visualizer?
-Python 3
-Tkinter
-Random module
-Time module

#Author
Dylan Reardon
https://github.com/dylanr6 
