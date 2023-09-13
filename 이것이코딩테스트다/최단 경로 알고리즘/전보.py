import heapq
import sys
input = sys.stdin.readline
INF =int(1e9) #무한을 의미하는 값

def dijkstra(start):
	q=[]
	#시작 노드로 가기 위한 최단 경로는 0으로 설정, 큐에 삽입
	heapq.heappush(q,(0,start))
	distance[start] = 0
	while q: #큐가 비어있지 않다면
		#가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
		dist, now = heapq.heappop(q)
		#현재 노드가 이미 처리된 적이 있는 노드라면 무시
		if distance[now] < dist:
			continue
		for i in graph[now]:
			cost = dist + i[1]
			#현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0])) #갱신될때마다 갱신정보 업데이트


#노드 개수, 간선 개수,시작노드 입력받기
n,m,start = map(int,input().split())
# 각 노드에 연결되어있는 노드에 대한 정보 담는 리스트 만들기
graph = [[] for i in range(n+1)]
#최단 거리 테이블 모두 무한으로 초기화
distance = [INF] * (n+1)

for _ in range(m):
	x,y,z = map(int, input().split())
	graph[x].append((y,z))

dijkstra(start)

#도달할 수 있는 노드의 개수
count = 0
#도달할 수 있는 노드 중 가장 멀리 있는 노드와의 최단 거리
max_distance = 0

for d in distance:
	#도달할 수 있는 노드인 경우
	if d != 1e9
		count += 1
		max_distance = max(max_distance,d)

#시작 노드 제외해야하므로 count-1출력
print(count-1,max_distance)