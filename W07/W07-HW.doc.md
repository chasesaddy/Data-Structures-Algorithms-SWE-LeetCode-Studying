<!-----
Conversion notes:
* Docs to Markdown version 1.0β34
* Tue Oct 24 2023 12:10:49 GMT-0700 (PDT)
* Source doc: W7 Coachable Practice HW
----->

# W07 Dynamic Programming Work 

### **Free Response Questions**

1. Describe dynamic programming.

A programming technique where you break down a larger problem into smaller subproblems which you can solve. As you compute the solutions to the subproblems, you store the solution to each subproblem so that each sub-problem is computed at most once. Optimal substructure.
Dynamic programming involves two key steps:
    - Subproblem decomposition: The original problem is divided into a set of overlapping subproblems. This is often done recursively, where each problem is broken down into smaller parts until a base case is reached.
    - Solution storage and re-use: The solutions to each subproblem are stored, typically in a table or an array for easy access. This process, known as memoization, avoids redundant computation of the same subproblem, which significantly improves efficiency.


2. When should you use dynamic programming? What types of problems where you should consider dynamic programming as a possible solution?

- Numerical Solution: Problems that require a numerical answer, especially those asking for a "total" amount (such as total paths, combinations, or permutations). Vs returning all of the paths which is not DP-compatible.
- Optimization Language: When the problem involves finding a "Maximum/Minimum" value (product, sum, etc.)
- Repeated Subproblems: Notice if you're calculating the same solution multiple times in separate but similar subproblems. This redundancy is a classic hallmark
- Overlapping Subproblems: When a problem can be divided into smaller parts that similar and reoccur throughout the problem.


3. What is the difference between top-down and bottom-up dynamic programming?

Bottom-up DP: starts with the simplest subproblems and uses their solutions to solve larger subproblems, building up to the original problem. This is often implemented using iteration and a table to store results of subproblems. The process starts from the "bottom" (the simplest subproblems) and works its way "up" to the original problem.

Top-down DP: starts with the original problem and breaks it down into subproblems. This is often implemented using recursion, sometimes with memoization to store results of subproblems to avoid redundant computations. The process starts from the "top" (the original problem) and works its way "down" to the base cases.


4. “Memoization” can be thought of as “caching” all the recursive calls that have already happened. What might be a reason why I wouldn’t want to do that?

Space complexity. Storing everything in memory when for something like binary tree traversal, that isn’t going to be worth it.
This also relates to If the sub-problems aren’t repetitive enough. If we aren’t solving the same subproblems again and again, memoization likely isn’t worth it.


5. Oftentimes, the answer `f(n)` may only require the result from `f(n-1)`​ and `f(n-2)`. What kind of space/memory optimization can we do if this is the case? If it helps, you can give an example of a specific problem.

If the current state of f(n) only depends on a constant number of previous states, like f(n-1) and f(n-2), we don't need to store all the previous states. We can just keep the last two states and update them as we go, reducing the space complexity to O(1).


6. What if we had a `f(r, c)` that relied only on ​`f(r-1, c)` for some arbitrary `c`? What kind of space/memory optimization can we do if this is the case? If it helps, you can give an example of a specific problem.

Cache the last f(r - 1, c) computed value. So O(1) space.


7. Fibonacci is one example of a 1-dimensional recurrence relation optimized with dynamic programming. Identify and share 3 other classes of dynamic programming problems that seem similar and describe what makes them feel similar.

Climing Stairs: need to keep track of n-1 and n-2 variables or the current stair
Sequences:  Like the longest increasing subsequence problem asks for the longest subsequence of a given sequence. We only need to keep track of the current position in the sequence
Some grid problems work where you only need to keep track of the current/previous row and/or column


8. Is this statement true or false?
"Dynamic programming only helps problems that have a brute-force recursive solution."

Not true. Dynamic programming can help optimize any problem that can be broken down into overlapping subproblems, whether or not a brute-force recursive solution exists. However, in practice, these tend to be problems that can also be solved using recursion.


### **Dynamic Programming and Recurrence Examples**

Each of the below problems can be solved with recursion. Please answer the following for each one.
1. **Unit Tests**. Identify the solution cases up to n= 4. For 2D, do all cases up to (3,3)
2. **Recurrence Relation.** Identify the recurrence relationship and base cases. Explain why they are true by giving a qualitative explanation in plain English.
3. **Bottom Up.** Compute a small example using a bottom-up (n = 6, m = 6)
4. **Top Down Approach.** Compute a small example using a top-down approach with memorization. (n=6,m=6)
5. **Complexity Analysis.** Identify the optimal runtime and space complexity.
6. **Is DP worth it?** Does dynamic programming improve the runtime compared to a recursive approach?


