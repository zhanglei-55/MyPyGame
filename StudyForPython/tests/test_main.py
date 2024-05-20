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
# 创建屏幕对象
screen = pygame.display.set_mode((screen_width, screen_height))
# 创建时钟对象
clock = pygame.time.Clock()
# 设置游戏是否运行的变量
running = True

# 设置初始蛇和食物的位置
snack_x = 300
snack_y = 300

# 食物不能在屏幕外
distance = 10
# 使用随机数，随机生成食物位置 => 坐标左上角为(0,0) => x轴向右,y轴向左
food_x = random.randint(distance, screen_width - distance)
food_y = random.randint(distance, screen_height - distance)

# 初始化游戏得分和蛇的速度
score = 0
speed = 2

# 随机选择初始方向
directions = ['LEFT', 'RIGHT', 'UP', 'DOWN']
# 使用此来随机获取列表的值，而不是索引
direction = random.choice(directions)

# 初始化蛇身，初始长度为1
snake_body = [(snack_x, snack_y)]

# 设置食物数量
food_count = 10


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


def draw_score():
    """
    绘制游戏得分
    """
    score_font = pygame.font.SysFont(None, 30)
    score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


def new_direction(direction):
    """
    根据当前方向，选择新的方向
    :param direction:
    :return:
    """
    # 根据当前方向，随机选择一个新的方向，避免蛇原地掉头
    if direction == 'LEFT':
        return random.choice(['UP', 'DOWN', "RIGHT"])
    if direction == 'RIGHT':
        return random.choice(['UP', 'DOWN', "LEFT"])
    if direction == 'UP':
        return random.choice(["RIGHT", 'DOWN', "LEFT"])
    if direction == 'DOWN':
        return random.choice(["LEFT", 'UP', "RIGHT"])


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
    # 规定按键后的新方向，避免蛇身体撞墙
    if keys[pygame.K_LEFT] and direction != 'RIGHT':
        direction = 'LEFT'
    if keys[pygame.K_RIGHT] and direction != 'LEFT':
        direction = 'RIGHT'
    if keys[pygame.K_UP] and direction != 'DOWN':
        direction = 'UP'
    if keys[pygame.K_DOWN] and direction != 'UP':
        direction = 'DOWN'
    if (
            snack_x < 20 or snack_x > screen_width - 20 or snack_y < 20 or snack_y > screen_height - 20) and not changed_direction:
        direction = new_direction(direction)
        changed_direction = True
    else:
        changed_direction = False

        # 判断蛇是否撞上屏幕
    if snack_x < 0 or snack_x > screen_width - 15 or snack_y < 0 or snack_y > screen_height - 15:
        print("游戏结束")
        running = False

    # 判断蛇是否撞上屏幕
    if snack_x < 0 or snack_x > screen_width - 15 or snack_y < 0 or snack_y > screen_height - 15:
        print("游戏结束")
        running = False
        # new_direction(direction)

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
        food_x = random.randint(distance, screen_width - distance)
        food_y = random.randint(distance, screen_height - distance)
    draw_score()
    # 更新屏幕
    pygame.display.flip()
    clock.tick(60)  # 限制游戏帧率为60FPS

# 退出pygame
pygame.quit()
sys.exit()
