// 92.

package problem92

func reverseString(s []byte) {
	left := 0
	right := len(s) - 1
	for right > left {
		s[right], s[left] = s[left], s[right]
		right -= 1
		left += 1
	}
}
