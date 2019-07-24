#Guilherme Paes
#Sorting algorithms benchmark program
#In order to run this program properly, you will need to have all the other 5 files regarding the sorting algorithms in the same folder as this


#importing necessary libraries
import matplotlib.pyplot as plt
import pandas as pd


#importing all 5 sorting algorithms files
import insertion
import selection
import bubble
import merge
import counting

#wrapping up the code for benchmarks
insert = insertion.bench100, insertion.bench500, insertion.bench1000, insertion.bench1500, insertion.bench2000, insertion.bench3000, insertion.bench4000, insertion.bench6000, insertion.bench8000, insertion.bench10000, insertion.bench12000
select = selection.bench100, selection.bench500, selection.bench1000, selection.bench1500, selection.bench2000, selection.bench3000, selection.bench4000, selection.bench6000, selection.bench8000, selection.bench10000,  selection.bench12000
bubble = bubble.bench100, bubble.bench500, bubble.bench1000, bubble.bench1500 ,bubble.bench2000, bubble.bench3000, bubble.bench4000, bubble.bench6000, bubble.bench8000, bubble.bench10000, bubble.bench12000
merg = merge.bench100, merge.bench500, merge.bench1000, merge.bench1500, merge.bench2000, merge.bench3000, merge.bench4000, merge.bench6000, merge.bench8000, merge.bench10000, merge.bench12000
count = counting.bench100, counting.bench500, counting.bench1000, counting.bench1500, counting.bench2000, counting.bench3000, counting.bench4000, counting.bench6000, counting.bench8000, counting.bench10000, counting.bench12000

#Creating the dataframe using pandas
df = pd.DataFrame({
        'Insertion Sort': insert, 
        'Selection Sort': select,
        'Bubble Sort': bubble,
        'Merge Sort': merg,
        'Counting Sort': count},
        index = ['100', '500', '1000', '1500', '2000', '3000', '4000', '6000', '8000', '10000', '12000'])

#Giving a name to the index
df.index.name = 'Size'

#Printing the benchmarks
print(df)

#Saving the benchmarks df in a csv file
df.to_csv('sorting_df.csv')

#Plotting a line graph with matplotlib
plt.plot(df)
plt.xlabel('Input size n')
plt.ylabel('Time in milliseconds')
plt.show()
