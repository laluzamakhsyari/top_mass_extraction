# top_mass_extraction

Simple code for extracting top quark mass for given cross sections and the histogram data

The program contains a detailed steps to compute/extract top quark mass for different observables given 
differential distributions based on the work of M. Work, et.all in [arXiv:1711.01831]

The folder contains (.txt) files which are tables for data of differential distributions for various observables.
The program is done in Wolfram Mathematica Notebook (.nb), that will automatically calculate the top quark mass, 
various statistical variables such as p-value, chi-square, mass shift and etc.

The program is divided for extracting different number of bins, i.e. 5 bins (_rebin.nb), 10 bins (_rebin_10.nb), 
20 bins (_null.nb)/default and for averaging observables that are taken from 2 different observables, i.e. (_ave.nb)

Python-based programs are also included for merging differential variables for various top quark mass for each of the
observables.
