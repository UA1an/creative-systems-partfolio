- [[SFCC notes week 2]]
-  [[SFCC Week 4 (FLOSS)]]
- [[GA Week 5 Fractal]]
- [[SFCC Week 6 (Further Python)]]
### Lists

- **Group together elements in a list:**
  `beatles = [’John’, ‘Paul’, ‘George’, ‘Ringo’]`
   *Can be nested arbitrarily:*
	 `bands = [`
		`[‘’Anni-Frid’, Bjorn’, ‘Benny’, ‘Agnetha’],`
		`[‘Lemmy’, ‘Eddy’, ‘Phil’],`
		`[‘Bono’, ‘Edge’, ‘Adam’, ‘Larry’],`
		`[’Roger’, ‘Dave’, ‘Richard’, [‘Syd’], ‘Nick’],[‘Nigel’, ‘David’, ‘Derek’, ‘”Caucasian” Jeffrey’, ‘Gregg’] ]`

- **You can access individual elements using an index variable:**
  `drummer = beatles[3]`
    *Note that lists start at index[0]*
  You won’t have to do this very often, since for loops make it easy to work through a list

- **length(list) gives the number of elements in a list**
  *There are also methods to get the first element, get the rest, append items to the list, reverse a list etc.*

- **You may also encounter ==“tuples”**==
	- Tuples are in (round brackets) not [square brackets]
	- Tuples and immutable – you can’t extend or shorten them
	- The parameters of a function are a tuple


### Dictionaries

**You can also collect data into a dictionary:**

`person = {`
	`‘name’: {`
		`‘first’: ’Andy’,`
		`‘last’: ’Holyer’`
		`},`
	`‘job’: ‘Senior Teaching Fellow’`
`}`

- Just like a list, but instead of indexing by a number, it’s indexed by the key (on the left) print(person[‘job’])

- Dictionaries are optimised so that access times are (almost) the same regardless of how many entries are in the dictionary
	  *You’ll definitely be fine with a couple of thousand entries*

-  Dictionary entries can be anything – other dictionaries, objects, anything…


## Usibg Dicitonaries: 
### Sorting alphabetically

`mydict = {`
	`'carl':40,`
	`'alan’:2,`
	`'bob’:1,`
	`'danny’:3`
`}`
`for key in sorted(mydict.iterkeys()):`
`print"%s:%s” % (key, mydict[key])`

### Counting words (or anything else)

`def word_count(string):`
	`my_string=string.lower().split()`
	`my_dict={}`
	`for item in my_string:`
		`my_dict[item]++`
	`print(my_dict)`
`word_count("I am what I am")`


## Shelves

**The shelve library allows you to link a dictionary to an external disk file**

**This can give you a quick and easy “mini-database” which persists between runs of the program.**
- I like shelves…
- ==WARNING:== shelves are basically insecure
  - If you create a shelf, and store it on a local disk, you’ll be fine
  - Never open a third-party shelf – other code may execute without you knowing…

### Example
![[Screenshot 2025-11-13 at 15.32.45.png]]


## Loops and conditionals use similar syntax:
![[Screenshot 2025-11-13 at 15.41.32.png]]


## Conditional Statements
![[Pasted image 20251113154237.png]]


## Conditional Operators

| Meaning               | Maths Symbol | Python Symbol |
| --------------------- | ------------ | ------------- |
| Less than             | $<$            | `<`           |
| Greater than          | $>$            | `>`           |
| Less than or equal    | $≤$            | `<=`          |
| Greater than or equal | $≥$            | `>=`          |
| Equals                | $=$            | `==`          |
| Not Equal             | $≠$            | `!=`          |
#### Warning!

The operator for “equals” is “ == ” 
Don’t do:
	`if x=15:`
		`do_something`

Python will assign 15 to x, and since it can always do this, the if clause will always
succeed


## Logical expressions

You can combine conditional clauses together using and (&&) and or (||) (and a few
others)
So:
	`if (month == ‘February’) && (day == 14):`
		`# It’s valentine’s day`

This is called ==**“Boolean logic”**==, and is another skill you will learn in time

#### for loops
![[Pasted image 20251113155221.png]]
### Example:
`For counter in [‘one’, ‘two’, ‘three’]:`
	`print counter`
