#
#
#
temp(A) = (1,4,7,6,3), (12,14,10), (8) = (), (),  = 65
temp(B) = (5,4,3,2), (1) = (), (), () = 15
temp(C) = (8,9,4,10,11,5,2), (6,7,3), (1) = (), (), () = 
temp(D) = (4,5,2), (5,4,2), (1) = (), (), () = 
temp(E) = (10,4,5,2), (9,8,6,3), (1) = (), (), () = 

tmp(A) = ( (1: 1 || 4,7,6: 2) + 3: 1 ), (12: 1,14: 1,10: 1), (8: 1) = ( (2+1), (3) ) = 3
tmp(B) = (), (5: 1, 4: 1, 3: 1, 2: 1), (1) = (1+1+1+1) = 4
tmp(C) = ( (8,9,4: 2 || 10,11,5: 2) + 2: 1 ), (6,7,3: 2), (1) = ( (2 + 1), (2) ) = 3
tmp(D) = ( (4,5,2: 2), (5,4,2: 2) ), (1) = (2) = 2
tmp(E) = ( (10,4: 1 || 5: 0) + 2: 1 ), (9: 1, 8: 1, 6: 1, 3: 1), (1) = ( (1 + 2), (1 + 1 + 1 + 1) ) = 4

tpp(A) = ( (1: 1 + 4,7,6: 2) <- 3 ), (12: 1,14,10) + (8: 0) = ( (1 + 2) + (1) ) = 4
tpp(B) = () + (5: 1, 4,3,2) + (1: 0) = (1) = 1
tpp(C) = ( (8,9,4: 2 + 10,11,5: 2) + 2: 0 ) + (6,7,3: 2) + (1: 0) = ( (2  2) + (2) ) = 6
tpp(D) = ( (4,5,2: 2) + (5,4,2: 2) ) + (1: 0) = (2 + 2) = 4
tpp(E) = ( (10,4: 1 + 5: 1) + 2: 0 ) + (9: 1, 8,6,3) + (1: 0) = ( (1 + 1) + (1) ) = 3

# 
# 
# 
size(A) = (1+4+7+6+3) + (12+14+10) + (8) = (5) + (3) + 1 = 9
size(B) = () + (5+4+3+2) + (1) = (4) + (1) = 5
size(C) = (8+9+4+10+11+5+2) + (6+7+3) + (1) = (7) + (3) + 1 = 11
size(D) = (4+5+2) + (5+4+2) + (1) = (3) + (3) + 1 = 7
size(E) = (10+4+5+2) + (9+8+6+3) + (1) = (4) + (4) + 1 = 9

sum(A) = (1+4+7+6+3) + (12+14+10) + (8) = () + () + 8 = 65
sum(B) = () + (5+4+3+2) + (1) = (14) + 1 = 15
sum(C) = (8+9+4+10+11+5+2) + (6+7+3) + (1) = (49) + (16) + 1 = 66
sum(D) = (4+5+2) + (5+4+2) + (1) = (11) + (11) + 1 = 23
sum(E) = (10+4+5+2) + (9+8+6+3) + (1) = (21) + (26) + 1 = 48

max_val(A) = (1 || 4,7,6 || 3), (12,14,10), (8) = (7), (14), 8 = 14
max_val(B) = (), (5,4,3,2), (1) = (5), 1 = 5
max_val(C) = (8,9,4 || 10,11,5 || 2), (6,7,3), (1) = (11), (7), 1 = 11
max_val(D) = (4,5,2), (5,4,2), (1) = (5), (5), 1 = 5
max_val(E) = (10,4 || 5 || 2), (9,8,6,3), (1) = (10), (9), 1 = 10

is_symmetric(K) = (left(L,R,root)) || (right(L,R,root)) aka flip the left and right each time.
is_symmetric(A) = (1 || 4,7,6 || 3), (12,14,10), (8) = (7,4,6 || 1 || 3), () = False
is_symmetric(B) = (), (5,4,3,2), (1) = (), (5,4,3,2) = False
is_symmetric(C) = (8,9,4 || 10,11,5 || 2), (6,7,3), (1) = (11,10,5 || 9,8,4 || 2), (7,6,3) = False
is_symmetric(D) = (4,5,2), (5,4,2), (1) = (5,4,2), (4,5,2) = True
is_symmetric(E) = (10,4 || 5 || 2), (9,8,6,3), (1) = (5,10,4,2), (9,8,6,3) = False

