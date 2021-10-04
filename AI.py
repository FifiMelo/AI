import math
import random
import data




sigmoid = lambda z: 1/(1 + math.e**(z * (-1)))
anti_sigmoid = lambda a: math.log(a/(1-a))

class Neuron:
    def __init__(self,z,y,index,L,output):      
        self.L = L
        self.z = z
        self.y = y
        self.j = 0
        self.bias = math.floor((random.random() - 0.5) * 10)
        self.a = sigmoid(self.z)
        self.index = index
        self.cost = (self.a - self.y)**2
        self.needed_bias = 0
        self.needed_weights = []
        self.weights = []
        if not output:
            for i in range(structure[self.L + 1]):
                self.weights.append((random.random() - 0.5) * 3)
                self.needed_weights.append(0)
        


    def load_input(self,value):  
        self.z = value
        self.a = sigmoid(self.z)

    def load_value(self):
        for x in layers[self.L - 1].neurons:
            self.z += x.a * x.weights[self.index]
        self.z += self.bias
        self.a = sigmoid(self.z)

    def calculate_y(self,right):
        if self.L:
            if self.L == len(structure) - 1:
                if self.index == right:
                    self.y = 1.0
                else:
                    self.y = 0.0
            else:
                for x in layers[self.L + 1].neurons:
                    self.y = (self.y * x.index - (x.cost/(2 * (x.a - x.y)*x.a*(1 - x.a)*self.weights[x.index])))/(x.index + 1)
            self.cost = (self.a - self.y)**2
    
    def calculate_weights_and_bias(self):
        print("calculating weights and bias for neuron L: " + str(self.L) + " index: " + str(self.index))
        if self.L:
            self.needed_bias = (self.j * self.needed_bias + (self.cost/(2 * (self.a - self.y) * self.a * (1 - self.a))))/(self.j + 1)
            for x in range(len(self.weights) - 1):
                self.needed_weights[x] = (self.j * self.needed_weights[x] + (self.cost/(2 * (self.a - self.y) * self.a * (1 - self.a) * layers[self.L - 1].neurons[x].a)))/(self.j + 1)
            self.j += 1
            if self.j == 10:
                self.j = 0
                print("zmiana bias z :" + str(self.bias) + " na: " + str(self.needed_bias))
                self.bias = self.needed_bias
                self.needed_bias = 0
                for x in range(len(self.weights) - 1):
                    self.weights[x] == self.needed_weights[x]
                    self.needed_weights[x] = 0




class Layer:
    def  __init__(self,size,L):
        self.L = L
        self.size = size
        self.neurons = []
        for x in range(size):
            a = Neuron((random.random() - 0.5) * 10,0.0,x,self.L,self.L == len(structure) - 1)
            self.neurons.append(a)
    def get_input(self, input):
        self.input = input
        if len(self.input) == self.size:
            for neuron in range(self.size):
                self.neurons[neuron].load_input(self.input[neuron])
        else:
            print("ERROR: bad input format: " + str(len(input)))





test = data.Input()


structure = [784,20,20,10]
layers = []

for i in range(len(structure)):
    layers.append(Layer(structure[i],i))

number = 5

for x in layers[len(structure) - 1].neurons:
    x.calculate_y(number)

for x in layers[len(structure) - 1].neurons:
    print(str(x.index) + ":\na: " + str(x.a) + "\ny: " + str(x.y) + "\ncost: " + str(x.cost))

print("__________________________________________")
for x in range(20):
    layers[len(structure) - 1].neurons[number].calculate_weights_and_bias

layers[len(structure) - 1].neurons[number].load_value()

for x in layers[len(structure) - 1].neurons:
    print(str(x.index) + ":\na: " + str(x.a) + "\ny: " + str(x.y) + "\ncost: " + str(x.cost))
