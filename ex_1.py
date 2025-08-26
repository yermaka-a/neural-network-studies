import numpy as np


def act(x):
    return 1 if x >= 0.5 else 0


def go(color, shape, taste):
    attrs = [color, shape, taste]
    w11 = [1, 0.3, 0.2]
    w12 = [-0.5, 0.3, 0.4]
    out_w = [1, -1]
    weights = np.array([w11, w12])
    
    hidden_val = np.dot(weights, attrs)
    print(f"Values of hidden layer: {hidden_val}")
    
    act_val = np.array([act(x) for x in hidden_val])
    print(f"Values of act_fn of hidden layer: {act_val}")
    
    out = np.dot(act_val, out_w)
    print(f"Out values: {out}")
    return out


color = 0 # (1-red 0-orange)
shape = 1 # 1-circle 0-oblong
taste = 0 # (1-sweet 0-sour)

# orange or apple

res = go(color, shape, taste)

if res == 1:
    print("apple")
else:
    print("orange")