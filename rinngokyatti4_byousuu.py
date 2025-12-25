import pyxel
import random

pyxel.init(300, 600)

score = 0
turns = 0  # ターン数を管理する変数
time_counter = 0
time_counter2 = 0
time_counter3 = 0
time_counter4 = 0
speedplay = 10
haba = 40
width_boost_turns = 0
applesspeed = 0
speedapple1 = 1
speedapple2 = 7
speedapple3 = 5


# 初期のリンゴのリストは空にしておく
apples = []
apples2 = []
apples3 = []
apples4 = []
apples5 = []


player = {"x": pyxel.width / 2 - 10, "y": pyxel.height - 20, "w": haba, "h": 20, "speed": speedplay}

def add_apples():
    """新しいリンゴを4個追加する関数"""
    global turns, speedapple1, speedapple2, speedapple3
    #凡リンゴ
    for _ in range(4):
        x_position = random.randint(5, pyxel.width - 15)
        speed = random.randint(speedapple1, speedapple2)
        apples.append({"x": x_position, "y": 0, "speed": speed, "alive": True})
    #特殊リンゴ1
    syutugennritu = [0,0,0,0,0,0,0,1]
    tokusyu = random.choice(syutugennritu)
    for _ in range(tokusyu):
        x_position = random.randint(5, pyxel.width - 15)
        speed = random.randint(speedapple3, speedapple2)
        apples2.append({"x": x_position, "y": 0, "speed": speed, "alive": True})
    #特殊リンゴ2
    syutugennritu2 = [0,0,0,0,0,0,0,1]
    tokusyu2 = random.choice(syutugennritu2)
    for _ in range(tokusyu2):
        x_position = random.randint(5, pyxel.width - 15)
        speed = random.randint(speedapple3, speedapple2)
        apples3.append({"x": x_position, "y": 0, "speed": speed, "alive": True})
    #特殊リンゴ３
    syutugennritu3 = [0,0,0,0,0,0,0,1]
    tokusyu3 = random.choice(syutugennritu3)
    for _ in range(tokusyu3):
        x_position = random.randint(5, pyxel.width - 15)
        speed = random.randint(speedapple3, speedapple2)
        apples4.append({"x": x_position, "y": 0, "speed": speed, "alive": True})
    #特殊リンゴ４
    syutugennritu4 = [0,0,0,0,0,1]
    tokusyu4 = random.choice(syutugennritu4)
    for _ in range(tokusyu4):
        x_position = random.randint(5, pyxel.width - 15)
        speed = random.randint(3, 6)
        apples5.append({"x": x_position, "y": 0, "speed": speed, "alive": True})


    turns += 1  # リンゴを追加するたびにターン数を増やす

def update():
    global apples, apples2, apples3, apples4, apples5, score, time_counter, time_counter2, time_counter3, time_counter4, width_boost_turns, haba, speedplay, applesspeed, speedapple1, speedapple2, speedapple3

    if score >= 600:
        print(f"ゲーム終了！ターン数: {turns}")
        pyxel.quit()

    # 時間を計測して5秒ごとにリンゴを追加
    time_counter += 1
    if time_counter >= 30 * 5:  # PyxelのデフォルトFPSは30なので、5秒ごとに
        add_apples()
        time_counter = 0

    if speedplay == 15:
        time_counter2 += 1
        if time_counter2 >= 30 * 15:  # PyxelのデフォルトFPSは30なので、10秒ごとに
            time_counter2 = 0
            speedplay = 10

    if width_boost_turns == 2:
        player["w"] = 60
        time_counter3 += 1
        if time_counter3 >= 30 * 15: 
            player["w"] = 40  
            time_counter3 = 0
            width_boost_turns = 0

    if applesspeed == 2:
        speedapple1 = 4
        speedapple2 = 9
        speedapple3 = 7
        time_counter4 += 1
        if time_counter4 >= 30 * 15: 
            time_counter4 = 0
            applesspeed = 0
            speedapple1 = 1
            speedapple2 = 7
            speedapple3 = 5
            

    #凡リンゴ
    for apple in apples:
        apple["y"] += apple["speed"]

        if apple["y"] > pyxel.height:
            apple["alive"] = False
    #特殊リンゴ1
    for apple2 in apples2:
        apple2["y"] += apple2["speed"]

        if apple2["y"] > pyxel.height:
            apple2["alive"] = False
    #特殊リンゴ2
    for apple3 in apples3:
        apple3["y"] += apple3["speed"]

        if apple3["y"] > pyxel.height:
            apple3["alive"] = False
