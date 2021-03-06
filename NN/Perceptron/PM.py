import numpy as np
import matplotlib.pyplot as plt
import matplotlib
class PM(object):
    def __init__(self):


    def _init_W(self, size = ( 2, 1 ) ):
        self.W = 0.02 * np.random.random(size)

    def _init_B(self, size= ( 1 ) ):
        self.B = 0.02 * np.random.random(size)

    def _get_data(self, size = ( 100,2 ) ):
        self.data = 100 * np.random.random(size)-50
        self.label = ( np.dot(self.data,np.array([1,0.3])) + 0.2 ) > 0
        # set label as 1 or -1 
        self.label = self.label * 2 -1

    def train(self, iter = 100):
        '''
        return a bool that indicates whether it converged.
        '''
        self._init_W()
        self._init_B()
        self._get_data()
        flag = 0
        for step in range(iter):
            phi = np.dot(self.data, self.W) + self.B
            phi = phi * self.label
            for t in range(100):
                i =int ( np.random.random(1) * 100 )
                if phi[i,0] < 0:
                    self.W = self.W + 0.001 * self.data[i].reshape(2,1) * self.label[i]
                    self.B = self.B + 0.001 * self.label[i]
                    val = self.evaluate()
                    if val == 0:
                        # to jump out of the second loop
                        flag = 1
                        break
                if flag == 1:
                    break
        
        if flag == 0 : 
            return False
        else:
            return True
        
    def evaluate(self):
        return  ( ( (np.dot( self.data, self.W) + self.B[0] ).reshape( 100 ) > 0 ) != ( self.label > 0 ) ).sum()
    
    def Visualize(self,f = 1, saveImage = True):
        fg = plt.figure(f)
        idx_1 = self.label==1
        p1 = plt.scatter(self.data[idx_1,1], self.data[idx_1,0],marker='x', color = 'm', label = '1',s=30)
        idx_2 = self.label==-1
        p2 = plt.scatter(self.data[idx_2,1], self.data[idx_2,0],marker='+', color = 'c', label = '2',s=50)
        p3 = plt.plot([50,-50],[-0.3*50-0.2,0.3*50-0.2 ],color = 'b')
        if f != 1:
            p4 = plt.plot([50,-50],[(-50*self.W[1,0]-self.B[0])/self.W[0,0],(50*self.W[1,0]-self.B[0])/self.W[0,0]],color = 'r')
        if saveImage == True:
            plt.savefig(str(f)+'.jpg',format='jpg')
        else:
            plt.show()



if __name__ == '__main__':
    pm = PM()
    count = 0
    for i in range (1000):
        count = count + pm.train()
    print ( count )
    #pm.Visualize()
