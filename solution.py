import pandas as pd
import numpy as np


chat_id = 424771681 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
from statsmodels.stats.proportion import proportions_ztest
    p_value = proportions_ztest([x_success, y_success], [x_cnt, y_cnt])[1] / 2
    if (p_value < 0.1) and (x_success/x_cnt < y_success/y_cnt):
return True
    else:
        return False
