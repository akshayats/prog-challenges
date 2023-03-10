When you are looking back in old editions of the New in Chess magazine, you find loads of chess puzzles. Unfortunately, you realize that it was way too long since you played chess. Even trivial puzzles such as finding a mate in one now far exceed your ability.

But, perseverance is the key to success. You realize that you can instead use your new-found algorithmic skills to solve the problem by coding a program to find the winning move.

You will be given a chess board, which satisfy:

    No player may castle.

    No player can perform an en passant1

    The board is a valid chess position.

    White can mate black in a single, unique move.

Write a program to output the move that white should play to mate black.
Input

The board is given as a

grid of letters. The first line is rank 8 on the chess board, and the last row is rank 1. The first column is the a-file, and the last column the h-file.

Each character represents a piece as follows:

P

    white pawn
N

    white knight
B

    white bishop
R

    white rook
Q

    white queen
K

    white king
p

    black pawn
n

    black knight
b

    black bishop
r

    black rook
q

    black queen
k

    black king
.

    empty square

Output

Output a move on the form a1b2, where a1 is the square to move a piece from (written as the file, a-h, followed by the rank, 1-8) and b2 is the square to move the piece to.
Sample Input 1 	Sample Output 1

rn...q.b
pb..pPkp
.p......
..ppN..p
...P....
..NB....
PPPQ.PP.
..KR....

	

d2g5

Sample Input 2 	Sample Output 2

..kr...r
p..n..pp
.p.Bnp..
....p...
........
........
PPP..PPP
...RKB.R

	

f1a6

Sample Input 3 	Sample Output 3

rnbq..kr
.p.n..pp
p...p...
...pP...
......Q.
B.PB....
P.P..PPP
R....RK.

	

g4e6

Sample Input 4 	Sample Output 4

r.bqkb.r
pp.npppp
.....n..
.....N..
...PN...
........
PPPBQPPP
R...KB.R

	

e4d6

Sample Input 5 	Sample Output 5

........
.....p..
...p....
b...Q.K.
k.nq....
p..NR..r
..P..P..
R..Bn...

	

e5e8

Sample Input 6 	Sample Output 6

.rbq..r.
p.Pk.K.b
.P.bnp..
..n....p
........
........
....p...
...R....

	

c7b8

Footnotes

    If you are not aware of this special pawn rule, do not worry ??? knowledge of it is irrelevant with regard to the problem.

