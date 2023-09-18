import pygame # provides functionality for creating games and multimedia applications. 
import neat #evolutionary algorithm for evolving neural networks, commonly used for training AIs in various tasks.
import sys #
import os
import math
import random
from pygame.locals import *

from utils import *

local_dir = 'C:/Users/sagar/OneDrive/Desktop/MODELS/NEAT'## Enter your config directory here
config_path = os.path.join(local_dir, 'config.txt')
run(config_path)