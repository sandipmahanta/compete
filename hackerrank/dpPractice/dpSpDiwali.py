#https://www.hackerrank.com/contests/w14/challenges/superman-celebrates-diwali
def diwali(h, n, input, p):
	build_floor = {}
	building = 0
	for inp in input:
		inp_arr = inp.split()
		l = int(inp_arr[0])
		for i in xrange(1,l+1):
			floor = int(inp_arr[i])
			key = str(building) + '_'	+ str(floor-1)
			if key in build_floor:
				value = build_floor[key]
				build_floor[key] = value + 1
			else :
				build_floor[key] = 1
			
		
		building += 1
	
	M = [0 for x in xrange(h)]
	P = [0 for x in xrange(n)]
	for f in xrange(h):
		#print P
		for b in xrange(n):
			flcount = get_floor_count(build_floor, b, f)
			temp = P[b]
			if f >= p:
				temp = max(temp, M[f-p])

			flres = flcount + temp
			if flres > M[f]:
				M[f] = flres
			
			P[b] = flres
			
	
	#print M
	print M[h-1]

def get_floor_count(build_floor, b, f):
	key = str(b) + '_' + str(f)
	if key in build_floor:
		return build_floor[key]
	
	return 0

def read_input():
	line1 = raw_input()
	line1_arr = line1.split()
	n = int(line1_arr[0])
	h = int(line1_arr[1])
	p = int(line1_arr[2])
	p_arr = []
	for a in xrange(n):
		p_arr.append(raw_input())
		
	diwali(h,n,p_arr, p)

#read_input()
diwali(15,4,["5 1 1 1 4 10","8 9 5 7 7 3 9 8 8","5 9 5 6 4 3","0"],5)
#diwali(10,2,[],2)