#### **Problems That Can Be Solved with Recursion**


1. Number of paths up a staircase of length `N` where you take `1` or `2` steps each time. **Example provided**.

a. f(0) = 1, f(1) = 1, f(2) = 2, f(3) = 3, f(4) = 5

b. f(n) = f(n-1) + f(n-2) This is because to get to step n you can get there by taking 1 step from n-1 or 2 steps from n-2 . Therefore the number of paths to n is the total number of paths from n-1 plus the number of paths from n-2

c. f(0) = 1, f(1) = 1, f(2) = 2
f(3) = f(2) + f(1) = 3
f(4) = f(3) + f(2) = 5
f(5) = f(4) + f(3) = 8
f(6) = f(5) + f(4) = 13
This shows the call stack.

d. The bottom call `f(2)` is completed first.
f(6) = f(5) + f(4) = 13 #f(6)=13 is stored in the memoization.
f(5) = f(4) + f(3) = 8  #f(5)=8 is stored in the memoization.
f(4) = f(3) + f(2) = 5  #f(4)=5 is stored in the memoization.
f(3) = f(2) + f(1) = 3  #f(3)=3 is stored in the memoization.
f(2) = f(1) + f(0) = 2  #f(2)=2 is stored in the memoization.

e. Runtime is O(n) and space O(1) if we only cache the previous 2 elements. Otherwise O(n) space.

f. Yes. If we used plain recursion, the runtime would be exponential. Dynamic programming gets us an O(n) runtime.


-----

2. Computing the number of permutations of `[1-n]` i.e. `[1,2,3,4,5,...n-1,n]`

a. f(1) = 1 permutation: [1].
f(2) = 2 permutations: [1,2] and [2,1].
f(3) = 6 permutations: [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
f(4) = 24 permutations

b. f(n) = n * f(n - 1).
This is because for each element in the set, there are n different positions it could take in a permutation, and for each of these positions, there are f(n - 1) ways to arrange the remaining n - 1 elements.

base case: n == 1: return 1

c. f(0) = 0, f(1) = 1
f(2) = 2 * f(1) = 2
f(3) = 3 * f(2) = 6
f(4) = 4 * f(3) = 24
f(5) = 5 * f(4) = 120
f(6) = 6 * f(5) = 720

d. The recursive stack so the bottom call gets called last and completed first:
f(6) = 6 * f(5) = 720
f(5) = 5 * f(4) = 120
f(4) = 4 * f(3) = 24
f(3) = 3 * f(2) = 6
f(2) = 2 * f(1) = 2
f(1) = 1

e. That's correct. The runtime complexity is indeed O(n) because we're performing a single operation for each value from 1 to n. The space complexity is also O(n) because we're storing the result for each value from 1 to n, either in the recursion stack (for the top-down approach) or in the memoization table (for the bottom-up approach).

f.  Without dynamic programming, a naive recursive solution would have a time complexity of O(n!) because it would generate all permutations. However, with dynamic programming, we can reduce the time complexity to O(n) by avoiding redundant computations. 


-----

3. Unique Paths: The number of paths from the top left corner of a grid to the bottom right corner when moving only down and to the right.

a,c. [0] = 0 paths

(1,1)
[1,0] = 1 path

(2,2)
[2,1]
[1,0] = 2

(3,3)
[6, 3, 1]
[3, 2, 1]
[1, 1, 0] = 6

(4,4)
[20, 10, 4, 1]
[10, 6,  3, 1]
[4,  3,  2, 1]
[1,  1,  1, 0] = 20

(5,5)
[70, 35, 15, 5, 1]
[35, 20, 10, 4, 1]
[15, 10,  6, 3, 1]
[5,  4,   3, 2, 1]
[1,  1,   1, 1, 0] = 70

(6,6)
[252, 126, 56, 21, 6, 1]
[126,  70, 35, 15, 5, 1]
[56,   35, 20, 10, 4, 1]
[21,   15, 10, 6,  3, 1]
[6,    5,  4,  3,  2, 1]
[1,    1,  1,  1,  1, 0] = 252

b. f(r, c) = f(r - 1, c) + f(r, c - 1) 

base case:
r == 0 or c == 0: return 1

c. f(0, 0) = 0
_if 0 is either number, it is 0 because there is nothing to go to_

f(1, 1) = 1
f(2, 2) = 2
f(3, 3) = 6
f(4, 4) = 20
f(5, 5) = 70
f(6, 6) = 252

d. call stack:
f(1, 1) = 1
f(1, 2) = 1
f(1, 3) = 1
f(2, 1) = 1
f(2, 2) = 2
f(2, 3) = 3
f(3, 1) = 1
f(3, 2) = 3
f(3, 3) = 6

e. Time: O(n * m)
Space: O(n * m)

f. Yes, runtime goes from O(2^n) to O(n^2)
    

-----

4. Given a `2xN` grid, how many different ways can you fill the grid with `2x1`​ dominoes?

a. f(0) = 0, f(1) = 1, f(2) = 2, f(3) = 2, f(4) = 4

b. f(n) = f(n - 1) + f(n - 2)

base case:
if e == 0: return 1;

c. 
f(1) = 1
f(2) = 2
f(3) = f(2) + f(1) = 3
f(4) = f(3) + f(2) = 5
f(5) = f(4) + f(3) = 8
f(6) = f(5) + f(4) = 13

(1) = 1
[1, 1]

(2) = 2
[1, 1]
[2, 2]

[1, 2]
[2, 2]

(3) = 3
[1, 2, 3]
[1, 2, 3]

[1, 1, 3]
[2, 2, 3]

[3, 1, 1]
[3, 2, 2]


(4) = 5
4 vertical
[1, 2, 3, 4]
[1, 2, 3, 4]

4 horizontal
[1, 1, 2, 2]
[3, 3, 4, 4]

2 horizontal then 2 vertical
[1, 1, 3, 4]
[2, 2, 3, 4]

2 vertical then 2 horizontal
[3, 4, 1, 1]
[3, 4, 2, 2]

1 vertical, 2 vertical, 1 vertical
[1, 3, 3, 2]
[1, 4, 4, 2]

(5) = 8
5 vertical
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]

