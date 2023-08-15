package main

import (
	"fmt"

	"github.com/awliu2/learndsa/disjointset"
)

func main() {
	ds := disjointset.NewQuickUnion(10)
	// ds := disjointset.NewQuickFind(10)
	// 1-2-5-6-7 3-8-9 4
	ds.Union(1, 2)
	ds.Union(2, 5)
	ds.Union(5, 6)
	ds.Union(6, 7)
	ds.Union(3, 8)
	ds.Union(8, 9)
	fmt.Println(ds.Connected(1, 5)) // true
	fmt.Println(ds.Connected(5, 7)) // true
	fmt.Println(ds.Connected(4, 9)) // false

	// 1-2-5-6-7 3-8-9-4
	ds.Union(9, 4)
	print(ds.Connected(4, 9)) // true
}
