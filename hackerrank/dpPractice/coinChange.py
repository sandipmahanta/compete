#https://www.hackerrank.com/challenges/coin-change

def coinchange(coins, n):
	m = len(coins)
	DP = [[0 for x in xrange(n+1)] for y in xrange(m+1)] 
	for i in xrange(m+1):
		DP[i][0] = 1
	
	for i in xrange(1,m+1):
		for j in xrange(1,n+1):
			DP[i][j] = DP[i-1][j]
			if j - coins[i-1] >= 0:
				DP[i][j] += DP[i][j-coins[i-1]]
			
		
	
	print DP[m][n]



def readinput():
	coinsinput = raw_input()
	coinStr = coinsinput.split(",")
	coins = []
	for c in coinStr:
		coins.append(int(c))
	
	n = int(raw_input())
	coinchange(coins,n)

readinput()
