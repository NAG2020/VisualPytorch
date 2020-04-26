# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:05:24 2020

@author: HP
"""
import numpy as np
# import model_generate as mog
# import main_generate as mag
from .model_generate import  add_main_net_info
from .main_generate import add_main_info
def all_generate(dict_input):
    main=None
    module=add_main_net_info(dict_input["canvas"][0])
    main=add_main_info(dict_input["static"])
    return main,module
'''
def main_output(main):
    fo=open("test_main.txt","w")
    for i in main:
        fo.write(i)
        fo.write('\n')
    fo.close()
def module_output(model):
    fo=open("test_module.txt","w")
    for i in model:
        fo.write(i)
        fo.write('\n')
    fo.close()'''


