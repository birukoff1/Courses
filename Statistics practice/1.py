import pandas as pd
import numpy as np
from scipy import stats

# Создадим датафрейм с данными о росте, весе и скоре игроков
df = pd.DataFrame({'player_number': [10, 8, 12, 22, 36, 7, 1, 20, 9, 4, 14],
 'height': [168, 176, 178, 191, 185, 183, 185, 179, 169, 183, 167],
 'weight': [76, 77, 79, 81, 82, 79, 74, 84, 73, 71, 68],
 'score': [95, 86, 94, 96, 95, 95, 89, 83, 99, 78, 82]})

mask_1 = df['score']>=4
mask_2 = df['score']<=8

a = df[mask_1*mask_2].var(ddof=1)

