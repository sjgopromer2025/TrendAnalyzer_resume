import itertools

# 색상 리스트
# colors = [
#     "그레이", "네이비", "딥그린", "라이트 브라운",
#     "레드", "머스타드", "베이지", "블랙",
#     "블루", "아이보리", "카라멜 브라운"
# ]
colors = ["베이지", "브라운", "아이보리"]

# 색상 조합 생성 (중복 허용)
combinations = list(itertools.combinations_with_replacement(colors, 2))

# 출력
options = [f"{c1}+{c2}" for c1, c2 in combinations]
print(", ".join(options))
# for option in options:
#     print(option)
