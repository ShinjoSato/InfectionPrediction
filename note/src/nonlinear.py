import numpy as np;
import matplotlib.pyplot as plt
import csv;

def gradient_descent(W, alpha, data, prediction):
    W[0] = W[0] + alpha * (data[1] - predict) * pow(data[0], 0);
    W[1] = W[1] + alpha * (data[1] - predict) * pow(data[0], 1);
    W[2] = W[2] + alpha * (data[1] - predict) * pow(data[0], 2);
    return W;

def showGraph(Data, W, Costs):
    x = np.arange(-100, 100, 0.1);
    y = W[0]+W[1]*x+W[2]*x*x;

    plt.subplot(1,2,1);
    plt.plot(x, y);
    plt.plot(Data[:,0], Data[:,1], 'o');

    plt.subplot(1,2,2);
    plt.plot(Costs);

    plt.show();

def loadData():
    dataset = np.array([]);
    with open('dataset01.csv') as f:
        reader = csv.reader(f)
        l = [[int(v) for v in row] for row in reader]
        dataset = l;
    return np.array(dataset);


epochs = 500000;
alpha = 0.000000001;
W = np.array([[.0], [.0], [.0]]);
Costs = [];
data = loadData();
for i in range(0, epochs):
    cost = 0.0;
    for j in range(0, len(data)):
        predict = W[0] * pow(data[j][0], 0) + W[1] * pow(data[j][0], 1) + W[2] * pow(data[j][0], 2);
        cost = cost + pow(data[j][1] -predict, 2);
        W = gradient_descent(W, alpha, data[j], predict);
    Costs.append(cost.tolist());
print(W);
showGraph(data, W, Costs);
