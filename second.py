"""
Author: Gerod Dunn
File name: main.py
purpose: find the wavelength of the photon as it passed through a slit(s).
"""

"""
The purpose of second.py is to graph the distances between peaks (gained from the first graph) and the principle index and the distances between the peaks.
The result of this is a linear graph with a slope equal to that of the wavelength of the photons shot through the slit(s). The results of this graph and statistics
that were computed with Python are seen in the Lab report, showing low standard deviation and variance, it was shown that the data was accurate and precise, with
an average percent error of less than one percent and a systematic error ratio of .78.
"""
import pandas as pd #I use Pandas for any data frame manipulation needed
import numpy as np#I use the Numpy package to make use of the Numpy arrays, whereas other packages make use of them, as well as a polynomial regregression
import matplotlib.pyplot as plt#I use Matplotlib for data visualization
import scipy # I used scipy and statistics for statistical analysis
from scipy import stats# I used scipy and statistics for statistical analysis
import statistics# I used scipy and statistics for statistical analysis

"""
First thing done was to hard code in the significant results from the first file (first graph) for ease of use and for speed
"""
#values were hard coded from other (main) file
y = [-2.3,-1.5,-.75,0,.85,1.6,2.35]# D istances from principle index
x = [-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0]# m values (indexes from principle)

  ###REGRESSION###
"""
Second.py has a function called myfunc, where it returns an output (a y value) based on an x value that is manipulated by a variable named slope and a variable
named intercept. Second.py then creates a first-degree polynomial fit based on the x and y values, and then runs a linear regression, returning the slope, intercept,
r value, confidence value, and standard deviation.
"""

"""
fucntion name: myfunc
function type: technically it's a float type function in terms of c/c++ as is, but dynamic
function parameters: a number x
function use: to generate a line of best fit based on an output (y) based on a single input, as well as two global variables slope and intercept
fucntion description: The function will take a single int or float x, multiply by a global slope value, then add a global y-intercept value then retrun the result
"""
def myfunc(x): #function to return outputs of slope and intercept for best fit line
  return slope * x + intercept
z = np.polynomial.polynomial.polyfit(x, y, 1) #polynomial reagression with order 1
slope, intercept, r, p, std_err = stats.linregress(x, y)#getting the slope, y-intercept, r, confidence level, standard deviation

    # forming the line
"""
Second.py then makes a list called mymodel from mapping x to the function myfunc returning y values. 
"""
mymodel = list(map(myfunc, x))#maps function outputs and puts them in a list to model

  # plot
"""
Second.py then makes the graph with labels based on the model and regression with a title, x, and y-axis, and a legend with error bars,
but again the error bars are too small to be seen.
"""
plt.plot(x, y, 'o',ms = 10) #ideal grean line
plt.plot(x, mymodel,"g--",label='0.7767x +  0.03571 +/-0.0049\nPressumed Ideal Green line')#ploting models
    # plot annotations
plt.title("Finding Wavelength of Green Bulb",loc = 'center') #title of graph
plt.xlabel("Maximum Integer value 'm'") #x-axis label
plt.ylabel("Position (mm)")# y-xasis label
    #error bars
plt.grid(color = 'k', linestyle = '-', linewidth = .5)#designing grid
plt.errorbar(x, y, xerr=0, yerr=std_err, errorevery=1, markeredgewidth=10) #fine tuning of error bars on graph
plt.legend()#show equation and legend on graph
plt.show()#show graph
"""
Second.py then prints the slope, intercept, r-value, confidence value, and standard deviation to the terminal.
"""
print("slope is", slope)#printing slope of best fit to terminal
print("intercept is", intercept)#printing of best fit to terminal
print("variance is", r) #printing variance or r value to terminal
print("Confidence value is: ",p)#printing confidence value to termainal
print("Standard deviation of the line is:", std_err)

"""
The next 4 lines deal with contestants that were given in class and algebraically solving for unknowns.
"""
L=float(500)#constants that were given out in class
d=float(25.4*(14/1000))#constants that were given out in class
real_lmda=(d*slope)/L #expirementally derived lambda based on calculations
lmda_real=((slope*d)*L) #solving for unknowns

"""
The next section of second.py is modular to save time on calculations. The functions return a wavelength list, the percent errors of a list, the average of a list,
the sample standard deviation of a list, the expected errors for a list, and the average error of a list.
"""

"""
fucntion name: lmda
function type: the function returns a list, but dynamic
function parameters: none
function use: returns a list of comparitive lambdas that were computed with sheets/excel
fucntion description: when called, the function will return a list of wavelengths that were computed using sheets/excel
"""
def lmda(): #I had to hack this together with sheets, but it returns a list of comparitive lambdas/wavelengths
  lmda_list=[0.000549402,0.0005492834667,0.0005575808,0.0005561584,0.0005504688,0.0005447792,0.0005415788,0.0005459645333]
  return lmda_list
"""
fucntion name: percent_er
function type: list of floats, but dynamic
function parameters: a float and a list of floats
function use: the function is inteneded to generate percent error for a point based on a given list
fucntion description: the function takes in a number and a list, then creates an empty list. In the for loop, with length of the input list, calculates the error. Then,
                      if the error is negative, it is adjuseted. Finally, errors are added to a list and the list is returned when called.
"""  
def percent_er(num,num_listL): #generating percent error for a list
  percent_errors=[]
  for i in range(len(num_listL)):
    EE = ((num_listL[i]-num)/num)*100
    if EE<0:
      EE=EE*-1 #forcing values to be positive
      percent_errors.append(EE)
    if EE>0:
      percent_errors.append(EE)
  return percent_errors
