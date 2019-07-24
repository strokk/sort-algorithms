# GMIT - Computational Thinking with Algorithms - Project 2019


# Benchmarking Sorting Algorithms 

## Author: Guilherme G. C. Paes 


### Project Description

For this project I wrote a Python application which was used to benchmark five different sorting algorithms. I also wrote a report which introduces the algorithms, and discusses the results of the benchmarking process. 
The five sorting algorithms which were implemented, benchmarked and discussed in this project were chosen according to the following criteria: 

Number|Criteria
-----|-----------
**1**|A simple comparison-based sort (Bubble Sort, Selection Sort or Insertion Sort) 
**2**|An efficient comparison-based sort (Merge Sort, Quicksort or Heap Sort) 
**3**|A non-comparison sort (Counting Sort, Bucket Sort or Radix Sort) 
**4**|Any other 2 sorting algorithm of choice

#### Python Application

This application includes implementations of the five sorting algorithms chosen, along with a main method which will test each of the algorithms in turn.

To benchmark the algorithms, it was used arrays of randomly generated integers with different input sizes n. It was used a variety of different input sizes, e.g. n=10,n=100,n=500,…,n=10,000 etc. to test the effect of the input size on the running time of each algorithm.

The running time (in milliseconds) for each algorithm was measured 10 times, and the average of the 10 runs for each algorithm and each input size n is outputed to the console when the program finishes executing.
 

#### Report

Report structure: 

1. Introduction: Introduced the concept of sorting and sorting algorithms, discussed the relevance of concepts such as complexity (time and space), performance, in-place sorting, stable sorting, comparator functions, comparison-based and non-comparison-based sorts, etc. 

2. Sorting Algorithms: Introduced each of the chosen algorithms in turn, discussed their space and time complexity, and explained how each algorithm works using my own diagrams and different example input instances. 

3. Implementation & Benchmarking: This section describes the process followed when implementing the Python application above, and presents the results of the benchmarking. Discussed how the measured performance of the algorithms differed