# 新しい特殊リンゴ
    for apple4 in apples4:
        apple4["y"] += apple4["speed"]
        if apple4["y"] > pyxel.height:
            apple4["alive"] = False
# 新しい特殊リンゴ
    for apple5 in apples5:
        apple5["y"] += apple5["speed"]
        if apple5["y"] > pyxel.height:
            apple5["alive"] = False


    #凡リンゴ
    for apple in apples:
        if (player["x"] < apple["x"] + 10 and
            player["x"] + player["w"] > apple["x"] and
            player["y"] < apple["y"] + 10 and
            player["y"] + 20 > apple["y"]):
            apple["alive"] = False
            score += 10
    #特殊リンゴ1
    for apple2 in apples2:
        if (player["x"] < apple2["x"] + 10 and
            player["x"] + player["w"] > apple2["x"] and
            player["y"] < apple2["y"] + 10 and
            player["y"] + 20 > apple2["y"]):
            apple2["alive"] = False
            speedplay = 15
    #特殊リンゴ3
    for apple3 in apples3:
        if (player["x"] < apple3["x"] + 10 and
            player["x"] + player["w"] > apple3["x"] and
            player["y"] < apple3["y"] + 10 and
            player["y"] + 20 > apple3["y"]):
            apple3["alive"] = False
            score += 40
    #
    for apple4 in apples4:
        if (player["x"] < apple4["x"] + 10 and
            player["x"] + player["w"] > apple4["x"] and
            player["y"] < apple4["y"] + 10 and
            player["y"] + 20 > apple4["y"]):
            apple4["alive"] = False
            width_boost_turns = 2
    #
    for apple5 in apples5:
        if (player["x"] < apple5["x"] + 10 and
            player["x"] + player["w"] > apple5["x"] and
            player["y"] < apple5["y"] + 10 and
            player["y"] + 20 > apple5["y"]):
            apple5["alive"] = False
            applesspeed  = 2

    apples = [apple for apple in apples if apple["alive"]]
    apples2 = [apple2 for apple2 in apples2 if apple2["alive"]]
    apples3 = [apple3 for apple3 in apples3 if apple3["alive"]]
    apples4 = [apple4 for apple4 in apples4 if apple4["alive"]]
    apples5 = [apple5 for apple5 in apples5 if apple5["alive"]]

    if pyxel.btn(pyxel.KEY_RIGHT):
        if player["x"] < pyxel.width - player["w"]:
            player["x"] += speedplay
    if pyxel.btn(pyxel.KEY_LEFT):
        if player["x"] >= 10:
            player["x"] -= speedplay
    if pyxel.btn(pyxel.KEY_UP):
        if player["y"] >= 10:
            player["y"] -= speedplay
    if pyxel.btn(pyxel.KEY_DOWN):
        if player["y"] < pyxel.height - 20:
            player["y"] += speedplay

def draw():
    pyxel.cls(0)
    #凡リンゴ
    for apple in apples:
        pyxel.rect(apple["x"], apple["y"], 10, 10, 8)
    #特殊リンゴ1
    for apple2 in apples2:
        pyxel.rect(apple2["x"], apple2["y"], 10, 10, 5)
    #特殊リンゴ2
    for apple3 in apples3:
        pyxel.rect(apple3["x"], apple3["y"], 10, 10, 10)
    #特殊リンゴ3
    for apple4 in apples4:
        pyxel.rect(apple4["x"], apple4["y"], 10, 10, 3)
    #
    for apple5 in apples5:
        pyxel.rect(apple5["x"], apple5["y"], 10, 10, 2)


    pyxel.rect(player["x"], player["y"], player["w"], 20, 7)

    # スコアとターン数を表示
    pyxel.text(10, 10, f"SCORE: {score}", 7)  # スコアを表示
    pyxel.text(10, 20, f"TURNS: {turns}", 7)  # ターン数を表示

pyxel.run(update, draw)