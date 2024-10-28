# -*- coding: utf-8 -*-
"""my_notebook.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lMZNNjey9SHllTaQ8unA2s9CLm4mqNjQ
"""

import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print(torch.__version__)

"""**Introduction to Tensors**

Creating tensors


"""

# scalar
scalar=torch.tensor(7)
scalar

scalar.ndim

scalar.item()

#vector
vector =torch.tensor([7,7])
vector

vector.ndim

vector.shape

# MATRIX
MATRIX=torch.tensor([[7,8],
                     [9,10]])
MATRIX

MATRIX.ndim

MATRIX[1]

MATRIX.shape

#TENSOR
TENSOR=torch.tensor([[[1,2,3],
                      [3,6,9],
                    [2,4,5]]])
TENSOR

TENSOR.ndim

TENSOR.shape

TENSOR[0]

"""### Random tensors"""

#Create a random tensirs of size(3,4)
random_tensor=torch.rand(3,4)
random_tensor

random_tensor.ndim

# Create a random tesnor with similar shape to an image tensor
random_image_size_tensor=torch.rand(size=(224,224,3))#height ,width ,colour channels(R,G,B)
random_image_size_tensor.shape,random_image_size_tensor.ndim

torch.rand(3,3)

"""### Zeros and ones"""

#Create a tensor of all zeros
zeros=torch.zeros(size=(3,4))
zeros

zeros*random_tensor

# Create a tensor of all ones
ones=torch.ones(size=(3,4))
ones

ones.dtype

random_tensor.dtype

"""### Creating a range of tensors and tensors-like"""

# use torch.range() and get deprecated message,use torch.arrange()
one_to_ten=torch.arange(start=0,end=100,step=10)
one_to_ten

torch.__version__

#Create tensors like
ten_zeros=torch.zeros_like(input=one_to_ten)
ten_zeros

ten_ones=torch.ones_like(input=one_to_ten)
ten_ones

"""##Tensor datatypes

"""

#Float 32 tensor
float_32_tensor=torch.tensor([3.0,6.0,9.0],dtype=None,#what dtype is tensor
                             device=None,#what device  is your tensor on
                             requires_grad=False )#whether or not to track gradients with this operation)
float_32_tensor.dtype

float_16_tensor=float_32_tensor.type(torch.float16)
float_16_tensor

float_16_tensor*float_32_tensor

int_32_tensor=torch.tensor([3,6,9],dtype=torch.int32)
int_32_tensor

float_32_tensor*int_32_tensor

"""Getting information form tensors

1.Tensors not right datatype-to do get datatype from a tensor,can use *tensor.dtype*

2.Tensors not right shape-to get shape from a tensor,can use *tensor.shape*

3.Tensors not on the right device from a tensor,can use *tensor.device*
"""

#Create a tensor
some_tensor=torch.rand(3,4)
some_tensor

#Find out details about some tensor
print(some_tensor)
print(f"Datatype of tensor: {some_tensor.dtype}")
print(f"Shape of tensor : {some_tensor.shape}")
print(f"Device tensor is on: {some_tensor.device}")

"""#Manipulating Tensors

Tensor operation include

*Addition

*Subtraction

*Multiplication(element-wise)

*Division

*Matrix Multiplication

"""

#Create a tensor
tensor=torch.tensor([1,2,3])
tensor+10

#Multiply tensor by 10
tensor*10

#Subtract
tensor-10

#Try out PyTorch in-built functions
torch.mul(tensor,10)

torch.add(tensor,10)

"""###Matrix Multiplication

Two main ways of perfroming multiplication in neural network and deep learning

 1.Element-wise multiplication

 2.Matrix multiplication(dot product)

 There are two rules that performing matrix multiplication needs to satisfy:
  
  1.The **inner dimension** must match:

  * '(3,2) @(3,2) won't work' (@= multiply)

  * '(2,3) @(3,2) will work'

  * '(3,2) @(2,3) will work'
   
   2.The resulting matrix has the shape of the ** outer dimesnions **

   * '(2,3)@(3,2)->(2,2)

"""

#Element wise multiplication

print(tensor,"*",tensor)
print(f"Equals: {tensor*tensor}")

#Matrix Multiplication
torch.matmul(tensor,tensor)

