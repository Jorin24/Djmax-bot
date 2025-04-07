import random
import os
from collections import defaultdict

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# 방해요소 리스트
hindrance_pool = [
    "스피드 2.0",
    "스피드 8.0",
    "랜덤",
    "하프랜덤",
    "미러",
    "미러하프랜덤",
    "페이드 인",
    "페이드 아웃"
]

hindrance_weights = defaultdict(lambda: 1.0)


def draw_hindrances(player_names):
    print("\n🎲 방해요소 추첨 결과:")
    assigned = []
    for name in player_names:
        weighted_pool = [h for h in hindrance_pool for _ in range(int(hindrance_weights[h] * 100))]
        hindrance = random.choice(weighted_pool)
        assigned.append((name, hindrance))
        print(f"🎮 {name} → {hindrance}")
        hindrance_weights[hindrance] *= 0.75  # 확률 점점 낮아짐
    return assigned


def main():
    while True:
        clear()
        print("🎮 디제이맥스 방해요소 추첨기")
        try:
            num = int(input("\n▶ 참가자 수를 입력하세요 (숫자): "))
            if num <= 0:
                print("참가자 수는 1명 이상이어야 합니다.")
                input("Enter를 눌러 다시 시도하세요.")
                continue
        except ValueError:
            print("숫자를 제대로 입력해주세요!")
            input("Enter를 눌러 다시 시도하세요.")
            continue

        player_names = []
        for i in range(1, num + 1):
            name = input(f"▶ 참가자 {i} 이름 입력: ").strip()
            if name == "":
                name = f"참가자 {i}"
            player_names.append(name)

        draw_hindrances(player_names)

        again = input("\n▶ 다시 추첨하려면 Enter, 종료하려면 q 입력: ")
        if again.lower() == 'q':
            break
        hindrance_weights.clear()  # 새 추첨 시 확률 초기화

if __name__ == "__main__":
    main()
