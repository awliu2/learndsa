package disjointset

// QuickFind implements a disjoint-set data structure with O(1) find operation and O(n) union operation
type QuickFind struct {
	root []int
}

func NewQuickFind(n int) QuickFind {
	root := make([]int, n)
	for i := 0; i < n; i++ {
		root[i] = i
	}
	return QuickFind{root: root}
}

func (qf QuickFind) Find(x int) int {
	return qf.root[x]
}

func (qf QuickFind) Union(x int, y int) {
	xRoot := qf.Find(x)
	yRoot := qf.Find(y)
	if yRoot != xRoot {
		for i := range qf.root {
			if qf.root[i] == yRoot {
				qf.root[i] = xRoot
			}
		}
	}
}

func (qf QuickFind) Connected(x int, y int) bool {
	return qf.Find(x) == qf.Find(y)
}