#Matrix multiplication by hand
1*1+2*2+3*3

# Commented out IPython magic to ensure Python compatibility.
# %%time
# value=0
# for i in range(len(tensor)):
#   value +=tensor[i]*tensor[i]
# print(value)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# torch.matmul(tensor,tensor)

"""### One Of The Most Common Error in deep learning:shape erros"""

# Shapes for matrix multiplication
tensor_A=torch.tensor([[1,2],
                      [3,4],
                      [5,6]])
tensor_B=torch.tensor([[7,10],
                       [8,11],
                       [9,12]])

#torch.mm(tensor_A, tensor_B)#torch.mm is the same as torch.matmul(it's an alias for writing less code)
torch.matmul(tensor_A,tensor_B)

tensor_A.shape, tensor_B.shape

"""To fix our tensor shape issues ,we can manipulate the shape of one of our tensors using a ** transpose ** switches the axes or dimensions of a given tensor.

  A ** transpose ** switches the axes or dimensions of a given tensor.
"""

tensor_B, tensor_B.shape

tensor_B.T,tensor_B.T.shape

#The matrix multiplication operation works when tensor_B is transposed
print(f"original shapes: tensor_A={tensor_A.shape},tensor_B={tensor_B.shape}")
print(f"New shapes: tensor_A={tensor_A.shape},tensor_B.T={tensor_B.T.shape}")
print(f"Multiplying:{tensor_A.shape} @ {tensor_B.T.shape} <-inner dimensions must match")
print("Output:\n")
Output=torch.matmul(tensor_A,tensor_B.T)
print(Output)
print(f"\nOutput shape:{Output.shape}")

"""### Finding the min,max,mean,sum,etc(tensor aggregation)"""

#Create a tensor
x = torch.arange(0,100,10)
x

#Find the min
torch.min(x),x.min()

#Find the max
torch.max(x),x.max()

#Find the mean-note:the torch.mean() fucntion recquires a tensor of float32 datatype to work
torch.mean(x.type(torch.float32)),x.type(torch.float32).mean()

#Find the sum
torch.sum(x),x.sum()

"""### Finding the positional min and max"""

#Find the position in tensor that has the minimum value with argmin() ->returns index  position of target tensor where the minimum value occurs
x.argmin()

x[0]

#find the position in tensor that has the maximum value with argmax()
x.argmax()

x

x[9]

"""## Reshaping,stacking,squeezing and unsqueezing tensors

* Reshaping - reshapes an input tensor to a defined shape

* View-a view of an input tensor of certain shape but keep the same memory as the original tensor

* Stacking - combine multiple tensors on top of each other (vstack) or side by side (hstack)

* squeeze- removes all '1' dimensions fro a tensor

* unsqueeze- add a'1' dimensions to a target tensor
  
* permute - return a view of the input with dimensions permuted(swapped) in a certain way
"""

#Let's create a tensor
import torch
x=torch.arange(1.,10.)
x,x.shape

#Add an extra dimensions
x_reshaped= x.reshape(1,9)
x_reshaped,x_reshaped.shape

#Change the view
z= x.view(1,9)
z,z.shape

#changing z changes x because the view of a tensor shares the same memory as the originalinput
z[:,0]=5
x,z

#stack tensors on top of each other
x_stacked =torch.stack([x,x,x,x],dim=1)
x_stacked

#torch.squeexe()- removes all dimensions from target tensor
print(f"previous tensor: {x_reshaped}")
print(f"previous shape:{x_reshaped.shape}")
 #Remove extra dimensions from x_reshaped
x_squeezed=x_reshaped.squeeze()
print(f"\nNew tensor:{x_squeezed}")
print(f"New shape:{x_squeezed.shape}")

#torch.uunsqueeze()- adds a single dimensions to a target tensors at specific dimensions
print(f"previous target:{x_squeezed}")
print(f"previous shape:{x_squeezed.shape}")
 #Add an extra dimension with unsqueee
x_unsqueezed=x_squeezed.unsqueeze(dim=0)
print(f"\nNew tensor:{x_unsqueezed}")
print(f"New shape: {x_unsqueezed.shape}")

