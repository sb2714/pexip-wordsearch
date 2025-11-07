# WordSearch - Pexip take home

Python implementation of a WordSearch class supporting horizontal (left to right)
and vertical (top to bottom) substring detection. Note this does not support word wrapping around edges.

## Structure
- `src/wordsearch.py` - implementation
- `src/tests` - 3 test cases / examples of usage

## Assumptions
1. word length between 4 and 20 (incl) characters
2. large grids
3. time complexity concerns
4. no wrapping - though this can be included fairly easily
5. top to bottom / left to right only

## Solution
- want to exploit bounds on word length: use hashing, prefix hashing ((polynomial in p) mod m, for m,p prime) in particular
- maximising for runtime efficiency: perhaps use precomputation, assuming there will be many queries
- again, does not support wrapping

Choice of modulus M results in probability of collision (failure) 1/M, can use multiple hashes with moduli M_1, ..., M_j
for probability of failure (M_1 ... M_j)^-1

In our solution we have kept j = 1, for simplicity, this may result in some collisions for especially large grids and words.

## Complexity
Let n be the number of rows and l be the maximum word length (min(n, 20)). Then
- Row/column construction: O(n^2)
- Prefix hash computation: O(l\*n^2)  

so initialisation is O(l\*n^2) (= O(n^2) for fixed max word length)
- Computing the hash of a word is O(l) and hashtable lookup is O(1)

so querying is O(l) (= O(1) for fixed max word length) after initialisation

## Multi-core situation
- compute hashes of the different rows and columns in parallel
- querying can be parallelised
- may be able to make some of the modular arithmetic more efficient