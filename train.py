import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os, sys
import pandas as pd
sys.path.append('utils')
from nets import *
# from datas import *
import os,sys
from PIL import Image
import scipy.misc
from glob import glob
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd


sample_dir = 'Samples/celebA_cgan_classifier_advance300/dia1:1'
ckpt_dir = 'Models/celebA_cgan_classifier_advance300/dia1:1'
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
if not os.path.exists(sample_dir):
    os.makedirs(sample_dir)
tf.reset_default_graph()
# param
n_class = 300
generator = G_dia()
discriminator = D_conv()
classifier = C_conv(n_class)

data = celebA(n_class)

# run

cgan_c = CGAN_Classifier(generator, discriminator , classifier, data, nclass = n_class)
cgan_c.train(sample_dir, ckpt_dir)
