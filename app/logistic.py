import matplotlib.pyplot as plt
import numpy as np
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
def logistic_func():
  l=plt.imread("img.jpg").transpose(2,0,1)
  r=l[0,:,:].mean()
  g= l[1,:,:].mean()
  b = l[2,:,:].mean()
  print(b,g,r)
  theta = np.array([0.19409765, -0.46355493, -0.61552151,  0.75662993])
  #theta = np.array([-2.17299476, -0.06251461, -0.28642574,  0.28075228])
  X=np.array([1,b,g,r])
  z = np.dot(X, theta)
  prob = sigmoid(z)
  print(prob)
  if(prob>=.5):
    return("Laterite"+"\n"+"R:"+str(int(r))+" "+"G:"+str(int(g))+" " + "B:"+str(int(b))    )
  elif(prob<.5):
    return("Alluvial"+"\n"+str(int(r))+" "+str(int(g))+" " + str(int(b))   )
  else:
    return("none")
