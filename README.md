## QuickSort  
_**About**_  
Given a file of integers, this algorithm sorts elements in increasing order in O(nlog(n)) running time.  

---  

_**How it works**_  
1. The algorithm has a "pivot", which is always chosen to be the last element of the list. Then, it sorts all elements simply to the left or right of the pivot based on whether it's less than or greater than the pivot.  

2. After this, the pivot is known to be in the correct place, because the lists are seperated with greater than ans less than.

3. From here, the algorithm recursively repeats on the group of elements on the left and right of the pivot.  
---  

_**Methods**_  
- fileToArray(filename)
    - Takes in parameters for _filename_, a name for an input file.
    - Reads the file of integers and appends each integers to a returned array.  
- quickSort(list)  
    - Takes in as parameters _list_
          - _list_ is simply the list that is to be sorted.
    - This method serves as the main method for this algorithm.  
    - Partitions about a pivot to sort the pivot to its correct location.  
    - Recursively partitions about the left and right sides of the pivot by inputting the respective sides into the methos.  

---  

_**Input**_  
The qs_test files describes an array of numbers. It uses the following format:  

num1  
num2  
num3  
...  

[Example Input File]( https://github.com/Adithya-Sripada/Algorithms/blob/main/qs_test1.txt )  

---  
