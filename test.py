import data
import matplotlib.pyplot as plt
import numpy as np
import AI_sierpien2k21 as AI
import pickle




pkl_file = open('result1.pkl', 'rb')
data1 = pickle.load(pkl_file)
weights = data1["weights"]
biases = data1["biases"]

#print(weights)
pkl_file.close()

myAI = AI.NN([784,20,20,10])

myAI.weights = weights
myAI.biases = biases
print(len(biases[0][0]))
scanner = data.Input()
"""

x = scanner.get_input(654,False)
#x = np.dot(x,weights[0])
#x = np.add(x,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
#print(x)
print(myAI.give_answer(x))
#plt.imshow(np.array(scanner.get_input(654,False))
#plt.show()
"""

