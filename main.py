from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import random

# 画面の大きさ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# ボールの初期位置と半径
BALL_X = SCREEN_WIDTH // 2
BALL_Y = SCREEN_HEIGHT // 2
BALL_RADIUS = 10

# ブロックの設定
BLOCK_WIDTH = 75
BLOCK_HEIGHT = 20
BLOCK_MARGIN = 20
BLOCK_COLORS = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (128, 255, 0), (0, 255, 0)]

# パドルの設定
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_COLOR = (255, 255, 255)

# ボールの速度
BALL_SPEED = 2

# ゲームの初期化
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Block Breaker")

# ブロックのリスト
blocks = []
for i in range(5):
    for j in range(5):
        x = (BLOCK_MARGIN + BLOCK_WIDTH) * i + BLOCK_MARGIN
        y = (BLOCK_MARGIN + BLOCK_HEIGHT) * j + BLOCK_MARGIN + 50
        color = BLOCK_COLORS[j]
        block = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
        blocks.append((block, color))

# パドルの位置
paddle_x = SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2
paddle_y = SCREEN_HEIGHT - PADDLE_HEIGHT * 2

# ボールの初期速度
ball_speed_x = BALL_SPEED
ball_speed_y = -BALL_SPEED

# ゲームのメインループ
running = True
while running:
    # イベントの処理
    pygame.display.init()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # パドルの移動
    paddle_x, _ = pygame.mouse.get_pos()
    paddle_x -= PADDLE_WIDTH // 2
    if paddle_x < 0:
        paddle_x = 0
    if paddle_x + PADDLE_WIDTH > SCREEN_WIDTH:
        paddle_x = SCREEN_WIDTH - PADDLE_WIDTH

    # ボールの移動
    BALL_X += ball_speed_x
    BALL_Y += ball_speed_y
    # print("BALL_X:", BALL_X, " BALL_Y:", BALL_Y)

    # ボールが壁に当たった場合の処理
    if BALL_X - BALL_RADIUS <= 0 or BALL_X + BALL_RADIUS >= SCREEN_WIDTH:
        ball_speed_x = -ball_speed_x

    if BALL_Y - BALL_RADIUS <= 0:
        ball_speed_y = -ball_speed_y
    elif BALL_Y + BALL_RADIUS >= SCREEN_HEIGHT:
        # ボールが画面下端に到達した場合は初期位置に戻す
        BALL_X = SCREEN_WIDTH // 2
        BALL_Y = SCREEN_HEIGHT // 2

    # ボールがパドルに当たった場合の処理
    if BALL_Y + BALL_RADIUS >= paddle_y and paddle_x < BALL_X < paddle_x + PADDLE_WIDTH:
        ball_speed_y = -ball_speed_y

    # ボールがブロックに当たった場合の処理
    for block, color in blocks:
      if block.colliderect(pygame.Rect(BALL_X - BALL_RADIUS, BALL_Y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)):
          blocks.remove((block, color))
          ball_speed_y = -ball_speed_y

    # ブロックが全部消えたらゲーム終了
    if not blocks:
        font = pygame.font.Font(None, 50)
        text = font.render("Congratulations!", True, (255, 255, 255))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.wait(3000)
        running = False

    # 画面の描画
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (BALL_X, BALL_Y), BALL_RADIUS)
    pygame.draw.rect(screen, PADDLE_COLOR, pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    for block, color in blocks:
        pygame.draw.rect(screen, color, block)

    pygame.display.flip()

# ゲームの終了
pygame.quit()
