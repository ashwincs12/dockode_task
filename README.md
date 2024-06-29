# dockode_task

## Output
<img width="332" alt="image" src="https://github.com/ashwincs12/dockode_task/assets/65584312/8ae5d7d0-4245-4582-ac8d-35f72c19f36e">

## Code Explanation
```python

    top = " ___ "
    middle = "/   \\"
    bottom = "\\___/"
    alt_top="___"
    space="   "
```
These are the parts of the hexagon which iterates to produce the required pattern. <br>


**alt_top** denotes the even iterative columns which are connected to the odd ones via the string consisting of 3 underscores. <br>
**space** denotes the left out area between each hexagon which consists of the same characters as of the **alt_top**, i.e, 3 spaces. <br>

```python
    modified_cols= math.ceil(columns/2)
```
Since I'm printing each hexagon along with the **alt_top**(which automatically prints the even columns), I must iterate only half the number of times of the given column parameter. To solve the decimal issue, I used the ceil function from math library.

```python
    for row in range(rows):
```
The outer loop iterates **rows** times which contains 3 inner loops for printing the top, middle and bottom part of the hexagon. 

```python
      if row==0:
      for col in range(modified_cols):
          print(top + space, end="")
      print()
```
The first inner loop prints the top part along with the space for **alt_top** of the hexagon. This is triggered only for the first row.

```python
       for col in range(modified_cols):
              #Hexagons in last column does not need the alt_top part
              if(col==modified_cols-1):
                  print(middle, end="")
                  continue
              #Other hexagons (not in the last column) need the middle part and alt_top part
              print(middle + alt_top, end="")
          print()
```
The second inner loop prints the middle part of the hexagon along with the **alt_top**. The **alt_top** part is omitted for the last column.

```python
        for col in range(modified_cols):
            print(bottom+space,end="")
        print()
```
The third inner loop prints the bottom part of the hexagon along with space left for **alt_top**.


