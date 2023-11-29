'''
경로탐색문제로써 DFS , Stack으로 문제 풀이진행
'''

# 문제풀이
def solution(tickets):
    # 딕셔너리 초기화
    routes = {}

    # 딕셔너리 알파벳순 정렬(티켓,루트의 항공정보)
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)

    # 스택 초기값세팅 "ICN"국제공항
    stack = ["ICN"]  
    visited_path = []  
    
    # 스택이 빌때까지 반복
    while stack:
        stack_top = stack[-1]

        # 갈수있는 공항이 없거나, 항공권을 모두 사용한 경우
        if stack_top not in routes or len(routes[stack_top]) == 0:
            visited_path.append(stack.pop())
            
        # 미사용 항공권이 있는 경우    
        else:  
            stack.append(routes[stack_top].pop())
            
    # 역순으로 결과 반환
    return visited_path[::-1]  


# 예시
tickets1 = [
                ["ICN", "JFK"],
                ["HND", "IAD"],
                ["JFK", "HND"]
            ]

tickets2 = [
                ["ICN", "SFO"],
                ["ICN", "ATL"],
                ["FCO", "ATL"],
                ["ATL", "ICN"],
                ["ATL","FCO"]
            ]

tickets3 = [
                ["CDG", "FCO"],
                ["LHR", "MUC"],
                ["MUC", "CDG"],
                ["LHR", "FCO"]
            ]


if __name__ == "__main__" :
    res1 = solution(tickets1)
    res2 = solution(tickets2)
    res3 = solution(tickets3)
    print(res1)
    print(res2)
    print(res3)