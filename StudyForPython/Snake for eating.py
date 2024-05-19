"""
@File : Snake for eating.py
@Author : mr
@Description : 
"""
import sys
import pygame
import random

# pygame setup
pygame.init()
screen_width = 500
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
snack_x = 300
snack_y = 300
food_x = random.randint(0, screen_width - 10)
food_y = random.randint(0, screen_height - 10)
score = 0
speed = 2

# 随机选择初始方向
directions = ['LEFT', 'RIGHT', 'UP', 'DOWN']
direction = random.choice(directions)

# 蛇身初始化，初始长度为1
snake_body = [(snack_x, snack_y)]


def check_collision(snack_x, snack_y, food_x, food_y, snack_size=22, food_radius=4):
    # 方块的中心
    snack_center_x = snack_x + snack_size / 2
    snack_center_y = snack_y + snack_size / 2
    # 圆的中心
    food_center_x = food_x
    food_center_y = food_y
    # 计算中心之间的距离
    distance = ((snack_center_x - food_center_x) ** 2 + (snack_center_y - food_center_y) ** 2) ** 0.5
    # 如果距离小于方块的一半加上圆的半径，则碰撞
    return distance < (snack_size / 2 + food_radius)


while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # 填充屏幕背景
    screen.fill("black")

    # 获取按键状态并改变移动方向
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != 'RIGHT':
        direction = 'LEFT'
    if keys[pygame.K_RIGHT] and direction != 'LEFT':
        direction = 'RIGHT'
    if keys[pygame.K_UP] and direction != 'DOWN':
        direction = 'UP'
    if keys[pygame.K_DOWN] and direction != 'UP':
        direction = 'DOWN'

    # 根据当前方向移动蛇头
    if direction == 'LEFT':
        snack_x -= speed
    if direction == 'RIGHT':
        snack_x += speed
    if direction == 'UP':
        snack_y -= speed
    if direction == 'DOWN':
        snack_y += speed

    # 更新蛇身位置
    snake_body.append((snack_x, snack_y))
    if len(snake_body) > score + 6:
        snake_body.pop(0)

    # 绘制食物
    pygame.draw.circle(screen, "white", (food_x, food_y), 7)

    # 绘制蛇身
    for segment in snake_body:
        pygame.draw.rect(screen, "white", (*segment, 15, 15))

    # 检查碰撞
    if check_collision(snack_x, snack_y, food_x, food_y):
        score += 1
        food_x = random.randint(0, screen_width - 8)
        food_y = random.randint(0, screen_height - 8)

    # 刷新屏幕
    pygame.display.flip()
    clock.tick(60)  # 限制帧率为60FPS

print("Score:", score)
print(len(snake_body))
pygame.quit()
sys.exit()
