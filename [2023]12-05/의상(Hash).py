# 모듈 import
from collections import Counter

# 조합계산함수
def calculate_combinations(acc, count):
    return acc * (count + 1)

# 문제풀이
def solution(clothes):
    count = Counter()
    total_combinations = 1
    
    # 의상 종류별 개수 카운트
    for clothe_name, clothe_type in clothes:
        count[clothe_type] += 1
        print('clothe_name:',clothe_name)
        print('clothe_type:',clothe_type)
    

    # 입거나,입지않을수 있는 모든조합수 반환
    for value in count.values():
        total_combinations *= (value + 1)

    # 모든 종류에서 입지 않는 경우는 제외하고 반환
    answer = total_combinations - 1
    return answer





# 매개변수 예시
clothes1 = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes2 = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	
clothes3 = [["black_sunglasses", "face"], ["blue_jean", "trousers"], ["white hoodie", "top"]]	


# 메인실행
if __name__ == "__main__" :
    res1 = solution(clothes1)
    res2 = solution(clothes2)
    res3 = solution(clothes3)
    print(res1)
    print(res2)
    print(res3)