height(A) = ( (1: 1 || 4,7,6: 2) + 3: 1 ), (12: 1,14: 1,10: 1), (8: 1) = ( (2+1), (3) ) = 3
height(B) = (), (5: 1, 4: 1, 3: 1, 2: 1), (1) = (1+1+1+1) = 4
height(C) = ( (8,9,4: 2 || 10,11,5: 2) + 2: 1 ), (6,7,3: 2), (1) = ( (2 + 1), (2) ) = 3
height(D) = ( (4,5,2: 2), (5,4,2: 2) ), (1) = (2) = 2
height(E) = ( (10,4: 1 || 5: 0) + 2: 1 ), (9: 1, 8: 1, 6: 1, 3: 1), (1) = ( (1 + 2), (1 + 1 + 1 + 1) ) = 4

max(height) + max(height) + 1
diameter(A) = ( (1: 1 || 4,7,6: 2) + 3: 1 ), (12: 1,14: 1,10: 1) + (8: 1) = ( (2+1) + (3) ) = 6
diameter(B) = (), (5: 1, 4: 1, 3: 1, 2: 1) + (1) = (1+1+1+1) = 4
diameter(C) = ( (8,9,4: 2 || 10,11,5: 2) + 2: 1 ), (6,7,3: 2) + (1) = ( (2 + 1) + (2) ) = 5
diameter(D) = ( (4,5,2: 2) + (5,4,2: 2) ) + (1) = (2 + 2) = 4
diameter(E) = ( (10,4: 1 || 5: 0) + 2: 1 ), (9: 1, 8: 1, 6: 1, 3: 1) + (1) = ( (1 + 2) + (1 + 1 + 1 + 1) ) = 7

leafs(A) = ( (1: 1 + 4,7,6: 2) <- 3 ), (12: 1,14,10) + (8: 0) = ( (1 + 2) + (1) ) = 4
leafs(B) = () + (5: 1, 4,3,2) + (1: 0) = (1) = 1
leafs(C) = ( (8,9,4: 2 + 10,11,5: 2) + 2: 0 ) + (6,7,3: 2) + (1: 0) = ( (2  2) + (2) ) = 6
leafs(D) = ( (4,5,2: 2) + (5,4,2: 2) ) + (1: 0) = (2 + 2) = 4
leafs(E) = ( (10,4: 1 + 5: 1) + 2: 0 ) + (9: 1, 8,6,3) + (1: 0) = ( (1 + 1) + (1) ) = 3

top_ordered(A) = ( ( (1 && 4,7) > 6) > 3 ) && (12 > 14 > 10) > (8) = ( (True && False) && (False) ) > 8 = False
top_ordered(B) = () + (5 > 4 > 3 > 2) > (1) = (True) > 1(True) = True
top_ordered(C) = ( (8,9 > 4 && 10,11 > 5) > 2 ) && (6,7 > 3) > (1) = ( (2  2) > 1(True) ) = True
top_ordered(D) = ( (4,5 > 2) && (5,4 > 2) ) > (1) = (2 + 2) > 1(True) = True
top_ordered(E) = ( (10 > 4 && 5) > 2 ) && (9 > 8 > 6 > 3) > (1) = ( (True && True) && (True) ) > 1(True) = True

# k = 2
find_height(A, k) = ( (1: 1 + 4,7, 6: 1) + 3: 0 ), (12: 0 + 14: 1 + 10: 0), (8: 0) = ( (1+1) + (1) ) = 3
find_height(B, k) = (), (5,4: 0 + 3: 1 + 2: 0) + (1: 0) = (1) = 1
find_height(C, k) = ( (8,9, 4: 1 + 10,11, 5: 1) + 2: 0 ), (6: 1,7: 1, 3: 0) + (1: 0) = ( (1 + 1) + (1+1) ) = 4
find_height(D, k) = ( (4: 1, 5: 1, 2: 0), (5: 1,4: 1, 2: 0) ) + (1: 0) = (1 + 1) + (1 + 1) = 4
find_height(E, k) = ( (10: 0, 4: 1 || 5: 1) + 2: 0 ), (9: 0, 8: 0, 6: 1, 3: 0) + (1: 0) = ( (1 + 1) + (1) ) = 3

