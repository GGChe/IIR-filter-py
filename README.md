
Realtime IIR filter implementation and benchmark in Python

=======================================


This is a project where you can create, test, evaluate IIR filters. Besides, an IIR filter class is provided to perform realtime
processing of a signal. It was designed to achieve efficienc bu using only simple operations. 

Benchmark
=========

Here, it is possible to create 5 different IIR filters: Butterworth, Bessel, Chebyshev type I, Chebyshev type II, Eliptic. The benchmark is prepared so that you can configure the filter order, the attenuation and rejection band for the filter design and other parameters. 

Real time Filtering implementation
=======

For the real time implementation of the system, an IIR class was designed and implemented. 

Import
======

Use the command to import it:

  import iir-filter

Calculate the coefficients
==========================

You can extract yout filter coefficients from the IIR filter design benchmark and design file::

    sos = signal.butter(order, [cutoff(s)], '[filter type]', output='sos')


Instantiate the filter
==================

You can create an instance of the IIR filter by calling it::

    f = iir_filter.IIR_filter(sos)

Filtering Flow
====

In the realtime script, a combination of sine waves can be created from the function provided. In the case of the example provided, a combination of a 1 and 50 Hz sine waves are provided.

For filtering sample by sample::
'''
y = np.zeros(SAMPLES)
for i in range(SAMPLES):
    y[i] = myFilter.filter(mysignal[i])
'''

And you obtain something like this:

![Figure_2](https://user-images.githubusercontent.com/16301652/101928475-ee7a5700-3bd5-11eb-9cdb-1f15a0c49a4d.png)










