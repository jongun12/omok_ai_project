import os
import numpy as np
from PIL import Image
import torch
from torchvision import datasets, transforms
from torch.utils import data

# data loader for Omok dataset
class OmokDataset(data.Dataset):

    def __init__(self, dataset_root, who_win, level, mode=-1, transform=None): # level: 모델 트레이닝 횟수, mode: 기보 n 번째
        super(OmokDataset, self).__init__()

        self.dataset_root = dataset_root
        self.who_win = who_win
        self.mode = mode
        self.level = level
        self.transform = transform

        self.omok_notations = []
        self.n_ans = []

        file_path = os.path.join(dataset_root, 'win_' + str(who_win), 'dataset_' + str(level) + '.txt')

        # read txt file
        with open(file_path, 'r') as f:
            lines = f.readlines()

            for line in lines:
                self.board = [0 for i in range(15*15)]
                line_split = line.split(' ')
                
                self.who_win = int(line_split[0]) # 0: 무승부, 1: 흑돌 승리, 2: 백돌 승리
                value = 1
                for i in line_split[1:self.mode]:
                    self.board[int(i)] = value
                    value = 2 if value == 1 else 1
                self.omok_notations.append(self.board[:])
                self.n_ans.append(int(line_split[self.mode]))

    def __len__(self):
        return len(self.n_ans)
    
    def __getitem__(self, index):
        omok_notation = np.array(self.omok_notations[index])
        ans = torch.tensor(self.n_ans[index], dtype=torch.long)

        if self.transform is not None:
            omok_notation = self.transform(omok_notation)
        else:
            omok_notation = torch.from_numpy(omok_notation)

        return omok_notation, ans