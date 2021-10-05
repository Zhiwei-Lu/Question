import matplotlib.pyplot as plt 
import numpy as np 
def show(ori_func, ft, sampling_period = 5001*1E-18*100): 
    n = len(ori_func) 
   
    interval = sampling_period / n 
    print(interval)
    plt.subplot(2, 1, 1) 
    plt.plot(np.arange(0, sampling_period, interval), ori_func, 'black') 
    plt.xlabel('Time steps'), plt.ylabel('Amplitude') 

    plt.subplot(2,1,2) 
    frequency = np.arange(n / 2-1) / (n * interval) 
    plt.xlim(0,0.4*1E14)
    nfft = abs(ft[range(int(n / 2))] / n ) 
    plt.plot(frequency, nfft, 'red') 
    plt.xlabel('Freq (Hz)'), plt.ylabel('Amp. Spectrum') 
    plt.show() 
    
 
x = np.loadtxt('M_y.txt')
x=x
y = np.fft.fft(x) 
show(x,y)
