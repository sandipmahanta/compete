#https://www.hackerrank.com/challenges/stockmax

def stock_maximize(prices):
	n = len(prices)
	local_max = [ 0 for x in xrange(n)]
	local_max[n-1] = prices[n-1]
	for i in xrange(n-2,-1,-1):
		if prices[i] > local_max[i+1]:
			local_max[i] = prices[i]
		else:
			local_max[i] = local_max[i+1]	
	
	profit = 0
	share_count = 0
	for i in xrange(n):		
		if prices[i] < local_max[i]:
			profit -= prices[i]
			share_count += 1
		else :
			profit += share_count * prices[i]
			share_count = 0
		
	
	print profit
		

#stock_maximize([1,3,1,2])
#stock_maximize([5,4,3,2])
#stock_maximize([1,2,3,4])


def read_input():
	t = int(raw_input())
	input = []
	for i in xrange(t):
		raw_input()
		input.append(raw_input())
	
	for input_str in input:
		str_array = input_str.split()
		prices = []
		for price_str in str_array:
			prices.append(int(price_str))
		
		stock_maximize(prices)
	

read_input()
