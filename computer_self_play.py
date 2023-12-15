from rule import *
from importlib import reload
import torch
import numpy as np
import os
import models.model
reload(models.model)
import models.whitemodel
reload(models.whitemodel)
import models.blackmodel
reload(models.blackmodel)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.model.SimpleNet().to(device)
white_model = models.whitemodel.WhiteNet().to(device)
black_model = models.blackmodel.BlackNet().to(device)

model.load_state_dict(torch.load("checkpoint/model.pth")['model'])
model.eval()

white_model.load_state_dict(torch.load("checkpoint/white.pth")['model'])
white_model.eval()

black_model.load_state_dict(torch.load("checkpoint/black.pth")['model'])
black_model.eval()

class Omok(object):
    def __init__(self):
        self.board = [[0 for i in range(board_size)] for j in range(board_size)]
        self.rule = Rule(self.board)
    
    def init_game(self):
        self.turn  = black_stone
        self.init_board()
        self.points = []
        self.id = 1
        self.is_gameover = False
        self.who_win = 0

    def init_board(self):
        for y in range(board_size):
            for x in range(board_size):
                self.board[y][x] = 0

    def draw_stone(self, point, stone, increase):
        self.board[point[1]][point[0]] = stone
        self.id += increase
        self.turn = 3 - self.turn

    def check_board(self, point):
        if self.board[point[1]][point[0]] != empty:
            print("occupied")
            self.turn = 3 - self.turn
            return True

        if self.turn == black_stone:
            if self.rule.forbidden_point(point[0], point[1], self.turn):
                print("forbidden point")
                return True

        self.points.append(point)
        self.draw_stone(point, self.turn, 1)
        if self.check_gameover(point, 3 - self.turn):
            self.is_gameover = True
        return True
    
    def check_gameover(self, point, stone):
        if self.id > board_size * board_size:
            self.show_winner_msg(stone)
            self.who_win = 0
            return True
        elif self.rule.is_gameover(point[0], point[1], stone):
            self.show_winner_msg(stone)
            self.who_win = stone
            return True
        return False
    
    def show_winner_msg(self, stone):
        pass

    def model_dicide(self, n = 1):
        board_tensor = torch.from_numpy(np.array(self.board)).float().to(device)
        board_tensor = board_tensor.reshape(-1)
        if self.turn == black_stone:
            output = black_model(board_tensor)
        else:
            output = white_model(board_tensor)
        output = output.detach().numpy()
        pos_points = self.rule.get_possible_points(self.turn)
        pos_points = np.array(pos_points).reshape(-1)
        output[~pos_points] = -1
        top_3_indices = output.argsort()[-n:][::-1]
        
        return top_3_indices
    
    def add_data(self,trained_level):
        file_path = os.path.join('omok_dataset', 'win_' + str(self.who_win), 'dataset_' + str(trained_level) + '.txt')
        a = [y * board_size + x for x, y in self.points]
        a = np.append(self.who_win, a)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(' '.join(map(str, a)))
        else:
            with open(file_path, 'a') as f:
                f.write('\n')
                f.write(' '.join(map(str, a)))