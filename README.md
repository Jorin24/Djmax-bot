# Djmax-bot

### This is a Djmax-bot for ANiMA Olympic.
The types of bots are as follows.
> Djmax_Map choice bot  
> Djmax_Obstacle draw bot

<details>
  <summary>Djmax_Map bot Code</summary>
  <div markdown="1">

```python
import random
import os

# DLC별 곡 리스트 (전체 반영)
dlc_songs = {
    "RESPECT": [
        "2Nite", "비상 ~Stay With Me~", "Armored Phantom", "Beautiful Day", "Beyond Yourself", "Binary World", "BlackCat", "Bullet, Wanted!", "Child of Night", "Don't Die", "Enter The Universe", "Far East Princess", "glory day", "Groovin Up", "Heavenly", "KILLER BEE", "Kung Brother", "Liar[10]", "Lift You Up", "Mulch", "NB RANGER - Virgin Force", "Only for you", "OPEN FIRE", "quixotic", "Remains Of Doom", "Royal Clown", "Runaway", "Running girl", "Ruti'n (GOTH Wild Electro Remix)", "Secret Dejavu", "Shadow Flower", "The Feelings", "The Lost Story", "The Obliterator", "U.A.D", "v o l d e n u i t", "waiting for me", "Waiting for you", "We're All Gonna Die", "WHY", "Always[CR]", "Fly Away", "Tok! Tok! Tok!", "Over Your Dream[2주년]", "Void[브라운더스트][2주년]"
    ],
    "RESPECT/V": [
        "Alone", "Boom!", "NEON 1989 (ESTi Remix)[CR]", "Ghost Voices", "Sad Machine", "Bleed", "Kingdom", "So Happy", "Get Jinxed[CR]", "POP/STARS[CR]", "Chemical Slave[3주년]", "RockSTAR[3주년]", "Watch Your Step[3주년]", "혜성[3주년]", "I want You\n~반짝★반짝 Sunshine~[브라운더스트][3주년]", "염라[CR]", "Dance of the Dead[TWC]", "Grid System[V1주년]", "서울여자[CR]", "Relation Again (ESTi's Remix)[4주년]", "너로피어오라[CR]", "Alone", "너랑 있으면", "Aurora Borealis[V2주년]", "Airlock", "Daylight", "OrBiTal", "Angelic Tears", "모짜르트 교향곡 40번 1악장", "Mr.Lonely[5주년]", "Dancin' Planet", "I'M ALIVE[V3주년]", "Dark Lightning", "Celestial Tears", "Can We Talk (Broken Dog Leg Mix)", "BlueWhite[V4주년]", "Kamui", "From Hell to Breakfast[CP]", "SURVIVOR[CP]"
    ],
    "PORTABLE": [
        "바람에게 부탁해", "바람에게 부탁해 ~Live Mix~[1주년]", "복수혈전", "아침형 인간", "피아노 협주곡 1번", "A.I", "Astro Fight", "BlythE", "Bright Dream", "Can We Talk", "Catch Me", "Chrono Breakers", "CnP[44]", "Dreadnought[45]", "Elastic Star", "End of the Moonlight[46]", "Enemy Storm", "Eternal Memory ~소녀의 꿈~", "Extreme Z4", "FEAR", "Fever GJ", "FTR", "Funky Chups", "Futurism", "HAMSIN", "JBG", "Jupiter Driving", "KUDA", "Lemonade", "Let's Go Baby", "Light House", "Long Vacation", "Luv Flow", "MASAI", "Memory of Beach", "Minimal Life", "NB Ranger", "Never Say", "OBLIVION", "OBLIVION (Rockin' Night Style)", "ON", "One the Love", "Out Law", "Para Q", "Ray of Illuminati", "RED", "Road Of Death", "Rock Or Die", "Save My Dream", "SIN", "SIN ~The Last Scene~", "Sunny Side", "Sunny Side (deepn' soul Mix)", "Temptation", "Triple Zoe", "Ya! Party!"
    ],
    "PORTABLE 2": [
        "설레임", "태권부리", "A Lie", "Another DAY", "Brain Storm", "Brandnew Days[48][CR]", "Brave it Out", "Bye Bye Love", "Chain of Gravity", "Cherokee", "DIVINE SERVICE", "Dream of You", "Fallen Angel", "Fentanest", "For Seasons", "For the IKARUS", "Get On Top", "GET OUT", "Good Bye", "Hello Pinky", "Higher", "Ladymade Star", "Lost n' found", "Memoirs", "Mess it Up", "Midnight Blood", "Miles", "Minus 3", "My Alias", "NANO RISK", "NB POWER", "NB RANGERS : Returns", "Negative Nature", "Nightmare", "Phantom of Sky", "Plastic Method", "Right Now", "Rocka-a-doodle-doo", "Rolling On the Duck", "Seeker", "Showtime", "Smoky Quartz", "sO mUCH iN LUV", "SQUEEZE", "STALKER", "StarFish", "Stay with me", "Sunset Rider", "Syriana", "WhiteBlue", "Yellowberry (AJ Mix)", "Yo Creo Que Si", "Your Own Miracle[50]"
    ],
    "V EXTENTION": [
        "Attack", "BLACK GOLD[TB]", "Do it[CR]", "Dream it", "Fancy Night", "FIGHT NIGHT (feat. Calyae)[TB]", "Kensei", "Lisrim[CR]", "Lost Serenity", "Lost Temple", "Maharajah -fenomeno edition-[CR]", "Misty Er'A", "Move Yourself", "NANAIRO", "Never Die", "Remember Me", "Space Challenger", "Vile Requiem", "welcome to the space (feat. Jisun)", "WONDER $LOT 777"
    ],
    "V EXTENTION 2": [
        "꿈의 기억 (feat. Jisun)", "Arcade Love (feat. KNVWN)", "Chrysanthemum", "Cocked Pistol", "Daydream", "FALLING IN LOVE", "Forgotten", "I've got a feeling", "Imaginary dance", "Melonaid", "Never let you go", "Odysseus", "Over Me", "Red Eyes", "Sweet On You", "Underwater Castle", "Vertical Floating", "Voyage", "Won't Back Down", "Zero to the hunnit"
    ],
    "V EXTENTION 3": [
        "밤비(Bambi) - DJMAX Edit -[CR]", "#mine (feat. Riho Iwamoto)", "Bright Future", "Charming World", "Disappearing Act", "Emerge", "Every Day ~ Every Night", "Fundamental", "KICK IT", "Misty E'ra 'Mui'", "Moment (feat. Nauts)", "NB RANGERS - 운명의 Destiny", "Plasma Sphere", "Secret", "Set Me Free", "Space Dream (feat. J.O.Y)", "STEP", "Tic! Tac! Toe![CR]", "Winners", "Zero-Break"
    ],
    "V EXTENTION 4": [
        "너에게로 갈래", "!!New Game Start!!", "ADDICT!ON (DJMAX Edit)[CR]", "Back to the oldschool", "Deadly Bomber", "DIE IN", "Don't Cry", "Gloxinia", "Hell'o", "Hyper Drive", "Hypernaid", "Like a Fool", "Love.Game.Money", "LUV", "New World", "Stolen Memory", "Stay Alive", "The Four Seasons : Summer 2017[TWC]", "Vertical Eclipse", "Weaponize"
    ],
    "V EXTENTION 5": [
        "별빛너머", "3:33", "Accelerate", "Behemoth", "Carrot Carrot", "Critical Point", "ECiLA", "glory MAX -나의 최대치로 너와 함께할게-", "God Machine", "Inside the Light", "My Wonderland", "Paradise", "Peace Comes At a Price", "Pitter-patter", "Revenger", "Rhapsody for The VEndetta", "Right Time [ScreaM Records]", "Rocket Launcher", "S.A.V.E", "Shining Light (feat. Shabel Tonya)"
    ],
    "V LIBERTY": [
        "덫", "따라와", "때론, 냉정도 필요해", "성장통 [ScreaM Records]", "평행고백 ~Pan Remix~", "Away", "Basement", "Bestie", "Break Out", "Broken Sphere", "Cotton Candy Soda", "Diomedes", "Final Hour (Game Ver.)", "Final Round", "Licrom", "O'men", "Petunia", "Rhythm In My Head", "Song For You", "Synchronize"
    ],
    "V LIBERTY 2": [
        "1! 2! 3! 4! Streaming rn CHU!", "B!G-BANG CHALLENGE", "break it down!", "Cata (feat. NC.A)", "Cheonmasan", "Delusion (feat. SOONHO)", "ELIXIR", "Hikari (feat. Negoto Bunnyla)", "Kakera", "Krush", "Love or Die", "Mad (feat. WaMi)", "MADNESS (feat. U1)", "Misty Er'A ~One Day~", "Outcast (feat. BIRA)", "Pull The Trigger", "RIPPER", "Rocket Ride", "Saga Script", "TOXIC (feat. Shabel Tonya)"
    ],
    "TECHNIKA 3": [
        "설레임 Part.2", "유령", "AD2222", "A Life With You", "Angel", "Bamboo on Bamboo", "Black Swan", "Dark Prism", "Dream Again", "EGG", "Emblem", "Fallin' in LUV", "Feel Ma Beat", "Give Me 5", "Kung-Fu Rider", "My Heart, My Soul", "Now a NEW Day", "Out of CTRL", "Over The Rainbow", "Right Back", "Showdown", "SigNalize", "SuperNova", "Supersonic 2011", "Wanna Be Your Lover", "Xeus", "You & Me", "AD2222 ~Extended Mix~", "EGG ~Extended Mix~"
    ],
    "GUILTY GEAR": [
        "Break a Spell", "Holy Orders (Be Just Or Be Dead)", "Marionette"
    ],
    "GIRLS' FRONTLINE": [
        "Frontline", "What am I Fighting for?", "Barbarous Funera"
    ],
    "GROOVE COASTER": [
        "Black MInD", "Good Night, Bad Luck.", "Got more raves?", "Groove Prayer", "HB-axeleration", "Marry me, Nightmare", "ouroboros -twin stroke of the end-", "OVER THE NIGHT", "Satisfiction", "Warrior"
    ],
    "DEEMO": [
        "Angelic Sphere", "ANiMA", "Dream", "Legacy", "Magnolia", "Nine Point Eight", "Sairai", "Undo", "Utopiosphere", "YUBIKIRI-GENMAN"
    ],
    "Cytus": [
        "AXION", "CODE NAME : ZERO", "conflict", "EMber", "Entrance", "L", "Les Parfums de L'Amour", "Mammal", "Myosotis[CR]", "Old Gold", "Shoot out", "Ververg"
    ],
    "CHUNITHM": [
        "Cyberozar", "Garakuta Doll Play", "Ikazuchi", "Ray Tuning", "The wheel to the right", "Trrricksters!!"
    ],
    "Muse Dash": [
        "Bang!!", "can you feel it", "Comet Coaster", "Cthugha", "DataErr0r", "Dysthymia", "ENERGY SYNERGY MATRIX", "Koi no Moonlight", "Lights of Muse", "MUSEDASH!!!!", "Pancake is Love", "PUPA[CR]", "tape/stop/night", "The 90's Decision", "XING"
    ],
    "EZ2ON": [
        "느낌", "Appeal", "Aquaris", "Back for more", "Complex", "Envy Mask", "Lie Lie", "Look out ~Here comes my love~", "Metagalactic", "Nihilism", "Sand Storm", "Showdown", "Sparrow", "Stay", "Weird Wave", "A Site De La Rue", "LIMBO", "Zeroize"
    ]
}

# 전체 곡 리스트와 인덱스
all_songs = []
song_index_map = {}
for dlc, songs in dlc_songs.items():
    for i, song in enumerate(songs, start=1):
        all_songs.append(song)
        song_index_map[song] = (dlc, i)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_song(keyword):
    return [(i + 1, song, song_index_map[song]) for i, song in enumerate(all_songs) if keyword.lower() in song.lower()]

def select_songs():
    clear()
    print("디제이맥스 곡 리스트:")
    for i, song in enumerate(all_songs):
        print(f"{i+1}. {song}")
    print("\n'search <키워드>' 입력 시 곡 검색 가능")

    selected = []
    while len(selected) < 4:
        user_input = input(f"\n{len(selected)+1}/4 곡 선택 (번호 또는 검색): ")

        if user_input.lower().startswith("search"):
            keyword = user_input[6:].strip()
            results = search_song(keyword)
            print(f"\n🔍 '{keyword}' 검색 결과:")
            for idx, song, (dlc, original_idx) in results:
                print(f"{idx}. [{dlc} #{original_idx}] {song}")
            continue

        try:
            pick = int(user_input)
            if 1 <= pick <= len(all_songs):
                song = all_songs[pick - 1]
                if song not in selected:
                    selected.append(song)
                else:
                    print("이미 선택된 곡입니다.")
            else:
                print("목록에 있는 번호를 입력하세요.")
        except ValueError:
            print("숫자나 'search <키워드>'를 입력해주세요.")
    return selected

def draw_song(prompt, candidates):
    input(prompt)
    chosen = random.choice(candidates)
    dlc, idx = song_index_map.get(chosen, ("Unknown", "?"))
    print(f"\n🎲 추첨 결과: {chosen}\n[DLC: {dlc} | 곡 번호: {idx}]\n")
    return chosen

def main():
    while True:
        print("🎮 플레이어 1 이름을 입력하세요:")
        player1_name = input("> ")
        print("🎮 플레이어 2 이름을 입력하세요:")
        player2_name = input("> ")

        selected = select_songs()
        player1 = selected[:2]
        player2 = selected[2:]

        print(f"\n🎮 {player1_name} 곡: {player1}")
        print(f"🎮 {player2_name} 곡: {player2}")

        first = draw_song("\n▶ Enter를 누르면 1라운드 곡을 추첨합니다!", selected)

        second_pool = player2 if first in player1 else player1
        second_pool = [s for s in second_pool if s != first]
        second = draw_song("▶ Enter를 누르면 2라운드 곡을 추첨합니다!", second_pool)

        decision = input("▶ Enter를 누르면 종료 / k 입력하면 3라운드 진행: ").lower()
        if decision == "k":
            third_pool = [s for s in selected if s not in [first, second]]
            draw_song("▶ Enter를 누르면 3라운드 곡을 추첨합니다!", third_pool)

        input("\nEnter를 누르면 처음으로 돌아갑니다!")
        clear()

if __name__ == "__main__":
    main()
```
</div>
</details>

#### This map bot has the ability to draw randomly among songs used in the Anima DMAC competition.  
---
<details>
  <summary>Djmax_Obstacle draw bot Code</summary>
  <div markdown="1">


```python
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
```
</div>
</details>

#### This bot does a raffle of distractions that can be used in the contest.
