import numpy as np;
import matplotlib.pyplot as plt
import csv;
import math;

def gradient_descent(W, alpha, data, prediction):
    W[2] = W[2] + alpha * (data[1] - predict) * data[0]*W[1]*pow(math.e, W[2]*data[0]);
    W[1] = W[1] + alpha * (data[1] - predict) * pow(math.e, W[2]*data[0]);
    W[0] = W[0] + alpha * (data[1] - predict) * 1;
    return W;

def showGraph(Data, W, Costs):
    x = np.arange(-5, 60, 0.1);
    y = W[0] + W[1]*pow(math.e, W[2] *x);

    plt.subplot(1,2,1);
    plt.plot(x, y);
    plt.grid(True);
    plt.plot(Data[:,0], Data[:,1], 'o');
    plt.title('y=w0+w1*e^(w2*x)');

    plt.subplot(1,2,2);
    plt.plot(Costs);
    plt.grid(True);
    plt.title('Costs');

    plt.show();

def loadData():
    dataset = np.array([]);
    with open('covid.csv') as f:
        reader = csv.reader(f)
        l = [[int(v) for v in row] for row in reader]
        dataset = l;
    return np.array(dataset);


epochs = 500000;
alpha = 0.0000000001;
W = np.array([[.0], [.0], [.0]]);
Costs = [];
data = loadData();

cost = 0.0;
for i in range(0, epochs):
    cost = 0.0;
    for j in range(0, len(data)):
        predict = W[0] + W[1]*pow(math.e, W[2] *data[j][0]);
        cost = cost + pow(data[j][1] -predict, 2);
        W = gradient_descent(W, alpha, data[j], predict);
    Costs.append(cost.tolist());

print("final cost: ", cost);
print("weight: ",W);
showGraph(data, W, Costs);