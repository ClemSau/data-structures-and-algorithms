// 1773.

package problem1773

func countMatches(items [][]string, ruleKey string, ruleValue string) int {
	count := 0
	for i := 0; i < len(items); i++ {
		if ruleKey == "type" {
			if items[i][0] == ruleValue {
				count++
			}
		} else if ruleKey == "color" {
			if items[i][1] == ruleValue {
				count++
			}
		} else {
			if items[i][2] == ruleValue {
				count++
			}
		}
	}
	return count
}
