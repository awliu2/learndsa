class QuickFind:
    """
    QuickFind implements a disjoint-set data structure with O(1) find operation and O(n) union operation
    
    find(x) returns the parent of node x

    union(x, y) updates the disjoint set, setting x and y to the same root node.
    """
    def __init__(self, n):
        self.root = list(range(n))

    def find(self, x) -> int:
        return self.root[x]
    
    def union(self, x, y) -> None:
        # set root of y, to root of x always
        # update any occurances of root_y to root_x
        root_x = self.find(x)
        root_y = self.find(y)
        if root_y != root_x:
            for i, parent in enumerate(self.root):
                if (parent == root_y):
                    self.root[i] = root_x
    
    def connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)

# Test Case
ds = QuickFind(10)
# 1-2-5-6-7 3-8-9 4
ds.union(1, 2)
ds.union(2, 5)
ds.union(5, 6)
ds.union(6, 7)
ds.union(3, 8)
ds.union(8, 9)
print(ds.connected(1, 5))  # true
print(ds.connected(5, 7))  # true
print(ds.connected(4, 9))  # false

# 1-2-5-6-7 3-8-9-4
ds.union(9, 4)
print(ds.connected(4, 9))  # true
