// 446.

package problem446

func numberOfMatches(n int) int {
	matchCount := 0
	for n > 1 {
		if n%2 == 0 {
			n = n / 2
			matchCount += n
		} else {
			matchCount += (n - 1) / 2
			n = (n-1)/2 + 1
		}
	}
	return matchCount
}
