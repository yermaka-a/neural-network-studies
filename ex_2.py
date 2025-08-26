import numpy as np


def act(x):
    return 1 if x >= 0.5 else 0


def go(jenre, duration, main_ch):
    x = [jenre, duration, main_ch]
    w11 = [0.3, 0.4, 0.7]
    w12 = [0.3, 0.4, 0.2]
    weight1 = np.array([w11, w12])
    weight2 = np.array([1, -1])
    
    sum_hidden = np.dot(weight1, x)
    print(sum_hidden)
    hidden_vals = np.array([act(x) for x in sum_hidden])
    out_sum = np.dot(hidden_vals, weight2)
    out_act = act(out_sum)
    print(f"Out act value: {out_act}")
    return out_act

jenre = 1
duration = 1
main_ch = 0

res = go(jenre, duration, main_ch)

if res == 1:
    print("favorite")
else:    
    print("UNfavorite")