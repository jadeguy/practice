# 규칙
# 로또는 주 1회씩 열립니다. 하지만 한 사람이 한 회차에 여러 번 참여할 수도 있습니다.
#
# 번호는 1부터 45까지 있는데요. 주최측에서는 매주 6개의 '일반 당첨 번호'와 1개의 '보너스 번호'를 뽑습니다. 그리고 참가자는 1번 참여할 때마다 서로 다른 번호 6개를 선택합니다.
#
# 당첨 액수는 아래 규칙에 따라 결정됩니다.
#
# 내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치 (10억 원)
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치 (5천만 원)
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치 (100만 원)
# 내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치 (5만 원)
# 내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치 (5천 원)

import random


def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        rnd = random.randint(1, 45)
        if rnd in numbers:
            continue
        else:
            numbers.append(rnd)
    return numbers


def draw_winning_numbers():
    bon = sorted(generate_numbers(6))
    rnd = random.randint(1, 45)
    while rnd in bon:
        rnd = random.radint(1, 45)
        



def count_matching_numbers(a: list, b: list) -> int:
    cnt_mch = 0
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if a[i] == b[j]:
                cnt_mch += 1
    return cnt_mch


def check(a,b):
