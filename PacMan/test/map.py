"""
@File : map.py
@Author : mr
@Description :
使用二维数组绘制地图
"""
import pygame
import sys

# 初始化Pygame
pygame.init()

# 定义常量
WIDTH = 400
HEIGHT = 440
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 定义地图数据
# 0表示空白区域，1表示墙壁，2表示豆子
MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 设置窗口大小
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Map")

# 加载图像
wall_img = pygame.image.load("..\img\wall.jpg")
dot_img = pygame.image.load("..\img\dot1.png")

size_width = 40
size_height = 40
wall_new_img = pygame.transform.scale(wall_img, (40, 40))
dot_new_img = pygame.transform.scale(dot_img, (20, 20))


# 游戏主循环
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 清屏
        win.fill(WHITE)

        # 绘制地图
        for y, row in enumerate(MAP):
            for x, tile in enumerate(row):
                if tile == 1:
                    win.blit(wall_new_img, (x * 40, y * 40))
                elif tile == 0:
                    win.blit(dot_new_img, (x * 40, y * 40))

        # 更新屏幕
        pygame.display.update()


if __name__ == "__main__":
    main()
