"""
@File : test_main.py.py
@Author : mr
@Description : 
"""
import sys
import pygame
import random

# 初始化pygame并设置屏幕大小
pygame.init()
screen_width = 500
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

# 设置初始蛇和食物的位置
snack_x = 300
snack_y = 300
food_x = random.randint(0, screen_width - 10)
food_y = random.randint(0, screen_height - 10)

# 初始化游戏得分和蛇的速度
score = 0
speed = 2

# 随机选择初始方向
directions = ['LEFT', 'RIGHT', 'UP', 'DOWN']
direction = random.choice(directions)

# 初始化蛇身，初始长度为1
snake_body = [(snack_x, snack_y)]

def check_collision(snack_x, snack_y, food_x, food_y, snack_size=22, food_radius=4):
    """
    检测蛇是否与食物发生碰撞

    参数:
    - snack_x, snack_y: 蛇头的x和y坐标
    - food_x, food_y: 食物的x和y坐标
    - snack_size: 蛇方块的大小，默认为22
    - food_radius: 食物的半径，默认为4

    返回值:
    - bool: 如果发生碰撞返回True，否则返回False
    """
    # 计算蛇头和食物中心的距离
    snack_center_x = snack_x + snack_size / 2
    snack_center_y = snack_y + snack_size / 2
    food_center_x = food_x
    food_center_y = food_y
    distance = ((snack_center_x - food_center_x) ** 2 + (snack_center_y - food_center_y) ** 2) ** 0.5
    # 判断是否碰撞
    return distance < (snack_size / 2 + food_radius)

# 游戏主循环
while running:
    # 处理事件，如退出和按键
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # 清空屏幕
    screen.fill("black")

    # 处理按键改变方向
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != 'RIGHT':
        direction = 'LEFT'
    if keys[pygame.K_RIGHT] and direction != 'LEFT':
        direction = 'RIGHT'
    if keys[pygame.K_UP] and direction != 'DOWN':
        direction = 'UP'
    if keys[pygame.K_DOWN] and direction != 'UP':
        direction = 'DOWN'

    # 根据方向移动蛇头
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

    # 检查蛇是否吃到食物
    if check_collision(snack_x, snack_y, food_x, food_y):
        score += 1
        food_x = random.randint(0, screen_width - 8)
        food_y = random.randint(0, screen_height - 8)

    # 更新屏幕
    pygame.display.flip()
    clock.tick(60)  # 限制游戏帧率为60FPS

# 游戏结束，输出得分和蛇的长度
print("Score:", score)
print(len(snake_body))

# 退出pygame
pygame.quit()
sys.exit()