"""
fucntion name: avgs
function type: float, but dynamic
function parameters: a list numbers
function use: generate the average of a list of numbers
fucntion description: the function takes in a list, sets a variable runsum to 0. The code then starts a for loop of length equal to that of the input list.
                      runsum value is updated to through the list to get the sum of the list. The function returns runsum divided by the length of the list.
"""  
def avgs(lists_here):#returning average of a list
  runsum=0
  for i in range(len(lists_here)):
    runsum=runsum+lists_here[i]
  return runsum/len(lists_here)
"""
fucntion name: stdevS
function type: a list of floats, but dynamic
function parameters: a list of numbers
function use: generate the sample standard deviation of a list of numbers
fucntion description: the function takes in a list of numbers. The function then creates an empty list and creates a variable who's value is set by calling the avgs
                      function on the unput list. The function then starts a for loop of length equal to that of the input list. The for loop generates the sample
                      standard deviation for each point of the imput list. The for loop then appends each sample standard deviation value for each point to the empty
                      list generated at the start of the function call. The function then ends with returning the list of sample standard deviations
"""  
def stdevS(num_list): #generating sample standard deviation for list
  stls=[]
  av=avgs(num_list)
  for i in range(len(num_list)):
    s=(((num_list[i]-av)**2)/(len(num_list)-1))**.5
    stls.append(s)
  return stls
"""
fucntion name: dsig
function type: a list of floats, but dynamic
function parameters: a list of floats
function use: generate the expected errors for a list
fucntion description: The function takes in a list of numbers, sets the lenzing factor to .001, creates an empty list and sets a variable equal to 0 for summing.
                      The function then starts a for loop of range equal to that of the input list. The math that was used to derive the algorithm for calculating
                      the expected errors was covered in class, but it's where the partial derivitive of a function is is taken of the variable that is being measured
                      directly. In class we called this "smear". The for loop generates the systematic error for a element in the input list, then appends it to the
                      empty list created at the start of the function. The function returns a list of systematic error for each element in the list.
"""
def dsig(lists_coming): #generating expected errors for a list
  lenzing=.001 # value given in class, but it comes from the tolerance of the equipment used in the expirement.
  d_elems=[]
  intdex=0
  for i in range(len(lists_coming)): #the exponents used were derived in class, but they make use of differential equations and implicit differentiation to fidn the
                                      # "smear" or error in measurement of a varaible
    intdex=(((lists_coming[i]*.001)**2)**.5)
    d_elems.append(intdex)
  return d_elems
"""
fucntion name: vars
function type: a list of numbers, but dynamic
function parameters: a list of numbers
function use: the function is meant to calculate the average errors of a list, though not directly, it works with another function for this purpose in the main()
              function
fucntion description: The function takes in a list of numbers. The function then starts a for loop of length equal to that of the imput list. The for loop then
                      changes the value at each index of the input list, squaring each value at each index. The function returns the squared result. This is not
                      meant to directly compute the average errors of a list, but is meant to work in conjunction with another function in the list.
"""  
def vares(listings): #generating average errors
  for i in range(len(listings)):
    listings[i]=listings[i]**2
  return listings

"""
The next section of second.py is the main function of second.py. Main.py first makes a list of comparative lambdas and comparative errors based on the global variables.
From there, python has the average wavelength and the average percent error. Python repeats a similar process for standard deviation and expected error in wavelengths.
Main.py then repeats the whole process for the distance from the principal peak. Python then will print the results of the calculations and the results of a test to
the terminal.
"""

"""
fucntion name: main
function type: None, but dynamic
function parameters: none, it is called at the bottom of the file using the __name__ variable
function use: to bring together all the spegettii code and other user created functions for the final analysis
fucntion description: The function begins by calling a function that returns a list of comparitive lambdas. The function then makes a list of comparitive errors based
                      on given values. The function then finds the average lambda and the average percent error for each lambda. the ssample standard deviation for
                      lambda and the sample standard deviation of errors is calculated. Then the average sample standard deviation of lambda and errors is calculated.
                      Then the expected errors for lambda and the expected error in measuring errors is calculated. The average expected error for wavelengths and
                      errors is calculated. The varince in lambda and errors is calculated. The function then prints a test result to the terminal and the statistical
                      analysis results to the terminal.
"""
def main():
  lamLists=lmda()#made list of comparitive lambdas
  errros=percent_er(real_lmda,lamLists)#made a list of comparitive errors
  
  avL=avgs(lamLists)#average lambda
  av_errros=avgs(errros)#average percent error
  
  stedevesL=stdevS(lamLists)#standard deviation of lambda
  stedevesE=stdevS(errros)#standard deviation of errors
  
  avgstedL=avgs(stedevesL) #average standard deviation
  avgstedE=avgs(stedevesE)
  
  sigL=dsig(lamLists)#exected error in lambda
  sigE=dsig(errros)#expected error in errors
  
  sigsL=avgs(sigL)#average error expected from D
  sigsE=avgs(sigE)
  
  varL=vares(lamLists)#variance in lambda
  varE=vares(errros)#variance in error
  
  varsL=avgs(varL) #average varaince in lambda
  varsE=avgs(varE) #average variance in error
  
  ##  printing out results to terminal
  print("Comparing in main",real_lmda," ",avL)
  print("Average percent error ",av_errros)
  print("Standard deviation of lambda ", avgstedL)
  print("Standard deviation of percent error ", avgstedE)
  print("Sigmda lamda ",sigsL)
  print("Systemetatic error ",avgstedL/sigsL)
  
if __name__ == '__main__':
    main()
