
"""
Created on Feb 28 2019
@author: J. C. Vasquez-Correa
        Pattern recognition Lab, University of Erlangen-Nuremberg
        Faculty of Engineering, University of Antioquia,
        juan.vasquez@fau.de
"""

import numpy as np
import pandas as pd

class Phonological:

    def __init__(self):

        self.list_phonological={"vocalic" : ["IY", "IH", "EH", "AE", "UW", "AX", "AH", "AA", "UH", "OY", "AA", "OW", "EY"],
                      "consonantal" : ["F", "V", "TH", "DH", "S", "Z", "SH", "ZH", "HH", "H", "P", "B", "Y", "D", "K", "G", "CH", "JH", "W", "R", "RX", "Y", "Z", "M", "N", "NX", "NG", "Q"],
                      "back"        : ["UW", "AH", "OY", "AA"],
                      "near-back"   : ["UH"],
                      "central"     : ["AX"],
                      "near-front"  : ["IH"],
                      "front"       : ["IY", "EH", "AE", "AA"],
                      "open"        : ["AA"],
                      "near-open"   : ["AE"],
                      "mid-open"    : ["AH", "OY"],
                      "mid-close"   : ["EH", "AX"],
                      "near-close"  : ["IH", "UH"],
                      "close"       : ["IY", "UW"],
                      "nasal"       : ["M", "N", "NX", "NG"],
                      #"stop"        : ["p","b", "B","t","k","g", "G","tS","d", "D"],
                      #"continuant"  : ["f", "F","b", "B","tS","d", "D","s", "Z", "T","x", "jj", "J","g", "G","S","L","x", "jj", "J", "z"],
                      "lateral"     :["L"],
                      "flap"        :["RX"],
                      #"trill"       :["rr"],
                      "voice"       :["IY", "IH", "EH", "AE", "UW", "AX", "AH", "AA", "UH", "OY", "AA", "V", "DH", "Z", "ZH", "B", "D", "G", "JH", "W", "R", "RX", "Y", "L", "M", "N", "NX", "NG"],
                      "voiceless"   :["F", "TH", "S", "SH", "HH", "H", "P", "K","T", "CH", "Q"],
                      "fricative"   :["F", "V", "TH", "DH", "S", "Z", "SH", "ZH", "HH", "H"],
                      "plosive"     :["G", "P", "B", "T", "D", "K", "G","Q"],
                      "affricate"   :["CH", "JH"],
                      "approximant" :["W", "R", "Y"],
                      "lateral-approximant":["L"],
                      "flap"        :["RX"],
                      "nasal"       :["M", "N", "NX", "NG"],
                      "labiodental" :["F", "V"],
                      "dental"      :["TH", "DH"],
                      "alveolar"      :["S", "Z", "T", "D", "R", "RX", "L", "N"],
                      "alveopalatal":["SH", "ZH", "CH", "JH"],
                      "glottal"     :["HH", "H", "Q"],
                      "bilabial"    :["P", "B", "M", "W"],
                      "velar"       :["K", "G", "NG", "NX"],
                      "pause"       :  ["sil", "<p:>", "sp"]}


    def get_list_phonological(self):
        return self.list_phonological

    def get_list_phonological_keys(self):
        keys=self.list_phonological.keys()
        return list(keys)

    def get_d1(self):
        keys=self.get_list_phonological_keys()
        dict_1={"xmin":[],"xmax":[],"phoneme":[],"phoneme_code":[]}
        for k in keys:
            dict_1[k]=[]
        return dict_1

    def get_d2(self):
        keys=self.get_list_phonological_keys()
        dict_2={"n_frame":[],"phoneme":[],"phoneme_code":[]}
        for k in keys:
            dict_2[k]=[]
        return dict_2

    def get_list_phonemes(self):
        keys=self.get_list_phonological_keys()
        phon=[]
        for k in keys:
            phon.append(self.list_phonological[k])
        phon=np.hstack(phon)

        return np.unique(phon)


def main():
    phon=Phonological()
    keys=phon.get_list_phonological_keys()
    print(keys)
    d1=phon.get_d1()
    print(d1)
    d2=phon.get_d2()
    print(d2)
    ph=phon.get_list_phonemes()
    print(ph)

if __name__=="__main__":
    main()


