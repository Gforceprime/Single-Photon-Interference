***Important note: For full break down, please see the word Doc tittled Readme in the file"

Disclaimer
***From spring 2020 to fall 2021, UNT implemented a virtual classroom approach, due to the pandemic. During this time, I took Modern Physics Laboratory (PHYS 3030) in spring 2021. Before I continue, I must say I have gained permission from the UNT Department of Physics to use the data that was given to us, my original lab report, and my code.***

Inspiration
One of most major breakthroughs in science in the early 20th century regards proving that a photon could act like a particle. Prior to this experiment, physics was still ruled by a Newtonian view that light is a wave. This experiment showed that light can behave like a particle as when it is filtered through tiny slits, the interference will cause the count for the photons in a region, similar to how a particle behaves.

Purpose of this project
The purpose of the application is to analyze experimentally generated data to demonstrate that light can behave like a particle as well as a wave. The application demonstrates the use of several Python packages to create data visualizations that graph the count (or intensity) of photons at each index vs the position along the back film opposite of a slit(s). Those results will then be processed to graph the distances between peaks (gained from the first graph) and the principal index and the distances between the peaks. The result of this is a linear graph with a slope equal to that of the wavelength of the photons shot through the slit(s).

Contents of this project
This project contains the following:
1.	original data that was experimentally gained in a CSV file (Single_Photon_Interference.csv)
2.	2 Python3 code files
o	first.py 
o	second.py
3.	this readme file
4.	the original lab report submitted.

Usage
How to run the code and what is needed

This section will discuss how to run the code for this project. There are several packages that both rely on to run, as well as there is an outside csv file that is required to run one of them that must be in the same file folder/directory as it. In the following 3 sections, I will discuss what is needed for both to run, then I will discuss the specifics for first.py to be run, and then I will end with discussing what is needed to run second.py.

Both executables
The project contains two executables, first.py and second.py. To run both, you will need to run the code in an environment that can read in csv files and display data visualizations, you will also need to ensure that up-to-date versions of each of the following packages are installed:
1.	Numpy-this is used for the numpy arrays mainly, as other packages are built on top of Numpy.
2.	Pandas-this is used to manage and manipulate data frames by cleaning data and moving data to more easily workable structures as well as reading in files.
3.	Matplotlib-This is mainly used for data visualization by graphing the experimentally gained data.
4.	Statistics-This is used to preform statistical analysis at various points in the lab analysis
5.	Scipy- This was used to sure up some of the statistical analysis in the lab, and was a main stay when programming my other labs.

First.py
In addition to the above, to run first.py, you will need to ensure following:
1.	Ensure that the csv file (Single Photon Interference) is in the same directory/folder and immediately accessible to the code and is a csv file, not a xls file.

Second.py
There are no other specifications to run second.py. The executable is self-contained, notwithstanding the above mentioned required specifications and dependencies.

Intended use of project
This project is meant to display the skill of Gerod as a python programmer. This project is intended to show graphically the results of a single photon interference lab and solve for the wavelength of the photons emitted by a bulb. This project is not meant to be a simulation, as such; to run this project, a csv file will need to be provided with column A having position in mm from the principal peak and column B having the count of photon interaction that occurred at the position.

Limitations of project
This project is limited to Python 3, and this specific experiment. It is not resilient to other physics experiments nor will it be able to properly manage data if the data being given to it is altered beyond updating the data itself. This project may become obsolete and may need to be updated if some of the methods used from the installed packages and modules become outdated.

Packages and techniques used
In this section, I will be discussing the packages and libraries used throughout this project as well as the techniques and outside knowledge that I used in coding this project.

Packages/libraries used
For this project, I used the following Python3 packages/libraries:
•	Numpy-this is used for the numpy arrays mainly, as other packages are built on top of Numpy.
•	Pandas-this is used to manage and manipulate data frames by cleaning data and moving data to more easily workable structures as well as reading in files.
•	Matplotlib-This is mainly used for data visualization by graphing the experimentally gained data.
•	Scipy-This was used for this find_peaks method found in the signals module to find the peaks of the data for the first graph as well as the stats module for some of the statistical analysis of the second.py file.
•	Statistics-This was used to sure up some of the statistical analysis in the lab, and was a main stay when programming my other labs.
csv-this was used to assist in reading in the initial csv file at the start of the project.

