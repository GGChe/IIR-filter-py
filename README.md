=======================================

Realtime IIR filter implementation and benchmark in Python

=======================================


This is a project where you can create, test, evaluate IIR filters. Besides, an IIR filter class is provided to perform realtime
processing of a signal. It was designed to achieve efficienc bu using only simple operations. 

Import
======

Use the standard python command to import it::

  import iir-filter


Calculate the coefficients
==========================

Use your favourite scipy IIR design command and export the coefficients as an SOS::

    sos = signal.butter(order, [cutoff(s)], '[filter type]', output='sos')



Create an instance
==================

The constructor takes the sos chain as an argument::

    f = iir_filter.IIR_filter(sos)



Perform filtering sample by sample
==================================

Filtering is sample by sample by processing the samples
as they arrive, for example from an ADC::

   sample = f.filter(sample)
=======
This is a IIR filter benchmark for filter design and realtime implementation on python

![Figure_1](https://user-images.githubusercontent.com/16301652/101923507-c0921400-3bcf-11eb-8acf-90d4f809ab89.png)