`#Loop has terminated here`

OR

 `for variable in ‘Andy Holyer’:`
	`print variable`
`#Loop has ended here…`


## Functions

There are lots of supplied python functions, and others come when you import libraries.
It’s also possible to define your own functions
You do this with the def keyword:
	`def sayhi( name):`
		`print “Hello” + name`
Here, the variable “name” is an **==argument==** of the function.
- Arguments are defined as local to the function invoked
- A copy of what is called is made when you enter the function and it goes away again when it is exited
- There are several other ways to define your arguments.
Above, the print function was **==a side effect==** of the function execution:
Alternatively, your function can return a value using the **==return==** keyword
If a function is defined inside a class definition, it will ”belong” to the instances of that class (the objects) and
is called a **==method==**
Functions can call themselves – this is called recursion

### Example: The Tower of Hanoi

`def moveTower( height, fromPole, toPole, withPole):`
	`if height >= 1:`
		`moveTower( height-1, fromPole, withPole, toPole)`
		`moveDisk( fromPole, toPole)`
		`moveTower( height-1, withPole, toPole, fromPole)`
`def moveDisk(frompole, toppole):`
	`print("moving disk from", frompole, "to", topole)`
`moveTower( 3, "A", "B", "C")`


## Objects

An “Object” is an abstract data structure intended to mimic the real world
Everything in Python is an object (though you might not see this)

### Example: A Class
![[Pasted image 20251113160213.png]]



## JupyterLab [🧪](https://jupyter.org/try-jupyter/notebooks/?path=notebooks%2FIntro.ipynb#JupyterLab-%F0%9F%A7%AA)

**JupyterLab** is a next-generation web-based user interface for Project Jupyter. It enables you to work with documents and activities such as Jupyter notebooks, text editors, terminals, and custom components in a flexible, integrated, and extensible manner. It is the interface that you're looking at right now.

**For an overview of the JupyterLab interface**, see the **JupyterLab Welcome Tour** on this page, by going to `Help -> Welcome Tour` and following the prompts.

> **See Also**: For a more in-depth tour of JupyterLab with a full environment that runs in the cloud, see [the JupyterLab introduction on Binder](https://mybinder.org/v2/gh/jupyterlab/jupyterlab-demo/HEAD?urlpath=lab/tree/demo).


## Jupyter Notebooks [📓](https://jupyter.org/try-jupyter/notebooks/?path=notebooks%2FIntro.ipynb#Jupyter-Notebooks-%F0%9F%93%93)

**Jupyter Notebooks** are a community standard for communicating and performing interactive computing. They are a document that blends computations, outputs, explanatory text, mathematics, images, and rich media representations of objects.

JupyterLab is one interface used to create and interact with Jupyter Notebooks.

**For an overview of Jupyter Notebooks**, see the **JupyterLab Welcome Tour** on this page, by going to `Help -> Notebook Tour` and following the prompts.

> **See Also**: For a more in-depth tour of Jupyter Notebooks and the Classic Jupyter Notebook interface, see [the Jupyter Notebook IPython tutorial on Binder](https://mybinder.org/v2/gh/ipython/ipython-in-depth/HEAD?urlpath=tree/binder/Index.ipynb).


### An example: visualizing data in the notebook [✨](https://jupyter.org/try-jupyter/notebooks/?path=notebooks%2FIntro.ipynb#An-example:-visualizing-data-in-the-notebook-%E2%9C%A8)

Below is an example of a code cell. We'll visualize some simple data using two popular packages in Python. We'll use [NumPy](https://numpy.org/) to create some random data, and [Matplotlib](https://matplotlib.org/) to visualize it.

Note how the code and the results of running the code are bundled together.

```python

from matplotlib import pyplot as plt
import numpy as np

# Generate 100 random data points along 3 dimensions
x, y, scale = np.random.randn(3, 100)
fig, ax = plt.subplots()

# Map each onto a scatterplot we'll create with Matplotlib
ax.scatter(x=x, y=y, c=scale, s=np.abs(scale)*200)
ax.set(title="Some random data, created with JupyterLab!")
plt.show()

```

![[Pasted image 20251113162527.png]]