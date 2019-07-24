#Bubble sort algorithm code

#importing necessary libraries
import numpy as np
import time
import random

# --- BUBBLE SORT FUNCTION ---
#Code adapted, original code from Joe James available at: https://github.com/joeyajames/Python/blob/master/Sorting%20Algorithms/SortingAlgorithms	
def bubble_sort(A):
	#outer loop variable i, goes from range 0 to the second to last item in the list
	for i in range (0, len(A) - 1):
		done = True
		#inner loop
		for j in range (0, len(A) - i - 1):
			#compare the item with the item on its right, if item on the left is larger than the item on the right then they swap places
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
				done = False
		if done:
			return
			

#creating random arrays
array100 = [random.randint(0, 500) for i in range(100)]
array500 = [random.randint(0, 500) for i in range(500)]
array1000 = [random.randint(0, 500) for i in range(1000)]
array1500 = [random.randint(0, 500) for i in range(1500)]
array2000 = [random.randint(0, 500) for i in range(2000)]
array3000 = [random.randint(0, 500) for i in range(3000)]
array4000 = [random.randint(0, 500) for i in range(4000)]
array6000 = [random.randint(0, 500) for i in range(6000)]
array8000 = [random.randint(0, 500) for i in range(8000)]
array10000 = [random.randint(0, 500) for i in range(10000)]
array12000 = [random.randint(0, 500) for i in range(12000)]

#Stores the results from the benchmarks
nun_runs = 10
results100 = []
results500 = []
results1000 = []
results1500 = []
results2000 = []
results3000 = []
results4000 = []
results6000 = []
results8000 = []
results10000 = []
results12000 = []

# --- BENCHMARK SIZE 100 ---
for r in range(nun_runs):
	#log the start time
	start_time = time.time()

	#Testing the function
	bubble_sort(array100.copy())

	#log the end time
	end_time = time.time()

	#calculate the elapsed time 
	time_elapsed = (end_time - start_time) * 1000
	results100.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench100 = np.around(np.mean(results100), 3)

# --- BENCHMARK SIZE 500 ---
for r in range(nun_runs):
	start_time = time.time()
	bubble_sort(array500.copy())
	end_time = time.time() 
	time_elapsed = (end_time - start_time) * 1000
	results500.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench500 = np.around(np.mean(results500), 3)

# --- BENCHMARK SIZE 1000 ---
for r in range(nun_runs):
	start_time = time.time()
	bubble_sort(array1000.copy())
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results1000.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench1000 = np.around(np.mean(results1000), 3)

# --- BENCHMARK SIZE 1500 ---
for r in range(nun_runs):
	start_time = time.time()
	bubble_sort(array1500.copy())
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results1500.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench1500 = np.around(np.mean(results1500), 3)

# --- BENCHMARK SIZE 2000 ---
for r in range(nun_runs):
	start_time = time.time()
	bubble_sort(array2000.copy())
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results2000.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench2000 = np.around(np.mean(results2000), 3)

# --- BENCHMARK SIZE 3000 ---
for r in range(nun_runs):
	start_time = time.time()
	bubble_sort(array3000.copy())
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results3000.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench3000 = np.around(np.mean(results3000), 3)

# --- BENCHMARK SIZE 4000 ---
for r in range(nun_runs):
	start_time = time.time()
	bubble_sort(array4000.copy())
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results4000.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench4000 = np.around(np.mean(results4000), 3)

# --- BENCHMARK SIZE 6000 ---
for r in range(nun_runs):
	start_time = time.time()
	bubble_sort(array6000.copy())
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results6000.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench6000 = np.around(np.mean(results6000), 3)

# --- BENCHMARK SIZE 8000 ---
for r in range(nun_runs):
	start_time = time.time()
	bubble_sort(array8000.copy())
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results8000.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench8000 = np.around(np.mean(results8000), 3)

# --- BENCHMARK SIZE 10000 ---
for r in range(nun_runs):
	start_time = time.time()
	bubble_sort(array10000.copy())
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results10000.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench10000 = np.around(np.mean(results10000), 3)

# --- BENCHMARK SIZE 12000 ---
for r in range(nun_runs):
	start_time = time.time()
	bubble_sort(array12000.copy())
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results12000.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench12000 = np.around(np.mean(results12000), 3)