4 horizontal, 1 vertical
[1, 1, 2, 2, 5]
[3, 3, 4, 4, 5]

1 horizontal, 4 vertical
[5, 1, 1, 3, 4]
[5, 2, 2, 3, 4]

2 horizontal then 3 vertical
[1, 1, 3, 4, 5]
[2, 2, 3, 4, 5]

3 vertical then 2 horizontal
[3, 4, 5, 1, 1]
[3, 4, 5, 2, 2]

2 vertical, 2 horizontal, 1 vertical
[1, 2, 3, 3, 5]
[1, 2, 4, 4, 5]

1 vertical, 2 horizontal, 2 vertical
[1, 2, 2, 4, 5]
[1, 3, 3, 4, 5]

2 horizontal, 1 vertical, 2 horizontal
[1, 1, 3, 4, 4]
[2, 2, 3, 5, 5]

(6) = 13
6 vertical, 

2 horizontal + 4 vertical, 
4 horizontal + 2 vertical, 

2 vertical + 4 horizontal, 
4 vertical + 2 horizontal, 

2 horizontal + 2 vertical + 2 horizontal, 
2 vertical + 2 horizontal + 2 vertical, 

1 horizontal + 2 vertical + 3 vertical, 
3 vertical + 2 horizontal + 1 vertical, 

1 vertical + 4 horizontal + 1 vertical, 

2 horizontal + 1 vertical + 2 horizontal + 1 vertical, 
1 vertical + 2 horizontal + 1 vertical + 2 horizontal, 

6 horizontal


d. 
f(1) = 1
f(2) = 2
f(3) = f(2) + f(1) = 3
f(4) = f(3) + f(2) = 5
f(5) = f(4) + f(3) = 8
f(6) = f(5) + f(4) = 13


e. 
Runtime: O(n) because each subproblem is computed only once and the results are stored for future use.
Space, it's O(n) for the top-down approach because of the additional space required for the recursion stack. For bottom-up approach, if we only keep track of the last two computed values (since f(n) depends only on f(n-1) and f(n-2)), the space complexity can be optimized to O(1).


f. O(2^n) to O(n)



5. Given a `3xN` grid, how many different ways can you fill the grid with `3x1`​ dominoes?

a, c. 
(1)
[111]

(2)
[111]
[222]

1

(3)
[111]
[222]
[333]

[123]
[123]
[123]

2

(4)
[111] 
[222]
[333]
[444]

[123]
[123]
[123]
[444]

[444]
[123]
[123]
[123]

3

(5)

[111] 
[222]
[333]
[444]
[555]

[123]
[123]
[123]
[444]
[555]

[444]
[123]
[123]
[123]
[555]

