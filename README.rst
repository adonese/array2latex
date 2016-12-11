array2latex
============

It converts NumPy's arrays into valid LaTeX tables. I use NumPy a lot, and it is always the case that I wanted to convert some array to latex. I wanted something that `imported' in my jupyter notebook such that when I get my results I will directly convert them into LaTeX table (as oppose of converting them into a csv file, and then convert that into LaTeX using other service)

In my thesis, I used `Tables Generator<https://www.tablesgenerator.com>`_ which is really cool and very awesome. But it is not what I wanted, the step of converting into csv, and then uploading to the website was just not the very best way to do that.

Uses
----

First you need to install it via pip using

.. code-block:: python

	pip install array2latex

Or using Anaconda, both work just fine, and they will always have the same lates version

.. code-block:: python

	conda install -c adonese array2latex

Starting `array2latex` is very simple. It is meant to be integrated with your workflow e.g., working with numpy array and output the final result into `LaTeX` table

.. code-block:: python

	from array2latex import tolatex
	import numpy as np
	# Assuming that you have done some cool stuffs with `NumPy`, you have
	# you output and want them to be in latex format
	# For me I will just use NumPy random array!
	array = np.random.rand(3, 4) # Create 3,4 random matrix
	table = tolatex(array, header=header)
	# And thats it! You now have a valid LaTeX table.

But there are even more to add. `array2latex` only have 2 required argumets, the array you want to convert (obviously), and the header of your table. You can also sepecify a `caption` of you table, and you can also add a `label` as you would normally do in a typical table in LaTeX. To do that is very simple actually, you just need to do

.. code-block:: python

	# Assuming you have imported all the necessary packages, and done you cool stuffs with numpy
	array = np.random.rand(3, 4) # Create 3,4 random matrix
	table = tolatex(array, header=["col1", "col2", "col3", "col4"], caption="My cool table", label="table:cool-table")

In the previous examples the output will be the stdout, i.e., your `jupyter notebook` or your terminal. However, we also allow you to store the results in a file. To do that

.. code-block:: python

	# Assuming you have imported all the necessary packages, and done you cool stuffs with numpy
	array = np.random.rand(3, 4) # Create 3,4 random matrix
	table = tolatex(array, header=["col1", "col2", "col3", "col4"], caption="My cool table", label="table:cool-table", output_file="somefile.txt") # The extenstion of the file doesn't really matter. It's just a txt file anyway.

So yes this is the whole about `array2latex`.

TODO
-----

	- Include Pandas dataframes. I could already done that lazily by detecting the input type and then convert it to numpy and the rest of the code will be unchanged.
	- Refactoring the code, etc. It is a must. The code is horrible, yet it works, efficiently? I guess
	- Adding comments, using more informative names for variables. I really wish I could found something more informative than string_arry.
	- Please, this code is yours, fork it, modify it, pull request, etc. so that we have a better tool to convert NumPy arrays and other arrays into LaTeX tables.
