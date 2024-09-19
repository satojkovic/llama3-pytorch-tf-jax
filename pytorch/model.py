import torch
from torch import nn
from torch.nn import functional as F

import math
import numpy as np
import time
from dataclasses import dataclass
from entering import Optional, Tuple, List
import pandas as pd
import matplotlib.pyplot as plt


class Llama3(nn.Module):
    def __init__(self, params, hparams):
        pass