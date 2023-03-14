# CS311_Triangulations
## Counting and Finding triangulations of a convex polygon.

To use this file, run main in python. By answering the input prompts, you can *calculate* or *find* all triangulations, and choose whether or not to print.

There are two ways to look at triangulations. 

- One method uses dynamic programming to quickly calculate the number of triangulations. This implementation takes O(n^2) time to run, and it can calculate for n<=1000 almost immediately.

- The other method explicitly finds the collection of all lists of diagonals and iterates through that using a generator. This method is more important.

I chose to save as little information as possible, in order to reach the hightest n possible. The general strategy was to use a recursive generator of triangulations. The value of a generator in python is that it does NOT store the result and output all at once. Instead, it finds one triangulation at a time, spits it out, and then moves on. The recursive strucuture was to split the polygon into pieces, then find all triangulations of each piece and combine them together by concatenating their lists of diagonals.

To utilize this function, there are multiple approaches. We can iterate through the diagonal lists and print each one, which is the goal of the assignement. Alternately, we could simply increase a counter and spit out the total number, since printing takes a long time. The last approach is to append each diagonal list to a Master Set. This is a way to store all the triangulations. The PRINTING and COUNTING approaches are implemented, while the STORING approach is in the comments.

This progam was able to COUNT up to n=20 and PRINT up to n=18, each in a few minutes. In addition, it can COUNT up to n=14 and PRINT up to n=13 instantly.
