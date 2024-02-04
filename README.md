# UbiquityInc

## Description

This linear programming project was developed for the class of Analysis and Synthesis of Algorithms using the PuLP library in Python.

## Objective

Calculate the **maximum profit** that can be extracted from the production of toys and packs of toys given some additional constraints.

- Refer to the file `p3.pdf` for the project's instructions and details.
- Refer to the file `relatorio_ubiquity_inc.pdf` for the full report on the solution's time complexity and description.

**Source Code:** The source code for the problem's solution is in the `src` directory in the file `proj3.py`.

To run `proj3.py` use:
> **python3 yourprogram.py < input_file**

**Unit Tests:** To generate unit tests you can use `gen_ubiquity.cpp` under the `generator` directory.

To compile `gen_ubiquity.cpp`, use:
> **g++ -std=c++11 -O3 -Wall -o gen_ubiquity gen_ubiquity.cpp -lm**

To run `gen_ubiquity.cpp` use:
> **./gen_ubiquity T P Tcmin Tcmax Tlmax Pok seed > testfile**
Where:
>- T is the number of toys
>- P is the number of packs of toys
>- Tcmin is the toy's minimum capacity
>- Tcmax is the toy's maximum capacity
>- Tlmax is the maximum toy profit
>- Pok is the percentage of valid packs
>- seed is a random seed generator (optional argument)


