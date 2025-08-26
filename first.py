import numpy as np

def act(x):
    return 0 if x < 0.5 else 1


def go(house, rock, attr):
    x = np.array([house, rock, attr])
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]
    weight1 = np.array([w11, w12]) # matrix 2x3
    weight2 = np.array([-1,1])     # vec 1x2
    
    sum_hidden = np.dot(weight1, x) # calc hidden layer in_features sum
    print(f"Sum of neurons of hidden layer: {sum_hidden}") 
    
    
    out_hidden = np.array([act(x) for x in sum_hidden])
    print(f"Values at outs neurons of hidden layer {out_hidden}")
    
    sum_end = np.dot(weight2, out_hidden)
    y = act(sum_end)
    print(f"Output value of NN: {y}")
    return y

house = 1
rock = 1
attr = 1
print(f"input data: {[house, rock, attr]}")
res = go(house, rock, attr)

if res == 1:
    print("Ok")
else:
    print("Not ok")