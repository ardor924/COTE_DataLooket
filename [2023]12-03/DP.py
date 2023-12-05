# 풀이
def solution(m, n, puddles):
    all_cases = string_to_number('1,000,000,007')
    memo = dict()                                   # 메모용 딕셔너리
    puddles = {(x, y) for x, y in puddles}         

    # 동적 계획법
    def dp(x, y):     
        # 파라미터 초기화
        result = 0                                     
        
        # 현재 위치가 물에 잠겼다면 실행
        if (x, y) in puddles:   
            return 0
        # 학교에 도착했다면 실행
        if x == m and y == n:   
            return 1   
        # 이미 계산한적이 있는 위치라면 저장된 값을 반환
        if (x, y) in memo:      
            return memo[(x, y)]        
        # 오른쪽으로 이동 가능한 경우
        if x < m:  
            result += dp(x+1, y)  # 오른쪽이동 >  최단경로개수 덧셈
        # 아래로 이동 가능한 경우
        if y < n:  
            result += dp(x, y+1)  # 아래이동 >  최단경로개수 덧셈
            
        # all_cases로 나눈 나머지 반환한 결과를 memo에 저장 
        memo[(x, y)] = result % all_cases  
        return memo[(x, y)]

    return dp(1, 1)


# 문자열입력 -> 숫자반환
def string_to_number(s):
    try:
        result = int(s.replace(',', ''))
        return result
    except ValueError:
        print("입력한 문자열이 올바른 형식이 아닙니다.")
        return None





# 예시
m = 4
n = 3
puddles = [[2, 2]]
result = solution(m, n, puddles)


# 메인실행
if __name__ == "__main__" :
    res = solution(m,n,puddles)
    print(res)