import gzip
import numpy as np



class Input:
    def __init__(self):
        
        
        self.num_images = 60000
        self.image_size = 28

    def get_input(self,index,training = True):
        if training:
            self.pictures = gzip.open('train-images-idx3-ubyte.gz','rb')
        else:
            self.pictures = gzip.open('t10k-images-idx3-ubyte.gz','rb')
        if index >= self.num_images: 
            print("ERROR: picture array out of range")
            return 0
        self.pictures.read(16 + self.image_size**2 * index)
        self.data = self.pictures.read(self.image_size**2)
        self.data = np.frombuffer(self.data, dtype=np.uint8).astype(np.float32)
        self.data = self.data.reshape(self.image_size * self.image_size)
        self.pictures.close()
        return self.data


    def get_answer(self,index,training = True):
        if training:
            self.answer = gzip.open('train-labels-idx1-ubyte.gz','rb')
        else:
            self.answer = gzip.open('t10k-labels-idx1-ubyte.gz','rb')
        if index >= self.num_images: 
            print("ERROR:answer array out of range")
            return 0
        self.answer.read(8 + index)
        self.data = self.answer.read(1)
        self.data = np.frombuffer(self.data, dtype=np.uint8).astype(np.float32)
        self.output = int(self.data)
        self.answer.close()
        return self.output



