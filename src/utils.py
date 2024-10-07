class UnionFind:
    def __init__(self, n):
        """
        Initialize Union-Find Disjoint Set (UFDS) with n elements.
        """
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.numdisjoint = n

    def find(self, x):
        """
        Find the representative of the set containing x with path compression.
        """
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])  # Path compression
        return self.parents[x]

    def union(self, a, b):
        """
        Union the sets containing a and b.
        """
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return

        # Union by rank
        if self.ranks[root_a] < self.ranks[root_b]:
            self.parents[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]
        else:
            self.parents[root_b] = root_a
            self.sizes[root_a] += self.sizes[root_b]
            if self.ranks[root_a] == self.ranks[root_b]:
                self.ranks[root_a] += 1

        self.numdisjoint -= 1

    def size(self, x):
        """
        Return the size of the set containing x.
        """
        return self.sizes[self.find(x)]
    
    def is_same_set(self, a, b):
        """
        Check if a and b are in the same set.
        """
        return self.find(a) == self.find(b)
    
from math import ceil

def edit_distance_optimized(sequence_a, sequence_b, window_percentage):
    """
    Calculate the edit distance between two sequences using a window of a specified percentage.
    Args:
        sequence_a (list): The first sequence.
        sequence_b (list): The second sequence.
        window_percentage (int): The window size as a percentage of the shorter sequence.
    
    Returns:
        int: The minimum cost to transform sequence_a into sequence_b.
    
    Description:
        This optimized version of the edit distance algorithm uses a window to reduce the time complexity,
        and a memory-efficient approach to store only the necessary information.
    """
    # Swap the sequences for memory efficiency
    if len(sequence_b) > len(sequence_a):
        sequence_a, sequence_b = sequence_b, sequence_a

    len_a = len(sequence_a) + 1
    len_b = len(sequence_b) + 1

    # Calculate the window size based on the window percentage
    window_size = ceil(len(sequence_b) * (window_percentage / 100))

    # Create a dynamic programming table with dimensions 2 x len_b
    dp = [[0] * len_b for _ in range(2)]

    for i in range(1, len_a):
        # Swap the rows for the current and previous iterations
        dp[0] = dp[1][:]
        dp[1][0] = i

        # Calculate the left and right bounds of the window
        left_bound = max(1, i - window_size)
        right_bound = min(len_b, i + window_size + 1)
        
        for j in range(left_bound, right_bound):
            # Calculate the cost of different operations: insert, delete, and replace
            insert = dp[1][j - 1] + 1
            delete = dp[0][j] + 1
            replace = dp[0][j - 1] + (sequence_a[j - 1] != sequence_b[i - 1])
            
            # Choose the minimum cost among the three operations
            dp[1][j] = min(insert, delete, replace)

    # Return the minimum cost to transform sequence_a into sequence_b    
    return dp[1][len_b - 1]