[444]
[555]
[123]
[123]
[123]

(6)
[111] 
[222]
[333]
[444]
[555]
[666]

[123]
[123]
[123]
[444]
[555]
[666]

[444]
[123]
[123]
[123]
[555]
[666]

[444]
[555]
[123]
[123]
[123]
[666]

[444]
[555]
[666]
[123]
[123]
[123]

5

--

Apparently this is wrong and the 3x1 domino is always vertical according to Coachable-AI.

a, c, d:
f(0) = 0
f(1) = 1
f(2) = 1
f(3) = 1
f(4) = 1
f(5) = 1
f(6) = 1

f(0) = 0
f(1) = 1
f(2) = 1
f(3) = 1
f(4) = 1
f(5) = 1
f(6) = 1

b.
n == 0: return 0
n == 1: return 1

e. O(1)

f. No, it's already so simple


6. Given a set `A = {1,2,3,...,N}`​ calculate the number of possible [subsets](https://en.wikipedia.org/wiki/Subset)of `A`.

a. f(0) = 1, f(1) = 2, f(2) = 4, f(3) = 8

f(0) = 1 ({})
f(1) = 2 ({1} and {})
f(2) = 4 ({1,2}, {1}, {2}, {})

b. 
the number of subsets of a set with n elements is equal to twice the number of subsets of a set with n-1 elements. This is because for each subset of the n-1 elements, we have two options: either include the nth element or not.

f(n) = 2 * f(n-1)
base case: f(0) = 1

c. 
[1, 2, 4, 16, 32, 64]

d.
f(0) = 1
f(1) = f(0) * 2 = 2
f(2) = f(1) * 2 = 4
f(3) = f(2) * 2 = 8
f(4) = f(3) * 2 = 16
f(5) = f(4) * 2 = 32
f(6) = f(5) * 2 = 64

e. 
O(n) time complexity
O(1) space if only keeping track of previous element. Otherwise O(n) for array/memo space. And for top-down, O(n) call stack space

f. Yes. Can do it in O(n) vs O(2^n).


7. Given a set `A = {1,2,3,...,N}`​ calculate the number of possible[ subsets](https://en.wikipedia.org/wiki/Subset)of `A` that do not contain any 2 numbers that are 1 apart. For example, `{1,2,4}` would not be valid because `1` and `2` are 1 apart.

a. f(0) = 1, f(1) = 2, f(2) = 3, f(3) = 5

b. f(n) = f(n - 2) + f(n - 1).
If we have a set with n elements, we can either include the largest element (n) in our subset or not.

If we include n, then we can't include n-1 (because they are 1 apart), so we're left with the problem of finding the number of valid subsets of the set {1, 2, ..., n-2}, which is f(n-2).

If we don't include n, then we're left with the problem of finding the number of valid subsets of the set {1, 2, ..., n-1}, which is f(n-1).

c, d. 
f(0) = 1
f(1) = 2
f(2) = 3
f(3) = 4
f(4) = 8
f(5) = 13
f(6) = 21

(0) = 1
[]

(1) = 2
[],
[1]

(2) = 3
[],
[1],
[2]


(3) = 4
[],
[1],
[2],
[3],
[1, 3]

(4) = 8
[],
[1],
[2],
[3],
[4],
[1, 3],
[1, 4],
[2, 4]


(5) = 13
[],
[1],
[2],
[3],
[4],
[5],
[1, 3],
[1, 4],
[1, 5],
[2, 4],
[2, 5],
[3, 5],
[1, 3, 5]


(6) = 21
[],
[1],
[2],
[3],
[4],
[5],
[6],
[1, 3],
[1, 4],
[1, 5],
[1, 6],
[2, 4],
[2, 5],
[2, 6],
[3, 5],
[3, 6],
[4, 6],
[1, 3, 5],
[1, 3, 6],
[1, 4, 6],
[2, 4, 6]


e. 
The time complexity is O(n), because we're computing the number of valid subsets for each set from 0 to n.

The space complexity is also O(n), because we're storing the number of valid subsets for each set from 0 to n. Or the call stack.
Or only need the final result can keep track of the last two results.


f. Yes, better than original O(n^2) runtime.



8. Count the number of[ functions](https://en.wikipedia.org/wiki/Function_(mathematics))from `{1,2,3,...,N}` to a set of size `{1,2,3,...,M}`​.

a. f(1, 1) = 1, f(2, 2) = 4, f(3, 3) = 27, f(4, 4) = 64

b. F(N, M) = M * F(N - 1, M)
base case: F(1, M) = M
there are M possible functions from a set of size 1 to a set of size M


c. 
[1,  2,   3,     4,       5,   6]
[1,  4,   9,     16,    25,   36]
[1,  0,   0,     0,     0,   216]
[1,  0,   0,     0,     0,  1296]
[1,  0,   0,     0,     0,  7776]
[1, 36, 216,  1296,  7776, 46656]

d. 
f(1) = m = 6
f(2) = m * f(1) = 36
f(3) = m * f(2) = 216
f(4) = m * f(3) = 1296
f(5) = m * f(4) = 7776
f(6) = m * f(5) = 46656


e. Time: O(N * M). Fill in a 2D table of size N x M.
Space: O(N * M) because we need to store the entire 2D table.
Could get space down to O(max(N, M)) only storing the last needed rows/columns as needed for the result

f. Yes a normal function would be an awful runtime while this gets down to O(N * M) for runtime and space is much smaller


9. A function has a[ fixed point](https://en.wikipedia.org/wiki/Fixed_point_(mathematics)) if `f(x) = x` for any `x` in the domain of `f` . How many functions are there from `{1,2,3,...,N}` to `{1,2,3,...,M}`​ without any fixed points? Hint, approach the problem in cases, then put it all together.

1. Case 1: Assume that `M=N`


2. Case 2: Assume that `N <= M`


3. Case 3: Assume that `N > M`

​
4. Combine Cases 1-3 to get a general recurrence.



10. Let's say a function is **reducing** if `f(x) &lt;= x`​ for all x in the domain of `f`. How many **reducing** functions are there from `{1,2,3,...,N}` to `{1,2,3,...,M}`​?

1. Case 1: Assume that `M=N`


2. Case 2: Assume that `N <= M`


3. Case 3: Assume that `N > M`

​
4. Combine Cases 1-3 to get a general recurrence.



#### Fibonacci Example (Problem 1)



1. `f(0) = 1, f(1) = 1, f(2) = 2, f(3) = 3, f(4) = 5`

2. `f(n) = f(n-1) + f(n-2)` This is because to get to step `n` you can get there by taking 1 step from `n-1` or 2 steps from `n-2` . Therefore the number of paths to `n` is the total number of paths from `n-1` plus the number of paths from `n-2`

f(0) = 1, f(1) = 1, f(2) = 2
f(3) = f(2) + f(1) = 3
f(4) = f(3) + f(2) = 5
f(5) = f(4) + f(3) = 8
f(6) = f(5) + f(4) = 13




1. This shows the call stack.
###### The bottom call `f(2)` is completed first.
f(6) = f(5) + f(4) = 13 #f(6)=13 is stored in the memoization.
f(5) = f(4) + f(3) = 8  #f(5)=8 is stored in the memoization.
f(4) = f(3) + f(2) = 5  #f(4)=5 is stored in the memoization.
f(3) = f(2) + f(1) = 3  #f(3)=3 is stored in the memoization.
f(2) = f(1) + f(0) = 2  #f(2)=2 is stored in the memoization.



2. Runtime is O(n) and space O(1) if we only cache the previous 2 elements.

3. Yes. If we used plain recursion, the runtime would be exponential. Dynamic programming gets us an O(n) runtime.


#### **OPTIONAL: Recursive Challenge Problems**

**Hint**: For these, you can assume the distinct integers are `1,2,3,...,N`​ Moreover, 8-11 are very tricky, so don't hesitate to Google more references for those ones. However, make sure you understand how they arrived at those solutions.


##### These ones are very tough and **completely optional.**



1. Given a `4xN` grid, how many different ways can you fill the grid with `2x1`​ dominoes?


2. How many binary trees can you create with `N` distinct integers? Assume `N=2^n-1`​ i.e. so `N` is the number of elements in a complete binary tree.


3. How many binary search trees can you create with `N=2^n-1` distinct integers?


4. How many distinct binary heaps can you create with `N=2^n-1`​ distinct integers?


5. We say a binary tree is level-sorted if every element is larger than every element in a lower level (even if they are in different subtrees). Note all level-sorted trees are also heaps, but not all heaps are level-sorted. Notice that BInary Tree A below is a heap but NOT level-sorted since (6) is larger than 4 but is at a lower level in the tree.

Binary Tree A

      9

     / \

    4   8

   / \ / \

  1  2 6  7


###### How many binary trees can you create with `N=2^n-1` distinct integers that are **level sorted**?


###### **Challenge**: Now solve 8-11 without assuming `N=2^n-1`
