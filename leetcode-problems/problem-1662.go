// 1662.

package problem1662

import "strings"

func arrayStringsAreEqual(word1 []string, word2 []string) bool {
	completeWord1 := strings.Join(word1, "")
	completeWord2 := strings.Join(word2, "")
	return completeWord1 == completeWord2
}
