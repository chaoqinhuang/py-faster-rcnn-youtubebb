# Scheduling script for automatically running faster-rcnn

from subprocess import call
import sys
from os import listdir
from os.path import isfile, join

vers_to_run = [6,65,66,67,68,69,71,42,43,36,37]

for index in range(0,len(vers_to_run)):

  call('rm -rf data/VOCdevkit2007',shell=True)

  call('ln -s /datasets/voc-2007/v'+
       str(vers_to_run[index])+
       ' data/VOCdevkit2007',shell=True)

  print('\nRunning with Version '+str(vers_to_run[index])+'\n')

  call('./experiments/scripts/faster_rcnn_alt_opt.sh 0 '+
       'VGG_CNN_M_1024 pascal_voc --set EXP_DIR foobar '+
       'RNG_SEED 42 > log_'+str(vers_to_run[index])+'.txt',shell=True)

