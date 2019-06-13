Numpy checklist: https://github.com/ageron/handson-ml/blob/master/tools_numpy.ipynb

Data analysis/Data Science

Cover topics mentioned here still: https://github.com/kgdunn/digital-skills-module5/blob/master/Notebooks/02.0%20NumPy%20arrays.ipynb
Consider elements from this notebook for module 1 and 2: https://nbviewer.jupyter.org/github/engineersCode/EngComp1_offtheground/blob/master/notebooks_en/2_Jupyter_strings_and_lists.ipynb

Containers
==========
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

Strings
=========
* M3: List comprehension. Find number of AGTC entries in a sequence.
* M3: Read genome. Stop when you find first sequence of GATTAG

Lists
======
# CAUTION! You cannot copy a list simply by typing species2 = species,
# because: species2 will only be a reference to list1,
# and changes made in species will automatically also be made in species2
species2 = species
species2.append('wrong')

# Count number od 'wrong' elements in the
# 'species list using the 'count' function
print("Number of wrong elements: {}".format(species.count('wrong')))

# Make a list with first 10 elements of the
# multiplication table of 2 (tafel van 2)
# using "Python list comprehension"
print([2**x for x in range(1,11)])


if-else
--------

M3: Go back to the quadratic example: solve for various values of a and b and c in the equation.

One-liner if statement:
a = 3
b = 4
q = a if a < b else b


Example:

analysis_type = ['MACHINE_TTR', 'MACHINE_PH', 'CellCount method1', 'CellCount method2', 'CellCount method 3']

Write a one-liner if-else that returns a variable called ``axis_type`` which has the value of 'log' if the
``analysis_type`` contains the word 'CellCount', or otherwise returns the value 'linear'.
Write a for loop that iterates over the ``analysis_type`` list, and returns the appropriate 'axis_type' value.


For loop
---------
Newton's method with this plan (sketch out on paper)
1. Initialize a
2. Initialize x to a/2
3. Repeat a few times:
>Replace x by (x + a/x)/2
>Display x
4. Stop; show the true value

Vectorization:
s = 0
for n = 1:100000
    s += 1/n^**

# Wait for numpy
n = arange(100000)
s = sum( 1 / n**2 )


While loop
----------

while True:
   print('Hi')
   # Infinite while loop. How to stop it?

While loop with += incremental operator; mention other operators are also possible: -= *= /=

Do while loop. Execute, then check: can be done with a break statement and condition check at end of a while True loop.

Example. Keep going until you see a particular DNA sequence. Or peak value above certain threshold

Style
-----
Comments: TODO comments used sparingly

Loops
-------
Make the Fibonacci series with append function

Files
-------
Write to file

Types
------
change from one type to another:
* float(45)
* int(45.7)
* round(45.7)  # different result
* chr(65)
* Won't loose precision with ints. If a is int And multiplied by float, it is upgraded

Lists
-------
Then you can iterate on that list, or do anything that lists can do. This section explores list methods

* See mikedane resources
* Find entries which appear more than once in a list
* Common elements into two different lists. Join function equivalent?
* Count how many entries in a list are greater than a threshold. List comprehension
* Contrast with tuples. Seen before. Immutable concept introduced

General exercises
---------------------
Random number. Guess it's value. If else, while loops printing.

Later module: Dictionaries introduced:
------------------
Calculate the molar mass given a chemical formula: C5H9NOS. Methionine. Do for others amino acids

NumPy
-----

### Try these elementwise operations on arrays yourself

>1. Calculating the absolute values: `np.fabs(...)` and  `np.absolute(...)`
>2. Comparing two arrays and return the minimum `np.fmin(...)` and maximum `np.fmax(...)`
>3. The reciprocal value of $x$ is equal to $1/x$. You can calculate it using `np.reciprocal(...)`
>4. The sign of the values in the array: `np.sign(...)`


* get the element in row 2, column 3, layer 4
* iterate over elements of an array
* recap an exercise from last week.
* write entries to an array index
* matrix multiplication for regression: https://nbviewer.jupyter.org/github/engineersCode/EngComp1_offtheground/blob/master/notebooks_en/5_Linear_Regression_with_Real_Data.ipynb


**Exercises**

* Random walk
* Average of the dice thrown tends to be normally
* Linear system of equations a least squares equation for a doe
* eig and svd
* 3D array: calculate summary values across each axis


Raspberry PI question
