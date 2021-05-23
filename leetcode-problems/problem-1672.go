// 1672.

package problem1672

func maximumWealth(accounts [][]int) int {
	wealthiestFortune := 0
	currentFortune := 0
	for i := 0; i < len(accounts); i++ {
		for j := 0; j < len(accounts[i]); j++ {
			currentFortune += accounts[i][j]
		}
		if currentFortune > wealthiestFortune {
			wealthiestFortune = currentFortune
		}
		currentFortune = 0
	}
	return wealthiestFortune
}
