package disjointset

// QuickFind implements a disjoint-set data structure with O(1) find operation and O(n) union operation
type QuickUnion struct {
	root []int
}

func NewQuickUnion(n int) QuickFind {
	root := make([]int, n)
	for i := 0; i < n; i++ {
		root[i] = i
	}
	return QuickFind{root: root}
}

func (qu QuickUnion) Find(x int) int {
	for {
		if x == qu.root[x] {
			break
		}
		x = qu.root[x]
	}
	return x
}

func (qu QuickUnion) Union(x int, y int) {
	xRoot := qu.Find(x)
	yRoot := qu.Find(y)
	if yRoot != xRoot {
		qu.root[yRoot] = xRoot
	}
}

func (qu QuickUnion) Connected(x int, y int) bool {
	return qu.Find(x) == qu.Find(y)
}
