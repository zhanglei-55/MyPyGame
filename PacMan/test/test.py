"""
@File : test.py
@Author : mr
@Description :
项目需求如下:
1. 绘制地图 吃豆人 和豆子都在地图里
2. 绘制 吃豆人 和豆子 后续添加 敌人
3. 绘制 一个记分面板
4. 绘制一个按钮或者图片用于开始游戏
游戏玩法：
1. 吃豆人点击开始游戏后 便开始移动 随机 根据地图
2. 吃完所有豆子 即游戏结束 一个豆子 一份
@Date : 2024/05/20 21:55
"""
import pygame

pygame.init()
pygame.display.set_caption("吃豆人")
screen_width = 600
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill("")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()