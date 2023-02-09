# Sorting-Visualizer
Insertion, Selection, Merge, and Bubble Sort Visualized using the PyGame library. The game has a menu to choose between each of the four sorting algorithms included, and will have additions in the form of a slider for speed and potentially more sorting algorithms.

Visualizing these popular sorting algorithms helps deeply with understanding the topics at the beginning. Being able to watch how the numbers interact is a huge help for beginners starting to weave their way through Data Structures and Algorithms.

## Merge Sort
Merge sort is a recursive algorithm that relies on splitting the array until each array only has one item, and then they are brought back together. The total time is O(nlogn) at worst case.
### Pseudocode for Merge Sort
```
for (number in array) {
	L = left half of array
	R = right half of array
	
	mergeSort(L)
	mergeSort(R)
	
	while (L and R both have not reached their end) {
		if (L's next number is less than R's) { append L's next number to array }
		else { append R's next number to array }
	}
	while (L has not reached its end) {
		add L's elements to the array until L has reached its end
	}
	while (R has not reached its end) {
		add R's elements to the array until R has reached its end
	}
}
```
![Merge sort](https://github.com/pw42020/Sorting-Visualizer/blob/main/gifs/MergeSort_AdobeExpress.gif)

## Insertion Sort
Insertion sort is the most basic sorting algorithm on the list. It looks at each item in the array and sends it to its respective place in the array. For example, in an array of 2,1,7,1,5:

- 2 stays in place (2,1,7,1,5)
- 1 moves to first place (1,2,7,1,5)
- 7 stays in place (1,2,7,1,5)
- 1 moves to first place (1,1,2,7,5)
- 5 moves to fourth place (1,1,2,5,7)
- Algorithm is complete

At its worst, Insertion sort is O(n^2). However, at its best (if the array is already sorted), insertion sort is the fastest sorting algorithm, taking O(n) to complete.

### Pseudocode for Insertion Sort
```
for (num1 in array) {
	if (num1 is not first item in array) {
		num2 = number before num1 in array
		while (num1 < num2) {
			swap(num1, num2)
			num2 = number before num1's new position in array
		}
	}
}
```
![Insertion sort](https://github.com/pw42020/Sorting-Visualizer/blob/main/gifs/InsertionSort_AdobeExpress.gif)

## Bubble Sort
Bubble sort is another simple sorting algorithm that continues to swap each array element if the element following the control element is less than the control element. Like Insertion sort, Bubble sort's Time Complexity is also O(n^2).

### Pseudocode for Bubble Sort
```
for (num in array) {
	next = number in array after num
	if (next < num) { swap(next, num) }
}
```
![Bubble sort](https://github.com/pw42020/Sorting-Visualizer/blob/main/gifs/BubbleSort_AdobeExpress.gif)

## Selection Sort
Selection sort is the final sorting algorithm so far.  Like Insertion and Bubble sort, Selection sort is also O(n^2). Selection sort continuously finds the minimum element in the array after 0 and swaps the index of position 0 and the minimum element for the rest of the array.

### Pseudocode for Selection Sort
```
for (num in array) {
	i = 1
	minindex = 0
	while (i != length(array) - 1) {
		if (array[i] < array[minindex]) {
			minindex = i
		}
	}
	swap(array[minindex], array[0])
}
```
![Selection sort](https://github.com/pw42020/Sorting-Visualizer/blob/main/gifs/SelectionSort_AdobeExpress.gif)
