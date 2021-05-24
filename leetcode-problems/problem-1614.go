// 1614.

package problem1614

func maxDepth(s string) int {
	depth := 0
	maxDepth := 0
	c := ""
	for i := 0; i < len(s); i++ {
		c = string(s[i])
		if c == "(" {
			depth++
			if depth > maxDepth {
				maxDepth = depth
			}
		} else if c == ")" {
			depth--
		}
	}
	return maxDepth
}
