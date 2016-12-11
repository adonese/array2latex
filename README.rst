Arraytolatex
============

It converts NumPy's arrays into valid LaTeX tables. I use NumPy a lot, and it is always the case that I wanted to convert some array to latex. I wanted something that `imported' in my jupyter notebook such that when I get my results I will directly convert them into LaTeX table (as oppose of converting them into a csv file, and then convert that into LaTeX using other service)

In my thesis, I used <https://www.tablesgenerator.com> which is really cool and very awesome. But it is not what I wanted, the step of converting into csv, and then uploading to the website was just not the very best way to do that.


TODO:
	- Include Pandas dataframes. I could already done that lazily by detecting the input type and then convert it to numpy and the rest of the code will be unchanged.
	- Refactoring the code, etc. It is a must. The code is horrible, yet it works, efficiently? I guess
	- Adding comments, using more informative names for variables. I really wish I could found something more informative than string_arry.
	- Please, this code is yours fork it modify it pull request, so that we have a better tool that will be the standard tool to convert NumPy arrays and other arrays into LaTeX tables.