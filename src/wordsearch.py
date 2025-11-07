"""

key information:
1. word length between 4 and 20 (incl) characters
2. large grids
3. time/space complexity concerns
4. no wrapping **UNSURE OF THIS MAYBE COME BACK TO THIS**
5. top to bottom / left to right only
6. no tricks - **WILL NOT PAY CARE TO INVALID INPUT CASES**

solution:
- want to exploit bounds on word length: use hashing, prefix hashing ((polynomial in p) mod m, for m,p prime) in particular
- maximising for runtime efficiency: perhaps use precomputation, assuming there will be many queries

choice of modulus M results in probability of collision (failure) 1/M, can use multiple hashes with moduli M_1, ..., M_j
for probability of failure (M_1 ... M_j)^-1

multi core solution:

----

"""
import math

base = 31  # good enough for 26 characters
modulus = int(1e9 + 7)  # could still result in collisions, probability 1/M


class WordSearch:
    N = 0  # keep track of number of characters in grid
    min_length = 4
    max_length = 20
    rows = ""
    cols = ""
    powers = []  # powers of base mod modulus
    sets = {}

    def __init__(self, grid: str):
        # validation
        if not isinstance(grid, str):
            raise TypeError("grid must be a string")

        self.N = len(grid)
        if self.N == 0:
            raise ValueError("grid must not be empty")

        n = int(math.isqrt(self.N))

        if n * n != self.N:
            raise ValueError("grid length is not a perfect square")

        self.max_length = min(self.max_length, n)  # fix to length of row/col

        self.rows = [grid[i * n:(i + 1) * n] for i in range(n)]
        self.cols = ["".join(grid[i + j * n] for j in range(n)) for i in range(n)]

        self.powers = [1] * (self.max_length + 1)

        for i in range(1, self.max_length + 1):
            self.powers[i] = (self.powers[i - 1] * base) % modulus

        self.sets = {i: set() for i in range(self.min_length, self.max_length + 1)}
        # could have sample hash dictionary for verification

        if n >= self.min_length:  # don't bother if row length is too small to contain words
            self.precompute()

    @staticmethod
    def prefix_hash(s: str):
        """
        pref[k] = hash(s[:k]) with pref[0]=0
        then hash(s[i:i+l]) = (pref[i+l] - pref[i]*base^l) % modulus
        """
        pref = [0] * (len(s) + 1)
        for i, ch in enumerate(s, start=1):
            x = ord(ch) - ord('a') + 1
            pref[i] = (pref[i - 1] * base + x) % modulus
        return pref

    def precompute(self):
        for r, s in enumerate(self.rows):
            if not s:  # empty
                continue
            pref = self.prefix_hash(s)
            for l in range(self.min_length, min(len(s), self.max_length) + 1):  # words of length l
                hs = self.sets[l]  # hash set for words of length l
                for i in range(0, len(s) - l + 1):
                    if i == 0:
                        new_hash = pref[l]
                    else:
                        new_hash = (pref[i + l] - pref[i] * self.powers[l]) % modulus
                    if new_hash < 0:
                        new_hash += modulus
                    hs.add(new_hash)

        for c, s in enumerate(self.cols):
            if not s:  # empty
                continue
            pref = self.prefix_hash(s)
            for l in range(self.min_length, min(len(s), self.max_length) + 1):  # words of length l
                hs = self.sets[l]  # hash set for words of length l
                for i in range(0, len(s) - l + 1):  # i is start position of word
                    if i == 0:
                        new_hash = pref[l]
                    else:
                        new_hash = (pref[i + l] - pref[i] * self.powers[l]) % modulus
                    if new_hash < 0:
                        new_hash += modulus
                    hs.add(new_hash)

    def is_present(self, word: str) -> bool:
        if not isinstance(word, str):
            raise TypeError("word must be a string")

        l = len(word)

        if l > self.max_length or l < self.min_length:
            return False

        for i in word:
            if not ('a' <= i <= 'z'):  # only consider lowercase letters
                return False

        word_hash = self.prefix_hash(word)[-1]

        return word_hash in self.sets[l]
