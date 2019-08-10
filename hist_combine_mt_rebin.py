#!/usr/bin/python2

from __future__ import division

import matplotlib.pyplot as plt
import numpy as np


np.seterr(divide='ignore', invalid='ignore')

fig=plt.figure(figsize=(6.5,5))
grid=plt.GridSpec(3, 1, hspace= 0.3, wspace=0.4)
ax1=fig.add_subplot(grid[:2, 0])
ax2=fig.add_subplot(grid[2,0], sharex=ax1) #define grid axes 

#with open('number.txt', 'r') as n:
 #       nhist=int(n.read())

def extract(data1, start_value, length):
    return np.transpose(data1[start_value:start_value+length])
    
class Hist(object):
    def __init__(self, title,  xlabel, ylabel, start, nbins, left, right):
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.start = start
        self.nbins = nbins
        self.left = left
        self.right = right
        
       
    def plot_combine(self, data1, data_com, label=None):

        (x, val) = extract(data1, self.start, self.nbins)
        (x_C, val_C)= extract(data_com, self.start, self.nbins)
    
        vals, bins, patches = ax1.hist(x, weights=val, linestyle='-', histtype="step", label=label, 
        bins=self.nbins, range=(self.left, self.right))
        bin_centers = list(map(lambda (a,b): a+(b-a)/2, zip(bins,bins[1:])))
        color = patches[0].get_edgecolor()
        ax1.legend(loc=0,prop={'size':4})
   #     ax1.semilogy()
      #  ax1.grid(True)
        #plt.title(self.title)
        #ax1.xlabel(self.xlabel)
        ax1.set_ylabel(self.ylabel)
        
        vals1, bins1, patches1 = ax2.hist(x, weights = val/val_C, linestyle='-', histtype="step", bins=self.nbins, range=(self.left, self.right)) #plot histogram
        bin_centers = list(map(lambda (a,b): a+(b-a)/2, zip(bins,bins[1:]))) #histogram properties
        color = patches[0].get_edgecolor()
      #  ax2.legend()
      #  ax2.grid(True)
        #plt.title(self.title)
        ax2.set_xlabel(self.xlabel)
        ax2.set_ylabel("Ratio to 173,2 GeV")
        ax2.set_ylim(0.5,1.5)



        
