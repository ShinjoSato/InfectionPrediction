import numpy as np;
import math;
import matplotlib.pyplot as plt;
import csv;

def sigmoid(x):
    return 1.0/(1.0 + pow(math.e, -x));

def cost_function(hw, y):
    if(y == 1): return -1*math.log(hw);
    else:       return -1*math.log(1-hw);

def gradient_descent(W, alpha, data, prediction):
    W[0] = W[0] + alpha * (data[2] - prediction);
    W[1] = W[1] + alpha * (data[2] - prediction) * pow(data[0], 1);
    W[2] = W[2] + alpha * (data[2] - prediction) * pow(data[1], 1);
    return W;

def showGraph(Data, W, Costs):
    x = np.arange(-5, 5, 0.1);
    # x2 = -(w0 +w1*x1)/w2
    y = -(W[0]+W[1]*x)/W[2];
    plt.subplot(1,2,1);
    plt.plot(x, y);
    plt.plot(Data[:,0], Data[:,1], 'o');

    plt.subplot(1,2,2);
    plt.plot(Costs);
    plt.show();

def loadData():
    dataset = np.array([]);
    with open('dataset02.csv') as f:
        reader = csv.reader(f)
        l = [[float(v) for v in row] for row in reader]
        dataset = l;
    return np.array(dataset);


alpha = 0.1;
epochs = 1000000;
data = loadData();
W = np.array([[.0], [.0], [.0]]);
Costs = [];
for i in range(0, epochs):
    cost = 0;
    for j in range(0, len(data)):
        prediction = sigmoid(W[0] + W[1]*data[j][0] + W[2]*data[j][1]);
        cost = cost_function(prediction, data[j][2]);
        W = gradient_descent(W, alpha, data[j], prediction);
    Costs.append(cost.tolist());
print(W);
showGraph(data, W, Costs);