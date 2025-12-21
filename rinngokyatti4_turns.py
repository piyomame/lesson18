import pyxel
import random

pyxel.init(300, 600)

score = 0
turns = 0  # ターン数を管理する変数
turns2 = 0
time_counter = 0
speedplay = 10

def turnsapple():
    if speedplay == 20:
        turns2 = 0
        if turns2 >= 2:
            turns2 = 0
            speedplay = 10

# 初期のリンゴのリストは空にしておく
apples = []
apples2 = []

player = {"x": pyxel.width / 2 - 10, "y": pyxel.height - 20, "w": 20, "h": 20, "speed": speedplay}

def add_apples():
    """新しいリンゴを4個追加する関数"""
    global turns,turns2
    #凡リンゴ
    for _ in range(4):
        x_position = random.randint(5, pyxel.width - 15)
        speed = random.randint(1, 7)
        apples.append({"x": x_position, "y": 0, "speed": speed, "alive": True})
    #特殊リンゴ
    syutugennritu = [0,0,0,0,0,0,0,0,0,1]
    tokusyu = random.choice(syutugennritu)
    for _ in range(tokusyu):
        x_position = random.randint(5, pyxel.width - 15)
        speed = random.randint(5, 7)
        apples2.append({"x": x_position, "y": 0, "speed": speed, "alive": True})
    turns += 1  # リンゴを追加するたびにターン数を増やす
    turns2 += 1

def update():
    global apples, apples2, score, time_counter ,speedplay, turns2

    if score >= 400:
        print(f"ゲーム終了！ターン数: {turns}")
        pyxel.quit()

    # 時間を計測して5秒ごとにリンゴを追加
    time_counter += 1
    if time_counter >= 30 * 5:  # PyxelのデフォルトFPSは30なので、5秒ごとに
        add_apples()
        time_counter = 0

    #凡リンゴ
    for apple in apples:
        apple["y"] += apple["speed"]

        if apple["y"] > pyxel.height:
            apple["alive"] = False
    #特殊リンゴ
    for apple2 in apples2:
        apple2["y"] += apple2["speed"]

        if apple2["y"] > pyxel.height:
            apple2["alive"] = False

    #凡リンゴ
    for apple in apples:
        if (player["x"] < apple["x"] + 10 and
            player["x"] + 40 > apple["x"] and
            player["y"] < apple["y"] + 10 and
            player["y"] + 20 > apple["y"]):
            apple["alive"] = False
            score += 10
    #特殊リンゴ
    for apple2 in apples2:
        if (player["x"] < apple2["x"] + 10 and
            player["x"] + 40 > apple2["x"] and
            player["y"] < apple2["y"] + 10 and
            player["y"] + 20 > apple2["y"]):
            apple2["alive"] = False
            speedplay = 20
            

    apples = [apple for apple in apples if apple["alive"]]
    apples2 = [apple2 for apple2 in apples2 if apple2["alive"]]

    if pyxel.btn(pyxel.KEY_RIGHT):
        if player["x"] < pyxel.width - 20:
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
    
    if speedplay == 20: #特殊リンゴ取得後ターンカウント
        if turns2 >= 2:
            turns2 = 0
            speedplay = 10

def draw():
    pyxel.cls(0)
    #凡リンゴ
    for apple in apples:
        pyxel.rect(apple["x"], apple["y"], 10, 10, 8)
    #特殊リンゴ
    for apple2 in apples2:
        pyxel.rect(apple2["x"], apple2["y"], 10, 10, 5)

    pyxel.rect(player["x"], player["y"], 40, 20, 7)

    # スコアとターン数を表示
    pyxel.text(10, 10, f"SCORE: {score}", 7)  # スコアを表示
    pyxel.text(10, 20, f"TURNS: {turns}", 7)  # ターン数を表示

pyxel.run(update, draw)