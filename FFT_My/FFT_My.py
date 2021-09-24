#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 22:21:31 2021

@author: luzhiwei
"""

import matplotlib.pyplot as plt 
import numpy as np 
def show(ori_func, ft, sampling_period = 5000): 
    n = len(ori_func) 
    print(n)
    interval = sampling_period / n 
   
    plt.subplot(2, 1, 1) 
    plt.plot(np.arange(0, sampling_period, interval), ori_func, 'black') 
    plt.xlabel('Time steps(x1000)'), plt.ylabel('Amplitude') 

    plt.subplot(2,1,2) 
    frequency = np.arange(n / 2) / (n * interval) 
    nfft = abs(ft[range(int(n / 2))] / n ) 
    plt.plot(frequency, nfft, 'red') 
    plt.xlabel('Freq (Hz)'), plt.ylabel('Amp. Spectrum') 
    plt.show() 
    
 
x = np.loadtxt('M_y.txt')
y = np.fft.fft(x) 
show(x,y)
