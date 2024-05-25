import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 1527061415 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # двухвыборочный критерий Колмогорова-Смирнова
    ks_statistic, p_value = ks_2samp(x, y)
    alpha = 0.07
    
    return p_value < alpha
