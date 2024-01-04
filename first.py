"""
Author: Gerod Dunn
File name: first.py
purpose: find the peaks of given data within a table and graph the results
"""


"""
The purpose of first.py is to graph the count of photons at each index vs the Position in mm. The results of this graph are used to form the second graph. I use Pandas and CSV to read in and manage data frames from a CSV file. I use the Numpy package to make use of the Numpy arrays, whereas other packages make use of them. I use Matplotlib to graph the data. I use the statistics package for the statistical analysis at the end of the file.
The results of the first graph result in something that looks like a mixed signal, where I make use of the Scipy package to find the peaks.
"""

from numpy import * #I use the Numpy package to make use of the Numpy arrays, whereas other packages make use of them
import pandas as pd #I use Pandas and CSV to read in and manage data frames from a CSV file
import numpy as np#I use the Numpy package to make use of the Numpy arrays, whereas other packages make use of them
import matplotlib #I use Matplotlib for data visualization
import matplotlib.pyplot as plt#I use Matplotlib for data visualization
import scipy # I use the scipy package to gain access to the signal module
from scipy import signal #I use the signal module to gain access to the find_peaks method
from scipy.signal import find_peaks #I use the find peaks method to determine the peaks of the graph from the data
import statistics #I use this to help with the statistical analysis at the end.
import csv#I use Pandas and CSV to read in and manage data frames from a CSV file

"""
The results of the first graph result in something that looks like a mixed signal, where I make use of the Scipy package to find the peaks. I will make note of when
I use this find_peaks method.
"""

### IMPORTING DATA  ###

"""
The first section of first.py deals with reading data from a CSV file into a data frame,
making use of the pandas module and library and organizing the information to be easier to work with.
"""

"""
first.py first creates a list called column_names so that columns would have names. It then opens the CSV file called Single_Photon_Interference.csv and then drops all
columns after the first 2 due to them being empty. First.py then drops all NaN (not a number) entries in the data frame and then creates a new one based on the columns
being deleted and dropping of NaN entries.
"""
column_names = ["Position(mm)", "Counts"] #making column names
df=pd.read_csv('Single_Photon_Interference.csv',index_col=False)#read in file
df = df.drop(df.columns[2:], axis=1)# removed all but the first two columns
df=df.dropna()#drop NaN values from remaining positions 
new_df=df #makes code easier, coded this originally using this

"""
first.py then moves all values in Position(mm) and Counts to an array and type casts them as floats for both Position and Counts.
"""
pos = new_df['Position(mm)'].values #moving Position(mm) values to independent structure
posit=np.array(pos)#moving values to numpy array
position=posit.astype('f')#forcing values to be of float type
cnt=new_df['Counts'].values#moving Counts values to independent structure
cnts=np.array(cnt)#moving values to numpy array
counts=cnts.astype('f')#forcing values to be of float type

### GRAPHING  ###

"""
The second section of first.py deals with graphing the first graph, and finding the peaks and troughs using Matplotlib and the find_peaks method from the signal module
in the Scipy package.
"""

#  First.py sets x-values to the array created from the position values and y-values to the Counts values. 
xpoints=position
ypoints=counts
    #   Peaks -this bit is used to find the 7 significant peaks of the graph, the purpose of the expirement
"""
    The next line of code is the sole reason why I used the Scipy package, signal module, find_peaks method. There are peaks within the data that need to be
    identified. I adjusted the arguments for the find peaks method, allowing me to find and determine the significant peaks of the expirement
"""
"""
Then first.py has peaks as a dictionary, where; after experimentally tuning the function inputs,
returns the peaks of the first graph using the find_peaks method from the signal module in the Scipy package.
"""
peaks = find_peaks(counts, height = 1500, threshold = 1, distance = 1) #getting peaks
height = peaks[1]['peak_heights'] #list containing the height of the peaks
peak_pos = position[peaks[0]]   #list containing the positions of the peaks  
    #   Minimums - this section was used to find the minima of the counts, while not directly needed, having them allowed for a more comprehensive data vizualizatio
"""
first.py then uses the find_peaks method to find the minima (troughs), after some fine-tuning of the function inputs again.
"""
y2=ypoints*-1
minima = find_peaks(y2, threshold = 1, distance = 1) #getting minimums
min_pos = position[minima[0]]   #list containing the positions of the minima
min_height = y2[minima[0]]   #list containing the height of the minima

"""
first.py then makes a line graph of all the plots given and highlights the peaks as read and the minima as gold.
"""
    #   Plotting the main imported data
plt.plot(xpoints, ypoints, color = 'b') #points from expirement are a line graph with the color blue

    #   Plotting the maxima and minima
plt.scatter(peak_pos, height, color = 'r', s = 40, marker = 'D', label = 'maxima') #peaks from data are red dimonds
plt.scatter(min_pos, min_height*-1, color = 'gold', s = 10, marker = 'X', label = 'minima')#minima from graph are yellow x's

### STATISTICAL ANALYSIS ###

"""
The third section of first.py deals with the statistical analysis of the information given.
"""

    #poison standard deviation for values
"""
In this section, first.py calculates the poison standard deviation and the error bars for the graph.
"""

sums=0.0
for i in range(len(position)): #manually calculating the poison standard deviation for values
    sums=sums+position[i]
avpos=sums/len(position)
xsqare=(avpos**.5)/len(position)

xerror=xsqare #basically adjusting name for ease of use
yerror =6.85944579
sigma=0.0
Peak=peaks[0] #pulling inforation from dictionary

for i in range(len(Peak)): #generating error bar values
    temp1=Peak[i]-avpos
    temp2=temp1**2
    temp3=temp2/(len(Peak)**.5)
    sigma=sigma+temp2#x error bars
total=0
"""
It is important to note that since we were instructed to use the standard deviation of the points for the error bars, the error bars are there, but they are
not visible.
This is also due to how well the data was experimentally derived. Error bars exist for both the x and y directions for each point.
"""
plt.errorbar(xpoints, ypoints, xerr=xerror, yerr=yerror, errorevery=1, markeredgewidth=10)#generating error bars for graph
plt.title("Interference Intensity", loc = 'center') #title
plt.xlabel("Position (mm)") #x-axis
plt.ylabel("Counts")#y-axis
plt.legend() #shows the lengend of the final graph
plt.grid() #shows the grid for ease of data visualization 
plt.show() # shows the final graph with legend and significant points (peaks and minima) with grid, and annotations

