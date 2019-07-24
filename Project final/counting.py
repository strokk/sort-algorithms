#Counting sort algorithm code

#importing necessary libraries
import numpy as np
import time
import random

  
# --- COUNTING SORT FUNCTION ---	
# code adapted from interviewcake, available at: https://www.interviewcake.com/concept/python3/counting-sort
def countSort(A, k):
    
    # Count the number of times each value appears.
    # counts[0] stores the number of 0's in the input
    # counts[4] stores the number of 4's in the input
    # and so on..
    counts = [0] * (k + 1)
    for item in A:
        counts[item] += 1

    """"Overwrite counts to hold the next index an item with
    a given value goes. So, counts[4] will now store the index
    where the next 4 goes, not the number of 4's the
    list has.""""
    num_items_before = 0
    for i, count in enumerate(counts):
        counts[i] = num_items_before
        num_items_before += count

    # Output list to be filled in
    sorted_list = [None] * len(A)

    # Run through the input list
    for item in A:
        
        # Place the item in the sorted list
        sorted_list[ counts[item] ] = item

        # And, make sure the next item we see with the same value
        # goes after the one we just placed
        counts[item] += 1

    return sorted_list
  

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
	countSort(array100.copy(), 500)

	#log the end time
	end_time = time.time()

	#calculate the elapsed time 
	time_elapsed = (end_time - start_time) * 1000
	results100.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench100 = np.mean(results100)

# --- BENCHMARK SIZE 500 ---
for r in range(nun_runs):
	start_time = time.time()
	countSort(array500.copy(), 500)
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results500.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench500 = np.around(np.mean(results500), 3)

# --- BENCHMARK SIZE 1000 ---
for r in range(nun_runs):
	start_time = time.time()
	countSort(array1000.copy(), 500)
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results1000.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench1000 = np.around(np.mean(results1000), 3)

# --- BENCHMARK SIZE 1500 ---
for r in range(nun_runs):
	start_time = time.time()
	countSort(array1500.copy(), 500)
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results1500.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench1500 = np.around(np.mean(results1500), 3)

# --- BENCHMARK SIZE 2000 ---
for r in range(nun_runs):
	start_time = time.time()
	countSort(array2000.copy(), 500)
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results2000.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench2000 = np.around(np.mean(results2000), 3)

# --- BENCHMARK SIZE 3000 ---
for r in range(nun_runs):
	start_time = time.time()
	countSort(array3000.copy(), 500)
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results3000.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench3000 = np.around(np.mean(results3000), 3)

# --- BENCHMARK SIZE 4000 ---
for r in range(nun_runs):
	start_time = time.time()
	countSort(array4000.copy(), 500)
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results4000.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench4000 = np.around(np.mean(results4000), 3)

# --- BENCHMARK SIZE 6000 ---
for r in range(nun_runs):
	start_time = time.time()
	countSort(array6000.copy(), 500)
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results6000.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench6000 = np.around(np.mean(results6000), 3)

# --- BENCHMARK SIZE 8000 ---
for r in range(nun_runs):
	start_time = time.time()
	countSort(array8000.copy(), 500)
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results8000.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench8000 = np.around(np.mean(results8000), 3)

# --- BENCHMARK SIZE 10000 ---
for r in range(nun_runs):
	start_time = time.time()
	countSort(array10000.copy(), 500)
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results10000.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench10000 = np.around(np.mean(results10000), 3)

# --- BENCHMARK SIZE 12000 ---
for r in range(nun_runs):
	start_time = time.time()
	countSort(array12000.copy(), 500)
	end_time = time.time()
	time_elapsed = (end_time - start_time) * 1000
	results12000.append(time_elapsed)

#Getting the average and rounding to 3 decimals
bench12000 = np.around(np.mean(results12000), 3)