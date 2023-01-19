
"""This module contains the CAMeL Tools Named Entity Recognition component.
"""

from helpers.helper import prepare_output
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
# from transformers import BertForTokenClassification, BertTokenizer
from helpers.constants import en_to_ar_camel
from camel_tools.ner import NERecognizer
import os 
import subprocess



if not os.path.exists('model/'):
        subprocess.call( 'mkdir model/', shell=True)
        print('============= MAKING  Model DIR ===============')


if not os.path.exists('model/camel'):
        subprocess.call( 'mkdir model/camel', shell=True)
        print('============= MAKING  Camel DIR ===============')

if not os.path.exists('model/ours'):
        subprocess.call( 'mkdir model/ours', shell=True)
        print('============= MAKING  Ours DIR ===============')



ner = NERecognizer.pretrained()

def test_camel(s):
    # Predict the labels of a single sentence.
    # The sentence must be pretokenized by whitespace and punctuation.
    sentence = s.split()

    labels = ner.predict_sentence(sentence)
    res = ''
    # Print the list of token-label pairs
    for token, label in zip(sentence, labels):
        if(label == 'O'):
            continue
        # print("{}\t{}".format(label, token))
        s = f"{en_to_ar_camel[label]}     {label}      {token}"
        res = res + s + '\n'
    return res , labels , sentence



