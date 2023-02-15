# -*- coding: utf-8 -*-

import pygame

# 初期設定
pygame.init()

# 画面の設定
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")

# ブロックの設定
block_list = []
block_color = (255, 0, 0)
for x in range(0, 650, 50):
    for y in range(50, 100, 50):
        block = pygame.Rect(x, y, 50, 25)
        block_list.append(block)

# ボールの設定
ball_color = (255, 255, 255)
ball_radius = 10
ball_rect = pygame.Rect(325, 450, ball_radius, ball_radius)
ball_speed = [5, -5]

# パドルの設定
paddle_color = (255, 255, 255)
paddle_rect = pygame.Rect(300, 480, 100, 20)

# ゲームループ
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # パドルの移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        paddle_rect.x += 5

    # ボールの移動
    ball_rect = ball_rect.move(ball_speed)

    # ボールとブロックの当たり判定
    for block in block_list:
        if ball_rect.colliderect(block):
            ball_speed[1] = -ball_speed[1]
            block_list.remove(block)

    # ボールとパドルの当たり判定
    if ball_rect.colliderect(paddle_rect):
        ball_speed[1] = -ball_speed[1]

    # 画面の描画
    screen.fill((0, 0, 0))
    for block in block_list:
        pygame.draw.rect(screen, block_color, block)
    pygame.draw.circle(screen, ball_color, ball_rect.center, ball_radius)
    pygame.draw.rect(screen, paddle_color, paddle_rect)
    pygame.display.flip()

    # 60fpsで実行
    clock.tick(60)

# 終了処理
pygame.quit()
