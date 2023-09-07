n,m = list(map(int,input().split(' ')))

array = list(map(int, input().split()))

start = 0 
end = max(array)

result = 0

while(start<=end) :
	total = 0
	mid = (start + end) // 2
	for x in array:
		if x>mid:
			total +=  x-mid
	#떡의 양이 부족한 경우 더 많이 자르기(왼쪽부분탐색)
	if total < m:
		end = mid - 1
	#떡의 양이 충분한 경우 덜 자르기(오른쪽부분탐색)
	else:
		result = mid
		start = mid+1