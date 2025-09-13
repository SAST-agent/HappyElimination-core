import enum
from dataclasses import dataclass
import numpy as np

class Type(enum.Enum):
    ABNORMAL = 0  # 未正常启动
    AI = 1  # ai
    PLAYER = 2  # 播放器

MAX_ROUND = 5
SKILL_COST = 50
