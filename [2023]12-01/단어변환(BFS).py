from collections import deque

# 두 단어가 한 글자만 다른지 확인하는 함수
def can_change(word1, word2):
    return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1

# bfs로 최단거리를 리턴
def bfs(begin, target, words):
    # 방문한 단어,거리를 딕셔너리에 저장
    visited, q = {begin: 0}, deque([begin])

    while q:
        current = q.popleft()
        # 현재 단어와 한 글자만 다른 단어들을 선택하여 큐에 추가
        for word in [w for w in words if w not in visited and can_change(current, w)]:
            visited[word] = visited[current] + 1
            q.append(word)

    # 목표 단어에 도달한 거리 반환, 없으면 0 반환
    return visited.get(target, 0)

# 주어진 문제를 해결하는 함수
def solution(begin, target, words):
    # 목표 단어가 단어 리스트에 없으면 0 반환
    return bfs(begin, target, words) if target in words else 0




# 예시
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

# 메인실행
if __name__ == "__main__" :
    res = solution(begin=begin,target=target,words=words)
    print(res)