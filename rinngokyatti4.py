import pyxel
import random

pyxel.init(300, 600)

score = 0
turns = 0  # ターン数を管理する変数
time_counter = 0

# 初期のリンゴのリストは空にしておく
apples = []

player = {"x": pyxel.width / 2 - 10, "y": pyxel.height - 20, "w": 20, "h": 20, "speed": 5}

def add_apples():
    """新しいリンゴを3個追加する関数"""
    global turns
    for _ in range(3):
        x_position = random.randint(5, pyxel.width - 15)
        speed = random.randint(1, 8)
        apples.append({"x": x_position, "y": 0, "speed": speed, "alive": True})
    turns += 1  # リンゴを追加するたびにターン数を増やす

def update():
    global apples, score, time_counter

    if score >= 200:
        print(f"ゲーム終了！ターン数: {turns}")
        pyxel.quit()

    # 時間を計測して5秒ごとにリンゴを追加
    time_counter += 1
    if time_counter >= 30 * 5:  # PyxelのデフォルトFPSは30なので、5秒ごとに
        add_apples()
        time_counter = 0

    for apple in apples:
        apple["y"] += apple["speed"]

        if apple["y"] > pyxel.height:
            apple["alive"] = False

    for apple in apples:
        if (player["x"] < apple["x"] + 10 and
            player["x"] + 40 > apple["x"] and
            player["y"] < apple["y"] + 10 and
            player["y"] + 20 > apple["y"]):
            apple["alive"] = False
            score += 10

    apples = [apple for apple in apples if apple["alive"]]

    if pyxel.btn(pyxel.KEY_RIGHT):
        if player["x"] < pyxel.width - 20:
            player["x"] += 10
    if pyxel.btn(pyxel.KEY_LEFT):
        if player["x"] >= 10:
            player["x"] -= 10
    if pyxel.btn(pyxel.KEY_UP):
        if player["y"] >= 10:
            player["y"] -= 10
    if pyxel.btn(pyxel.KEY_DOWN):
        if player["y"] < pyxel.height - 20:
            player["y"] += 10

def draw():
    pyxel.cls(0)
    for apple in apples:
        pyxel.rect(apple["x"], apple["y"], 10, 10, 8)

    pyxel.rect(player["x"], player["y"], 40, 20, 7)

    # スコアとターン数を表示
    pyxel.text(10, 10, f"SCORE: {score}", 7)  # スコアを表示
    pyxel.text(10, 20, f"TURNS: {turns}", 7)  # ターン数を表示

pyxel.run(update, draw)