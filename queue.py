from collections import deque
for _ in range(int(input())):
    n, m = map(int, input("작업 수 / 작업 번호 : ").split())
    prior = deque(list(map(int,input("우선순위 : ").split())))
    count = 0
    while 1:
        if prior[0] >= max(prior):
            prior.popleft()
            count += 1
            if m == 0:
                print(count)
                break
            m -= 1
        else:
            if m == 0:
                m = len(prior) - 1
            else:
                m -= 1
            prior.append(prior.popleft())