import torch
import torch.nn as nn
import torchvision

class BlackNet(torch.nn.Module):
    def __init__(self):
        super(BlackNet, self).__init__()

        self.conv1 = torch.nn.Sequential(
                torch.nn.Conv2d(1, 32, kernel_size = 3, stride = 1, padding = 1),
                torch.nn.BatchNorm2d(32),
                torch.nn.ReLU(),
                torch.nn.Conv2d(32, 32, kernel_size = 3, stride = 1, padding = 1),
                torch.nn.BatchNorm2d(32),
                torch.nn.ReLU(),
                torch.nn.Conv2d(32, 32, kernel_size = 3, stride = 1, padding = 1),
                torch.nn.BatchNorm2d(32),
                torch.nn.ReLU(),
                torch.nn.Conv2d(32, 32, kernel_size = 3, stride = 1, padding = 1),
                torch.nn.BatchNorm2d(32),
                torch.nn.ReLU(),
                torch.nn.Conv2d(32, 32, kernel_size = 3, stride = 1, padding = 1),
                torch.nn.BatchNorm2d(32),
                torch.nn.ReLU() )

        self.input = torch.nn.Sequential(
                torch.nn.Linear(225, 225), 
                torch.nn.ReLU(),
                torch.nn.Linear(225, 256),
                torch.nn.ReLU(),
                torch.nn.Linear(256, 256),
                torch.nn.ReLU(),
                torch.nn.Linear(256, 289),
                torch.nn.ReLU(),
                torch.nn.Linear(289, 289),
                torch.nn.ReLU(),
                torch.nn.Linear(289, 324),
                torch.nn.ReLU(),
                torch.nn.Linear(324, 324),
                torch.nn.ReLU(),
                torch.nn.Linear(324, 324),
                torch.nn.ReLU(),
                torch.nn.Linear(324, 225) )
        
    def forward(self, x):
        x = self.input(x)
        return x