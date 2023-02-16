import pygame

# 画面の大きさ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# ゲームの初期化
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Breaker")

# ブロックのリスト
blocks = []

# ブロックを作成してリストに追加
for i in range(5):
    for j in range(5):
        block = pygame.Rect(i*160, j*120, 150, 100)
        blocks.append(block)

# ボールの座標
ball_x = SCREEN_WIDTH/2
ball_y = SCREEN_HEIGHT/2

# ボールの移動速度
ball_speed_x = 5
ball_speed_y = 5

# パドルの座標
paddle_x = SCREEN_WIDTH/2
paddle_y = SCREEN_HEIGHT-50

# ゲームのメインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ボールの移動
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # ボールが画面外に出たら反射
    if ball_x < 0 or ball_x > SCREEN_WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y < 0:
        ball_speed_y = -ball_speed_y
    if ball_y > SCREEN_HEIGHT:
        running = False

    # パドルの移動
    paddle_x, _, _, _ = pygame.mouse.get_pos()

    # ブロックとボールの当たり判定
    for block in blocks:
        if block.collidepoint(ball_x, ball_y):
            ball_speed_y = -ball_speed_y
            blocks.remove(block)
            break

    # パドルとボールの当たり判定
    if (ball_x > paddle_x and ball_x < paddle_x + 150) and (ball_y > paddle_y):
        ball_speed_y = -ball_speed_y

    # 画面の描画
    screen.fill((0, 0, 0))
    pygame.draw.
