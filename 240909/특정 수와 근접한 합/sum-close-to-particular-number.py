"""
문제이해
- 입력 : S,N (2개의 정수)
      : N개의 수   

- N개의 수들 중 정확히 2개를 제외하여 남은 N-2개의 숫자들의 합이 S와 최대한 가까워지도록 하는 프로그램을 작성

- 출력 : S와 S와 가장 가까운 수와의 차를 출력

아이디어
반복문으로 완전 탐색을 통해 가장 가까운 수를 찾아낸다.

for i in range(len(data)): # 입력 N중 첫번쨰 수부터 탐색
    for j in range(i+1, len(data)): # i 다음 요소부터 제거
        for k in range(j+1, len(data)): # j 다음 요소까지 제거 후 모두 탐색



"""

import sys

S, N = map(int, input().split())

data = list(map(int, input().split()))

answer = sys.maxsize

for i in range(len(data)): # 입력 N중 첫번쨰 수부터 탐색, 제거할 첫번째 요소
    for j in range(i+1, len(data)): # i 다음 요소부터 제거, 제거할 두번째 요소
        sum = 0
        for k in range(len(data)): # i,j 를 제거한 요소 덧셈
            if k == i or k == j:
                continue
            sum += data[k]

        sum = abs(N - sum)

        answer = min(answer, sum)
        

print(answer)