#torch.permute -rearanges the dimensions of the target tensor in a specified order
x_original =torch.rand(size=(224,224,3)) #height,width,color_channels
#permute the original tensor to rearrange the axis (or dim) order
x_permuted=x_original.permute(2,0,1)#shifts 0->1,1->2,2->0
print(f"previous shape:{x_original.shape}")
print(f"New shape:{x_permuted.shape}")#color_channel,height,width

x_original[0,0,0]=728218
x_permuted[0,0,0],x_original[0,0,0]

"""#Indexing (selecting data from tensors)
Indexing with Pytorch is similar to indexing with Numpy

"""

#Create a tensor
import torch
x=torch.arange(1,10).reshape(1,3,3)
x,x.shape

#Let's index on our new tensor
x[0]

#Let's index on the middle bracket(dim=1)
x[0][0]

#Let's index on the most inner bracket (last dimension)
x[0][0][0]

x[0][2][2]

#You can also use":" to select "all" of a target dimension
x[:,0]

#Get all values of 0th and 1st dimensions but only index1 of 2nd dimensions
x[:,:,1]

#Get all values of the 0 dimension but only 1 index value of 1st and 2nd dimension
x[:,1,1]

#Get index 0  of 0th and 1st dimension and all values of 2nd dimension
x[0,0,:]

#Index on x to return 9
x
#Index on x to return 3,6,9

x[0,2,2]

x[:,:,2]

"""#Pytorch tensors and numpy
Numpy is a popular scientific python numerical computing library.

And because of this PyTorch has functionality to interact with it.

* Data in Numpy,want in PyTorch tensor-.torch.from_numpy(ndarray)

* PyTorch tensor->Numpy->torch.Tensor.numpy()
"""

#Numpy array to tensor
import torch
import numpy as np
array =np.arange(1.0,8.0)
tensor=torch.from_numpy(array)# warning : when converting from numoy ->pytorch,ptorch reflects numpy's default datatype of float64 unless specified otherwise
array,tensor

#change the value of an array,what will do to 'tensor'
array=array+1
array,tensor

#tensor to numpy array
tensor=torch.ones(7)
numpy_tensor=tensor.numpy()
tensor,numpy_tensor

#change the tenaor ,what happens to 'numpy_tensor'
tensor=tensor+1
tensor,numpy_tensor

"""## Reproducbility(trying to take random out of random)

In short how a neural networks learns:

 'start with random numbers-> tensor operations-> update random numbers to try and make them better representations of data -> again -> again->..

 To reduce the randomness in neural networks and pytorch comes the concept of a ** random seed**

 Essentially what the random seed does is"flavour" the randomness.

"""

import torch
#Create two random tensors
random_tensor_A=torch.rand(3,4)
random_tensor_B=torch.rand(3,4)
print(random_tensor_A)
print(random_tensor_B)
print(random_tensor_A==random_tensor_B)

#Let's make some random but reproducible tensors
import torch
#Set the random seed
RANDOM_SEED=42
torch.manual_seed(RANDOM_SEED)
random_tensor_C=torch.rand(3,4)
torch.manual_seed(RANDOM_SEED)
random_tensor_D=torch.rand(3,4)
print(random_tensor_C)
print(random_tensor_D)
print(random_tensor_C==random_tensor_D)

"""## Running tensors and pytorch objects on the GPUs ( and making faster computations)

GPUS= faster computation ,thanks to CUDA+NVIDIA hardware +PyTirch working behind the scenes to make everything hunky dory(good).

### Getting a GPU

Easiest--Use Google colab for a free GPU (options to upgrade as well)
"""

### Check for GPU access with PyTorch
import torch
torch.cuda.is_available()

#Setup device agnostic code
device="cuda" if torch.cuda.is_available() else"cpu"
device

"""Putting tensors (and models) on the GPU

 The reason we want our tensors/models on the GPU is because using GPU results in faster computations.
"""

#Create a tensor (default on the CPU)
tensor=torch.tensor([1,2,3],device="cpu")

#Tensor not on GPU
print(tensor,tensor.device)

#Move tensor to GPU(if available)
tensor_on_gpu=tensor.to(device)
tensor_on_gpu

"""### Moving tensors back to cpu"""

#If tensors is on GPU ,can't transform it to Numpy
tensor_on_gpu.numpy()

