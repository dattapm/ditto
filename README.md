# ditto
Ditto coding assignment

Assumptions:
1. Input file 'test_example.csv' is present in the same path as the code file 'points.py'.
2. Input file is not empty.
3. Input file has a line with atleast 2 float values seperated with a comma('). All values above 2 are ignored.
4. Program will exit with error code 1 if input file is not readable.
5. Program will exit with error code 1 if output cannot be written to a file.


Extra test cases:

1. Test case with either X or Y coordinate is missing.
2. Test case where X or Y are not float values.
3. Empty input file.
4. Input file with only 2 lines(not enough data to run the solution).
5. Input file with more that 2 values in each line(extra inputs should be ignored).
6. Test case where none of the data is on the same lines.
7. Test cases where the linear points are either vertically or horizontaly located.

Time complexity:

 The solution provided is a very basic one keeping in mind the available time.
 The time complexity for the same is O(n*2), since we are running two for loops to get the co0linear points.
 
Cases where code can fail:

What if the X coordinates of two points P1 and P2 are such that X2 - X1 is Zero(0). In this case slope of the line joining P1 and P2, will be infinity, resulting in unexpected results. Will need to add a proper fix for this issue.