def main():
    
    varname = ["Mttbar", "PTt_ave", "PTbbar", "Mb1b2_ave", "Me+b1", "Me+b2", "Me+mu-", "min(Me+b1_Me+b2)", "PTb1", "PTb2", "PTb_ave", "PTe+", "PTmu-", "PTl_ave", "PTe+mu-", "PTe+b1", "PTe+b2", "PT_miss", "yt_ave", "yb_ave", "ye+", "ymu-", "yl_ave", "yttbar", "ybbar", "kdeltaRb1b2", "kdeltaRe+mu-", "kdeltaRe+b1", "kdeltaRe+b2", "kdeltaRmu-b1", "kdeltaRmu-b2", "kdeltaRttbar","y_e+mu-","PTl1", "PTl2", "yl1", "yl2"]
    mass = ["168,2", "170,7", "173,2", "175,7", "178,2"]
    numb =10
    rebin=20
    data=[]
    data_compare=np.loadtxt("/scratch/work/zam/top_mass_extraction/mathematica/kdata_{}_{}_173,2_mt.txt" .format(varname[numb],rebin))

        
    
      
    hists = [
        Hist("inv_ttbar_mass", "$M_{t\\bar{t}}$ [GeV]","$1/\sigma d\sigma/dM_{t\\bar{t}}$ [fb/GeV]", 0,rebin, 300,1500),
        Hist("trans_mom_t_averaged", "$p_{T,t}$ [GeV]", "$1/\sigma d\sigma/dp_{T,t}$ [fb/GeV]",0, rebin, 0, 400),
        Hist("trans_mom_bbbar", "$p_{T, b\\bar{b}}$ [GeV]", "$1/\sigma d\sigma/dp_{T, b\\bar{b}}$ [fb/GeV]", 0, rebin, 0,400),
        Hist("inv_b1b2_mass_average", "$M_{b\\bar{b}}$ [GeV]","$1/\sigma d\sigma/dM_{b_1 b_2}$ [fb/GeV]", 0, rebin, 0, 400),
        Hist("inv_eplus_b1_mass", "$M_{e^+b_1}$ [GeV]", "$1/\sigma d\sigma/dM_{e^+b_1}$ [fb/GeV]",81, 20, 0,200),
        Hist("inv_eplus_b2_mass", "$M_{e^+b_2}$ [GeV]", "$1/\sigma d\sigma/dM_{e^+b_2}$ [fb/GeV]",101, 20, 0,200),
        Hist("inv_eplus_muminus_mass", "$M_{e^+\mu^-}$ [GeV]", "$1/\sigma d\sigma/dM_{e^+\mu^-}$ [fb/GeV]",0,rebin, 0,200),
        Hist("min(eplus_b1_mass, eplus_b2_mass)", "$min(M_{e^+b_1},M_{e^+b_2})$ [GeV]", "$1/\sigma d\sigma/dmin$ [fb/GeV]",0,rebin, 0,200),
        Hist("trans_mom_b1", "$p_{T, b_1}$ [GeV]", "$1/\sigma d\sigma/dp_{T,b_1}$ [fb/GeV]",0,rebin, 0, 400),
        Hist("trans_mom_b2", "$p_{T,b_2}$ [GeV]", "$1/\sigma d\sigma/dp_{T,b_2}$ [fb/GeV]", 0,rebin, 0, 400),
        Hist("trans_mom_b_averaged", "$p_{T,b}$ [GeV]", "$1/\sigma d\sigma/dp_{T,b}$ [fb/GeV]", 0,rebin, 0, 400),
        Hist("trans_mom_eplus"," $p_{T,e^+}$ [GeV]", "$1/\sigma d\sigma/dp_{T,e^+}$ [fb/GeV]", 221, 20, 0, 200),
        Hist("trans_mom_muminus", "$p_{T,\mu^-}$ [GeV]", "$1/\sigma \sigma/dp_{T,\mu^-}$ [fb/GeV]", 241, 20, 0, 200),
        Hist("trans_mom_lepton_averaged", "$p_{T, l}$ [GeV]", "$1/\sigma \sigma/dp_{T,l}$ [fb/GeV]", 0,rebin, 0, 200),
        Hist("trans_mom_eplus_muminus"," $p_{T,e^+\mu^-}$ [GeV]", "$1/\sigma d\sigma/dp_{T,e^+\mu^-}$ [fb/GeV]", 0,rebin, 0, 200),
        Hist("trans_mom_eplus_b1"," $p_{T,e^+b_1}$ [GeV]", "$1/\sigma d\sigma/dp_{T,e^+b_1}$ [fb/GeV]", 0,rebin, 0, 200),
        Hist("trans_mom_eplus_b2"," $p_{T,e^+b_2}$ [GeV]", "$1/\sigma d\sigma/dp_{T,e^+b_2}$ [fb/GeV]", 0,rebin, 0, 200),
        Hist("trans_mom_miss", "$p_{T,miss}$ [GeV]", "$1/\sigma \sigma/dP_{T,miss}$ [fb/GeV]", 0,rebin, 0, 200),
        Hist("rapidity_t_averaged", "$y_t$", "$1/\sigma d\sigma/dy_t$ [fb]", 361, 20, -3, 3),
        Hist("rapidity_b_averaged", "$y_b$", "$1/\sigma d\sigma/dy_b$ [fb]", 381, 20, -3, 3),
        Hist("rapidity_eplus", "$y_{e^+}$", "$1/\sigma d\sigma/dy_{e^+}$ [fb]", 401, 20, -3, 3),
        Hist("rapidity_muminus", "$y_{\mu^-}$", "$1/\sigma d\sigma/dy_{\mu^-}$ [fb]", 421, 20, -3, 3),
        Hist("rapidity_lepton_averaged", "$y_l$", "$1/\sigma d\sigma/dy_l$ [fb]", 0,rebin, -3, 3),
        Hist("rapidity_ttbar", "$y_{t\\bar{t}}$", "$1/\sigma d\sigma/dy_{t\\bar{t}}$ [fb]", 461, 20, -3, 3),
        Hist("rapidity_bbbar", "$y_{b\\bar{b}}$", "$1/\sigma d\sigma/dy_{b\\bar{b}}$ [fb]", 481, 20, -3, 3),
        Hist("deltaR_b1b2", "$\Delta R_{b_1 b_2}$", "$1/\sigma d\sigma/d\Delta R_{b_1, b_2}$ [fb]", 501, 20, 0.5, 4),
        Hist("deltaR_eplusmuminus", "$\Delta R_{e^+ \mu^-}$", "$1/\sigma d\sigma/d\Delta R_{e^+, \mu^-}$ [fb]", 0,rebin, 0, 4),
        Hist("deltaR_eplusb1", "$\Delta R_{e^+ b_1}$", "$1/\sigma d\sigma/d\Delta R_{e^+, b_1}$ [fb]", 541, 20, 0, 4),
        Hist("deltaR_eplusb2", "$\Delta R_{e^+ b_2}$", "$1/\sigma d\sigma/d\Delta R_{e^+, b_2}$ [fb]", 561, 20, 0, 4),
        Hist("deltaR_muminusb1", "$\Delta R_{\mu^- b_1}$", "$1/\sigma d\sigma/d\Delta R_{\mu^-, b_1}$ [fb]",581, 20, 0, 4),
        Hist("deltaR_muminusb2", "$\Delta R_{\mu^- b_2}$", "$1/\sigma d\sigma/d\Delta R_{\mu^-, b_2}$ [fb]", 601, 20, 0, 4),
        Hist("deltaR_ttbar", "$\Delta R_{t\\bar{t}}$", "$1/\sigma d\sigma/d\Delta R_{t\\bar{t}}$ [fb]",621, 20, 3, 4),
        Hist("rapidity_eplusmuminus", "$y_{e^+ \mu^-}$", "$1/\sigma d\sigma/dy_{e^+ \mu^-}$ [fb]",0, rebin, -3, 3),
        Hist("trans_mom_{l_1}"," $p_{T,l_1}$ [GeV]", "$1/\sigma d\sigma/dp_{T,l_1}$ [fb/GeV]", 0, rebin, 0,200),
        Hist("trans_mom_{l_2}"," $p_{T,l_2}$ [GeV]", "$1/\sigma d\sigma/dp_{T,l_2}$ [fb/GeV]", 0, rebin, 0,200),
        Hist("rapidity_{l_1}", "$y_l1$", "$1/\sigma d\sigma/dy_{l_1}$ [fb]",0,rebin, -3, 3),
        Hist("rapidity_{l_2}", "$y_l2$", "$1/\sigma d\sigma/dy_{l_2}$ [fb]",0,rebin, -3, 3)
        ]
    
        
    for k in xrange(len(mass)):
        data.append(np.loadtxt("/scratch/work/zam/top_mass_extraction/mathematica/kdata_{}_{}_{}_mt.txt" .format(varname[numb], rebin, mass[k])))
     
        hists[numb].plot_combine(data[k], data_compare, label="LO, {} GeV".format(mass[k]))
        
    plt.legend()
    plt.savefig("rebin_{}_{}_mt.pdf" .format(rebin,hists[numb].title))
    plt.close()
    
    

    
if __name__ == "__main__":
    main()
