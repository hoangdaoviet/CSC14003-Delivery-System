import pygame
import time
from agent import *

board = Board('input0_level2.txt')
# hiện tại hàm BFS đang được thêm 2 dòng sleep(1) nên code sẽ chạy chậm, tạm thời không dùng cái này
# agent = PlayerLvl1()
# path = agent.BFS(board)

#screen
WIDTH, HEIGHT = 1280, 720

#color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

pygame.init()
pygame.display.set_caption("Searching")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# đây sẽ là bản đồ cho các level
# vẽ 1 lưới ô vuông mà vị trí góc trên bên trái là (startX, startY)
# kích thước là width * height (ô), mỗi ô mặc định có kích thước là 50x50 (pixel)
def drawGrid(coloredMap, startX, startY, width, height, blockSize=50):
    for i in range(width):
        for j in range(height):
            pygame.draw.rect(screen, BLACK, (startX + i*blockSize, startY + j*blockSize, blockSize, blockSize), 1)

# Nếu cần vẽ bất cứ cái gì có thể đem bỏ vào hàm draw() này
def draw():
    screen.fill(WHITE)
    drawGrid(board.coloredMap, 50, 50, board.n, board.m)
    pygame.display.update()

# vòng lặp chính, dùng để chạy chương trình. không cần phải sửa gì ở đây nếu như không có vấn đề gì
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw()

pygame.quit()