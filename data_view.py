import pygame as pg

n = 0 # n번째 줄을 가져올 것입니다. 0을 입력하면 제일 최신 데이터를 가져옵니다.
filename = 'omok_dataset/win_2/dataset_0.txt'  # 파일 이름입니다. (파일이 존재해야 합니다.)
with open(filename, 'r') as file:
    lines = file.readlines()
line = lines[n-1].strip()
data = [int(item)+1 for item in line.split(' ')][1:]

pg.init()
board_color = (204, 153, 000)
bg_color = (128, 128, 128)
black = (0, 0, 0)
blue = (0, 50, 255)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
window_size = [800,500]
board_eight = 500
board_size = 15
grid_size = 30
black_stone = 1
white_stone = 2
clock = pg.time.Clock()
done = False
screen = pg.display.set_mode(window_size)
pg.display.set_caption("Omok game")
button = 0
position = 0
late_data = len(data)
screen.fill(bg_color)
board = pg.image.load("image/board.png")
board = pg.transform.scale(board, (500, 500))
screen.blit(board, [0,0])
arrow = pg.image.load("image/arrow.png")
arrow = pg.transform.scale(arrow, (300, 100))
screen.blit(arrow, [500,400])
White_Ston = pg.image.load("image/white.png")
White_Ston = pg.transform.scale(White_Ston, (27, 27))
Black_Ston = pg.image.load("image/black.png")
Black_Ston = pg.transform.scale(Black_Ston, (27, 27))
mark = pg.image.load("image/mark.png")
mark = pg.transform.scale(mark, (150, 80))

while not done:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if 520<pg.mouse.get_pos()[0]<562 and 430<pg.mouse.get_pos()[1]<472:
                button = 1
            if 593<pg.mouse.get_pos()[0]<633 and 430<pg.mouse.get_pos()[1]<472:
                button = 2
            if 664<pg.mouse.get_pos()[0]<708 and 430<pg.mouse.get_pos()[1]<472:
                button = 3
            if 738<pg.mouse.get_pos()[0]<781 and 430<pg.mouse.get_pos()[1]<472:
                button = 4
        if event.type == pg.QUIT:
            done=True
    if button == 3 and not position == late_data:
        position += 1
    if button == 2 and not position == 0:
        position -= 1
    if button == 1:
        position = 0
    if button == 4:
        position = late_data
    if not button == 0:
        screen.blit(board, [0,0])
        for i in range(position):
            if i%2:
                screen.blit(White_Ston, [28+30*((data[i]-1)//15),447-30*((data[i]-1)%15)])
                if i == position-1:
                    screen.blit(mark, [36+30*((data[position-1]-1)//15),448-30*((data[position-1]-1)%15)])
            else:
                screen.blit(Black_Ston, [28+30*((data[i]-1)//15),447-30*((data[i]-1)%15)])
                if i == position-1:
                    screen.blit(mark, [36+30*((data[position-1]-1)//15),448-30*((data[position-1]-1)%15)])
    button = 0
    pg.display.flip()

pg.quit()