Techniques used
For this project, I used the following techniques and outside information to complete this project:
•	Python 3: Used for the power of the language and the plethora of trusted libraries
•	Signal module – The signal module from the Scipy package contains a built in method called find_peaks that allows the user to find the peaks and minima of data when graphed based on user parameters
•	I ran Poisson distribution – partially because that was part of the parameters that we were told in class, but also partially because we needed to find the distribution of instances within a fixed interval of time
•	Ran gaussian Variation – for the statistical analysis at the end of the lab to determine if the experiment was successful or not as well as how accurate and precise the data was.
•	Higher levels of calculus and partial derivatives were used to derive equations to measure what my class called “smear” or the uncertainty in our measurements per instance of measurement.

Code details
In this section, I will be giving a line by line explanation of the code and what it does for both programs. I will be making note of when I use an outside package and why I am using it. I will also be describing the purpose of each of the programs written.

first.py
The purpose of first.py is to graph the count of photons at each index vs the Position in mm. The results of this graph are used to form the second graph. I use Pandas and CSV to read in and manage data frames from a CSV file. I use the Numpy package to make use of the Numpy arrays, whereas other packages make use of them. I use Matplotlib to graph the data. I use the statistics package for the statistical analysis at the end of the file.

The results of the first graph result in something that looks like a mixed signal, where I make use of the Scipy package to find the peaks.

The first section of first.py deals with reading data from a CSV file into a data frame, making use of the pandas module and library and organizing the information to be easier to work with.

First.py first creates a list called column_names so that columns would have names. It then opens the CSV file called Single_Photon_Interference.csv and then drops all columns after the first 2 due to them being empty. First.py then drops all NaN (not a number) entries in the data frame and then creates a new one based on the columns being deleted and dropping of NaN entries.

First.py then moves all values in Position(mm) and Counts to an array and type casts them as floats for both Position and Counts.

The second section of first.py deals with graphing the first graph, and finding the peaks and troughs using Matplotlib and the find_peaks method from the signal module in the Scipy package.

First.py sets x-values to the array created from the position values and y-values to the Counts values. Then first.py has peaks as a dictionary, where; after experimentally tuning the function inputs, returns the peaks of the first graph using the find_peaks method from the signal module in the Scipy package. First.py then uses the find_peaks method to find the minima (troughs), after some fine-tuning of the function inputs again. First.py then makes a line graph of all the plots given and highlights the peaks as read and the minima as gold.

The third section of first.py deals with the statistical analysis of the information given.

In this section, first.py calculates the poison standard deviation and the error bars for the graph. It is important to note that since we were instructed to use the standard deviation of the points for the error bars, the error bars are there, but they are not visible. This is also due to how well the data was experimentally derived. Error bars exist for both the x and y directions for each point.

second.py
The purpose of second.py is to graph the distances between peaks (gained from the first graph) and the principle index and the distances between the peaks. The result of this is a linear graph with a slope equal to that of the wavelength of the photons shot through the slit(s).
The results of this graph and statistics that were computed with Python are seen in the Lab report, showing low standard deviation and variance, it was shown that the data was accurate and precise, with an average percent error of less than one percent and a systematic error ratio of .78.
Second.py has a function called myfunc, where it returns an output (a y value) based on an x value that is manipulated by a variable named slope and a variable named intercept. Second.py then creates a first-degree polynomial fit based on the x and y values, and then runs a linear regression, returning the slope, intercept, r value, confidence value, and standard deviation.
Second.py then makes a list called mymodel from mapping x to the function myfunc returning y values. Second.py then makes the graph with labels based on the model and regression with a title, x, and y-axis, and a legend with error bars, but again the error bars are too small to be seen.
Second.py then prints the slope, intercept, r-value, confidence value, and standard deviation to the terminal. The next 4 lines deal with contestants that were given in class and algebraically solving for unknowns.
The next section of second.py is modular to save time on calculations. The functions return a wavelength list, the percent errors of a list, the average of a list, the sample standard deviation of a list, the expected errors for a list, and the average error of a list.
The next section of second.py is the main function of second.py. Main.py first makes a list of comparative lambdas and comparative errors based on the global variables. From there, python has the average wavelength and the average percent error. Python repeats a similar process for standard deviation and expected error in wavelengths. Main.py then repeats the whole process for the distance from the principal peak. Python then will print the results of the calculations and the results of a test to the terminal.
