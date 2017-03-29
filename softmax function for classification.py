import numpy as np
scores = [3.0,1.0,0.2]

def softmax(x):
    return np.exp(x)/np.sum(np.exp(x))

print(softmax(scores))