if the outer two are TRUE.
sum_only_child_parents(A) = ( (1 && (4,7 <- 6)) <- 3 ) |& (12,14 <- 10) |& (8) = ( 10 + 14 ) = 24
sum_only_child_parents(B) = (), (5: 1 && 4: 1 && 3: 1 *&& 2: 1) |& (1) = (4+3+2+1) = 10
sum_only_child_parents(C) = ( (8,9,4 && 10,11,5) && 2 ) + (6,7 && 3) && (1) = (0) = 0
sum_only_child_parents(D) = ( (4,5 && 2), (5,4 && 2) ) && (1) = (0) = 0
sum_only_child_parents(E) = ( (10,4: 1 || 5: 0) + 2: 1 ), (9: 1, 8: 1, 6: 1, 3: 1) && (1) = ( 4 + 8 + 6 + 3 ) = 21

sum_only_child(A) = ( (1 && (4,7 <- 6)) <- 3 ) |& (12,14 <- 10) + (8) = (12 + 14) + 8 = 34
sum_only_child(B) = (), (5: 1 &+ 4: 1 &+ 3: 1 *&+ 2: 1) + (1) = (5+4+3+2) + 1 = 15
sum_only_child(C) = ( (8,9,4 && 10,11,5) && 2 ) + (6,7 && 3) + (1) = 0 = 0
sum_only_child(D) = ( (4,5 && 2), (5,4 && 2) ) + (1) = 0 = 0
sum_only_child(E) = ( (10: 1 <- 4 && 5) && 2 ), (9: 1 &+ 8: 1 &+ 6: 1 &+ 3: 1) + (1) = ( 10 + 9 + 8 + 6 ) + 1 = 34

# level_min(root, height)
# same as find_height except finding the lowest
# k = 2
# do min in the final part
level_min(A, k) = ( (1: 1, 4,7: 0, 6: 1) <- 3 ) || (12: 0, 14: 1, 10: 0) || (8: 0) = ( (1 || 6) || (14) ) = 1
level_min(B, k) = () || (5: 0, 4: 0, 3: 1, 2: 0) || (1: 0) = (3) = 3
level_min(C, k) = ( (8,9, 4: 1 || 10,11, 5: 1) || 2: 0 ) || (6: 1,7: 1 || 3: 0) || (1: 0) = ( (4 || 5) + (6 || 7) ) = 4
level_min(D, k) = ( (4: 1, 5: 1, 2: 0) || (5: 1,4: 1, 2: 0) ) || (1: 0) = (4 || 5) || (5 || 4) = 4
level_min(E, k) = ( (10: 0, 4: 1 || 5: 1) + 2: 0 ) || (9: 0, 8: 0, 6: 1, 3: 0) || (1: 0) = ( (4 || 5) || (6) ) = 4

# inverse/opposite of checking for only child (parent one)
# full
full(A) = ( (1: True && (4,7 <- 6: True)) <- 3: True ) && (12: False, 14: False <- 10: False) && (8: True) = (True && False && True) = False
full(B) = (), (5: False && 4: False && 3: False *&& 2: False) && (1: False) = (False) && False = False
full(C) = ( (8,9,4 && 10,11,5) && 2 ) + (6,7 && 3) && (1: True) = (True && True) && True = True
full(D) = ( (4,5: True && 2: True), (5,4: True && 2: True) ) && (1: True) = (True && True) && True = True
full(E) = ( (10,4: False && 5: True) && 2: True ) && (9: False, 8: False, 6: False, 3: False) && (1: True) = (False && False) && True = False

# for all of them
same(X, X) = True
same(X, Y) = False

# almost_same(A, B, k)


this works:
9
2 2 3 
2 4 5 
1 8 
0 
2 6 7 
0 
0 
1 9 
0 


	8
   / \
  3   10
 / \    \
1   6    14
   / \   /
  4   7 12

	  8
   / \
  3   2
 / \    \
1   6    5
   / \   /
  4   7 9

8 3
8 2
3 1
3 6
6 4
6 7
2 5
5 9

0 1 
0 2 
1 3 
1 4 
2 7 
4 5 
4 6 
7 8 



