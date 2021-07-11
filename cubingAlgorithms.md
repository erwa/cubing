### Skewb

* default: http://meep.cubing.net/skewb-fcn.html
* Strong: http://sarah.cubing.net/skewb/my-method#section/notation-and-algs

### CLL/EG

Pi (RFU, LUF, BUL, BRU): [Strong] R' F R F'
Peanut (FLU, RUB): [Strong] R' F R F' y R' F R F'
Diag: L U' R' U R' L R' L
Diag-Peanut (LUF, BRU): U R U' R' L' U' L U
Diag-Pi (LFD, RDF, UFL, URF): L D R D U D' R D

Last 4 centers:
[USE SETUP TURNS for 3 and 4 unsolved centers cases!]
U (R -> L -> B -> R): [Strong] R' F R F' y2 R' F R F' [y2]
Z (F<->L, R<->B): R L' U' L U L R L' R  6/9/14
H (U<->D, R<->L): R U' L U' R' L U' L  6/9/14


### 2x2x2

Triple Sune:

```
 `| - F' (R U R' U') R' F R
 |` - F (L' U' L U) L F' L'
```


### 3x3x3

F2L:
Edge solved, corner in slot, twisted cc, at DFR: (R U2) (R U R') U (R U2 R2)
Edge solved, corner in slot, twisted cc, at DFL: (L2 U2) (L U L') (U L U2 L)
Edge solved, corner in slot, twisted c, at DFR: (R2 U2 R' U' R U') (R' U2 R')
Edge solved, corner in slot, twisted c, at DFL: (L' U2) (L' U' L) (U' L' U2 L2)


OLL:

Only edges flipped:

* 2 adjacent edges flipped (UB and UL): (M' U M) U2 (M' U M)
* 2 opposite edges flipped (UB and UF): (R U R' U') (M' U R U' r')
* 4-edge flipper: (r' R U) (R U R' U') (r2 R2' U R U' r')


Only corners flipped:

* UFL flipped cc, UBR flipped c: x U R' U' L U R U' L' x'
* UFR flipped cc, UBL flipped c: x U' L U R' U' L' U R x'
* Diagonal stripe, strips on B and L: (R U R') U (R' F R F') U2 (R' F R F')
* Triangle, bar on B: F (R U R') (U y') (R' U2) (R' F R F')
* Triangle, strips on L and R: (r' R U) (R U R' U') (r R2' F R F')
* Dot, bar on L: (F R U R' U' F') f (R U R' U' f')
* Dot, bar on L and R: (R U2' R2' F R F') U2 (R' F R F')

Bad I (hold sideways): F (R U R' U') R F' (r U R' U') r'
Good I (vertical, bar on right): (R' U' R U' R' U) y' (R' U R B)

U: R2 D' R U2 R' D R U2 R
Stripes: z' (U' R U2 r' U) L2 (U' r U2 R' U) z
L, 2 pairs: F U R U' R2 F' R U R U' R'
Y: R U R' U' R' F R2 U R' U' F'


CLL:
Triple Sune position: (F, U, F', U, F, U2), R2, B', R', B, R', F' - (...) is really a Sune
Two Sune: (R, U2, R', U', R, U', [R2), U2, R, U, R', U, R] - really two Antisunes
Two AntiSune: (R', U', R, U', R', U2, [R2), U, R', U, R, U2, R'] - really two Sunes
OLL complete, diagonal corners swapped: R2 D L' B L D' R2 U' F' U' F

PLL:

A1: x R' U R' D2 R U' R' D2 R2 x'

A2:
* x' R U' R D2 R' U R D2 R2 x
* (R B' R) F2 (R' B R) F2 R2

F:
* (R U' R' U R2') y (R U R' U') x (U' R' U) (R U2')  3/27/10
* (R' U R U' R2' F' U' F) (U R U') x' (R2 U' R' U)

G1: (R U R') y' (R2 u' R) (U' R' U R' u R2)

G2:
* (R' U' R) y (R2 u R') (U R U' R u' R2)
* (D R' U' R U D') (R2 U R') (U R U' R U' R2' U') - "French G"

G3:
* (R2 u' R U') (R U R' u R2) y (R U' R') - .``\. starts with right hand thumb on B face
* one-handed (pair at UR and URB): R' U' R z x' U2 r U' R U R' U r' U2

G4 (pair at UF and UFR):
* (R2 u R') (U R' U' R u') R2 y' (R' U R)
* D' (R2 U R') (U R' U' R U' R2 U' D) (R' U R U) - "French G"
* one-handed (pair at RB and RBU): U2 r U' R U' R' U r' U2 x' U' R U

J1:
* (R U R' F' R) (U R' U') (R' F R2 U' R' U')
* R' U L U' R U2 L' U L U2 L'

J2:
* x' (R' F' R) (U R' F' R) (F R U') (R2 F R F)
* L U' R' U L' U2 R U' R' U2 R

N1:
* (z) R (U R' D R2 U' R D')2 (z')  8/13/16
* (R U' R' U l U) (F U' R' F' R U') (R U R' F R')

N2:
* (z) R' (U' R D' R2' U R' D)2 (z')  8/13/16
* (R' U R U' R' F') (U' F R U R') (F R') (F' R U' R)

R1: (R' U2) (R U2) (R' F R U R' U') (R' F' R2 U')

R2: (R2 B' R' U') (R' U R B R' U2) (R U2) (R' U') - /| starts with right hand thumb on D face

T: (R, U, R', U') (R', F, R2, U') (R', U', R, U, R', F')

U1: R2 U R U R' U' R' U' R' U R'

V:
* (R' U R' U') y (R' F' R2 U') (R' U R') (F R F)
* (R' U R U' R' f' U') (R U2 R' U' R U' R' f R)  7/9/21

Y:
* (F R U') (R' U' R U) (R' F') (R U R' U') (R' F R F') - keep your left hand thumb light while gripping
* (R2 U' R' U R U') z'y' (L' U') (R U' R') (U' L U)
* F R U' R' U' R U y R U R' B' R U' R2

Z:
* M2 U M2 U M' U2 M2 U2 M' U2 - swaps (UF UR) (UL UB)
* x' (R U' R' U) (D R' D U') (R' U R z') (R2' F)
* (U R' U' R U' R) (U R U' R' U R) U (R2 U' R' U)

One-handed:
Left-handed:
Y: z' (U' U' L' U' L U L') y' (L' U' R U' R' U' L U)

Right-handed:
A1: x' L' U L' D2 L U' L' D2 L2
A2: x' U L' U R2 U' L U R2 U2
E: x U' L U R' U' L' U R2 z2 U R' U' L' U R U' x'
F: L U' L' U L2 F U F' U' L' U L2 x' U L U' x
G1: L U L' y z' U2 l' U L' U' L U' l U2 z
G2: L' U' L y L2 u L' U L U' L D' B2
G3: L2 D' y' L U' L U L' u L2 x y' U L' U'
G4: L2 u L' U L' U' L D' y' L2 y' L' U L
H:
 L' R' U2 L l U z' L x U2 L' R'
 L R U2 L' R' y' L' R' U2 L R
J1:
 L' U R U' L U2 R' U R U2 R'
 U L U' R U2 L' U L U2 R' L'
J2: L' U' L F L' U' L U L F' L2 U L U
N1: L U' L' U L F U F' L' U' L x U' L U L' x' U L'
N2: L' U L U' L' x' U' F' U L F L' U L' U' L F' L
Y: (U, U, R, U, R', U', R) y (R, U, L', U, L, U, R', U')

Blindfolded:
Bruno CO:
 F (R U R' U') (R U R' U') F' (R U R' U') r (R' U R U' r')
 R' U' ((R' F R F') (R U' R' U))*2 U R
Triple Sune:
 F' R D2 R' F U2 F' R D2 R' F U2
 (R U2) (R' U2) (R' U') (R U') (R' U2 R) U2 (R U R' U)
 (R' U R2' U' R2 U' R' U) (R U R' U') (R2' U' R2 U)
Sune:
 R' U L U' u' R2 u R2 U2 L' U R' U
 L U' R' U u L2 u' L2 U2 R U' L U'

Patterns:
Cube in a cube: (R' F' R U R U' R' F x y') * 4
R F' L' U B2 U' L F L U2 R' L' F2 L' F2 U2  6/6/08


Big Cubes:

G-Permutations:
G1: z' U L U' x U2 l' U L' U' L U' l U2  12/20/09
G2: z U' R' U x U2 r U' R U R' U r' U2  12/20/09
G3: z' U2 l' U L' U L U' l U2 B L' B'  12/20/09
G4: x U2 r U' R U' R' U r' U2 x' U' R U  12/20/09

4x4x4 Last Two Pairs of Dedges:
 Hold at FR and BR: (Uu)' R U R' F R' F' R (Uu)

Orientation Parity:
 Hold offending pair at UF: (Rr)2 B2 U2 (Ll) U2 (Rr)' U2 (Rr) U2 F2 (Rr) F2 (Ll)' B2 (Rr)2
 Hold offending pair at UR: (Rw' U) (R U Rw') (U2 Rw') (U2 Rw') (U2 Rw2) (U R' U' Rw2 U' R' U Rw')

Permutation Parity (4x4x4): (Uu)2 (Rr)2 U2 r2 U2 (Rr)2 (Uu)2
Adjacent Dedge Swap (4x4x4, UF<->UR):
 R' U R U' r2 U2 r2 Uw2 r2 Uw2 U' R' U' R
 (x R2 F') (Uw2 Rw2) (U2 r2 U2) (Rw2 Uw2) (F R2 x')

Dedge Swap (5x5x5+): (Rr)2 (Bb)2 U2 r2 U2 (Bb)2 (Rr)2
Dedge Swap (5x5x5+) - UF and UB: F2 Rw U2 Rw' x2 y' R2 U2 R2' x z Rw U2 Rw'  8/22/09
Dedge Swap (5x5x5+) - UB and DF: Rw U2 Rw' x2 y' R2 U2 R2' x z Rw U2 Rw'  12/13/09
Dedge Swap (5x5x5+) - UF and DF: U2 Rw U2 Rw' x2 y' R2 U2 R2' x z Rw U2 Rw'  8/22/09
Dedge Swap (5x5x5+) - UFl and UBl need to swap:
 [(Rr)' U2]*2 B2 (Rr)' B2 (Ll) U2 (Ll)' U2 (Rr)2  9/21/09
Checkerboard 1 (5x5x5+) (right two tredges go together):
 [(Rr) U2 (Rr)2] [U2 (Rr)'] U2 [(Rr) U2 (Rr)'] [U2 (Rr)2] [U2 (Rr)]  9/21/09
Checkerboard 2 (5x5x5+) (left two tredges go together):
 [(Rr)' U2 (Rr)2] U2 [(Rr) U2 (Rr)'] [U2 (Rr)] [U2 (Rr)2] [U2 (Rr)']  9/21/09

Double edge flip (5x5x5) - FL and FR: (Uu)' (Dd) R U R' F R' F' R (Dd)' (Uu)  8/19/09
Double Parity (5x5x5) - UFl, UFr and UB same color: Rw2 F2 Rw U2 Rw U2 x U2 Rw U2 Rw' U2 Rw U2 Rw2  8/19/09

Center Cyclers:
r2 u2 r2 u2
l2 F r2 F' l2 F r2 F'
r2 B2 r'  (fb') r B2 r' (f'b) r'
r2 B2 r' f r B2 r' f' r'
r2 (du') R (du') r2 (d'u) R' (d'u)
r' (d'u) r U2 r' (du') r U2
(l r') d2 (l' r) U' D' (l r') d2 (l' r) U D


Square-1:
Getting back into a cube shape:
- http://www.jaapsch.net/puzzles/square1.htm#s1m1
- Gather all 6 corners in one layer. Learn 5 cases.
4-4: /(2,2)/(0,-1)/(3,3)/
5-3 (5 in top-left, 3 in bottom-right):
  /(-4,0)/(-1,-2)/(3,-4)/(2,1)/(0,3)/
  /(-4,0)/(-1,-2)/(-3,2)/(-2,-1)/(0,-3)/[(-1,1)]
6-2 (6 on top): /(-4,-2)/(-1,4),(-3,0)/
6-2 (6 on bottom): /(-2,-4)/(-1,4)/(0,-3)/
7-1 (6 on left + top and right): /(2,0)/(3,2)/(3,-2)/(2,1)/(0,3)/
8-0: /(2,4)/(1,2)/(-3,-3)/

Separating edges:
 UB, DF: (0,-1) / (-3,0) / (4,1) / (-4,-1) / (3,0) / [(0,1)]
 UB, UF, DF, DB: (1,0) / (-1,-1) / [(0,1)]
 UL, UB, DB, DR: (1,0) / (-3,0) / (-1,-1) / (4,1) / [(-1,0)]
 UB, UF, DF, DR: (0,-1) / (3,0) / (-3,0) / (1,-2) / (0,3) / [(-1,0)]
 UL, UB, UR, DF, DR, DB:
   (0,-1) / (1,4) / (-1,-4) / (-3,0) / (4,1) / (-1,0)

Fix parity:
# https://www.speedsolving.com/forum/showthread.php?9512-Square-1-Parity-Algs
On top (diag corner swap on top (UFL UBR), H on bottom):
  /(3,3)/(-1,0)/(-4,2)/(-2,4)/(0,1)/(3,3)/[(0,6)]
On bottom (H on top, diag corner swap on bottom (DFL DBR)):
  /(-3,-3)/(0,1)/(-2,4)/(-4,2)/(-1,0)/(-3,-3)/[(6,0)]
Both (1 edge swap in each layer (UB UF, DF DB)): (1,0) / (5,-1) / (-5,1) / [(5,0)]

### Corner Permutation ###
Adjacent corner swap in both layers (UFL UFR, UL UF, DFL DFR, DL DF): /(-3,0)/(3,3)/(0,-3)/
Diagonal corner swap in both layers (UFL UBR, UL UR, DFL DBR, DL DR): /(-3,3)/(3,-3)/

Adjacent swap on top (UFR UBR, UF UR), diagonal swap on bottom (DFR DBL, DF DB): /(0,-3)/(0,3)/(0,-3)/(0,3)/
Diagonal swap on top (UFL UBR, UL UR), adjacent swap on bottom (DFR DBR, DF DR): /(-3,0)/(3,0)/(-3,0)/(3,0)/

J (UFR UFL, UL UF): / (3,-3) / (3,0) / (-3,0) / (0,3) / (-3,0) / [(3,0)]
J bottom (DFL DFR, DL DF): / (3,-3) / (0,3) / (-3,0) / (3,0) / (-3,0) / [(0,3)]

N (UBR UFL, UR UL): / (3,3) / (3,0) / (3,3) / (3,0) / (3,3) / [(3,0)]
N bottom (DFR DBL, DF DB): / (3,3) / (0,3) / (3,3) / (0,3) / (3,3) //[(0,3)]

### Edge Permutation ###
U1 (UR UL UB): / (3,0) / (1,0) / (0,-3) / (-1,0) / (-3,0) / (1,0) / (0,3) / (-1,0)
U2 (UR UB UL): (1,0) / (0,-3) / (-1,0) / (3,0) / (1,0) / (0,3) / (-1,0) / (-3,0) /

U1 bottom (DR DL DB):
  / (0,-3) / (0,-1) / (3,0) / (0,1) / (0,3) / (0,-1) / (-3,0) / (0,1)
U2 bottom (DR DB DL):
  (0,-1) / (3,0) / (0,1) / (0,-3) / (0,-1) / (-3,0) / (0,1) / (0,3) /

H: / (3,-3) / (3,-3) / (0,1) / (-3,3) / (-3,3) / [(-1,0)]
H bottom: / (3,-3) / (3,-3) / (-1,0) / (-3,3) / (-3,3) / [(0,1)]

Double H-perm: (1,0) / (5,-1) / (3,3) / (1,1) / (3,-3) / (5,0)

Z: (UF UL, UR UB): / (3,3) / (0,3) / (1,1) / (-1,-4) / (-3,-3) /
Z bottom (DF DL, DR DB): / (-3,-3) / (-3,0) / (-1,-1) / (4, 1) / (3,3) /

Parity: (UR UL): / (3,3) / (-1,0) / (2,-4) / (4,-2) / (0,-2) / (-4,2) / (1,-5) / (3,0) / (3,3) / [(3,0)]

Move Sequence Execution Speeds (Average):

Sune 2: 1.08  8/20/05
Sune 1: 1.18  8/20/05
Antisune 1: 1.20  8/20/05
Antisune 2: 1.26  8/20/05
Niklas 1: 1.36  8/20/05
Niklas 2: 1.38  8/20/05
Double Sune: 1.69  8/20/05
Bruno 2: 1.76  10/10/05
Double Antisune: 1.88  8/20/05
U1: 2.02
Triple Sune: 2.12  8/20/05
T: 2.13  10/21/05
Bruno 1: 2.13  8/20/05
Triple Antisune: 2.14  8/20/05
J2: 2.15  11/27/05
Rune 1: 2.20  8/20/05
J1: 2.20  11/27/05
U2: 2.21  7/28/05
Z: 2.23  8/1/05
H: 2.24  8/1/05
A2: 2.43  8/3/05
Rune 2: 2.47  8/20/05
A1: 2.48  8/19/05
Y: 2.61  8/19/05
G4: 2.69  8/19/05
G1: 2.71  8/3/05
R1: 2.73  8/3/05
G3: 2.86  8/19/05
N2: 2.87  10/21/05
R2: 2.87  8/19/05
N1: 2.88  10/22/05
V: 2.89  10/22/05
E: 2.90  8/19/05
F: 2.95  8/19/05
G2: 2.96  10/22/05
