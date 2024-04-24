import sys
import torch
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
print(f'Welcome to Torch,\nYou are using version {sys.version}')
print(f'PyTorch version {torch.__version__}')

## Introduction to Tensors
# Scalar
# source: https://pytorch.org/docs/stable/tensors.html
scalar = torch.tensor(17)
print(f'Scalar is {scalar}')
print(f'scaral has {scalar.ndim} dimenstions')
print(f'scalar content is {scalar.item()}')
print(f'scalar shape is {scalar.shape}')

# Vector
vector = torch.tensor([3,4])
print(f'"vector" has dimension of {vector.ndim}')
print(f'"vector" content is [{vector[0].item()}, {vector[1].item()}]')
print(f'"vector" shape is {vector.shape}')

# matrix
matrix = torch.tensor([[3,4],[5,6]])
print(f'"matrix" has dimension of {matrix.ndim}')
print(f'"matrix" content is [{matrix[0][0].item()}, {matrix[0][1].item()}]')
print(f'"matrix" shape is {matrix.shape}')

# tensor
tens = torch.tensor([[[6,7,8,9],
                      [8,7,6,5],
                      [3,2,1,7]]])
print(f'"tens" has dimension of {tens.ndim}')
print(f'"tens" content is [{tens}]')
print(f'"tens" shape is {tens.shape}')

tens2 = torch.tensor([[[6,7,8,9],[8,7,6,5],[3,2,1,7]],[[16,17,18,19],[81,17,16,15],[13,12,11,71]]])
print(f'"tens2" has dimension of {tens2.ndim}')
print(f'"tens2" content is [{tens2}]')
print(f'"tens2" shape is {tens2.shape}')
