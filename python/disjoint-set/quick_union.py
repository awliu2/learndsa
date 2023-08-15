class QuickUnion:
    def __init__(self, n):
        self.root = list(range(n))
    
    def find(self, x):
        # recursively travel along parent nodes until a root node is found
        # characteristic of disjoint sets: root nodes are guaranteed to be their own parent, 
        # e.g self.root[root_node] = root_node
        while x != self.root[x]:
            x = self.root[x]
        return x

    def union(self, x, y):
        root_x = self.root[x]
        root_y = self.root[y]
        # quick union sets root_y's parent node to root_x
        # thus we don't need to alter any other nodes as QuickFind version of disjoint set does 
        if root_y != root_x:
            self.root[root_y] = root_x
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

# Test Case
ds = QuickUnion(10)
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
