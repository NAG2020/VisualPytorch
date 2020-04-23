# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:07:47 2020

@author: HP
"""
import numpy as np
class ModelError(Exception):
    def __init__(self, erro_info):
        super().__init__(self)
        self.error_info = erro_info

    def __str__(self):
        return self.error_info
class Global:
    def __init__(self):
        self.s_number=0
        self.ml_number=0
        self.dict_number=0
        self.model=np.array([])
        self.para_str={'ceil_mode','count_include_pad','nonlinearity'}
        self.para_group={'shape','in_channel','out_channel','dim','type','p','layer_type',
                         'kernel_size','stride','padding','ceil_mode','count_include_pad',
                         'negative_slope','weight','lower','upper','input_size',
                         'hidden_size','num_layers','nonlinearity','num_features','num_groups','num_channel'}
        self.inttype={'in_channel','out_channel','dim','kernel_size','stride','padding','input_size','hidden_size','num_layers',
                      'num_features','num_groups','num_channel'}
        self.doubletype={'p','negative_slope','weight','loser','upper'}
        self.type={'1d','2d','3d'}
        self.notzero={'in_channel','out_channel','kernel_size','stride','weight','lower','upper','negative_slope',
                      'input_size','hidden_size','num_layers','num_features','num_groups','num_channel'}
        self.start_layer = ['start']
        self.multi_layer = ['element_wise_add_layer', 'concatenate_layer']
class Node:
	#记录了单个神经网络层的属性以及连接情况
    def __init__(self, id = None, name = None,data=None,detailed_type=None):
                self.fa = np.array([], dtype = str)
		#在生成图中的父节点
                self.next = np.array([], dtype = str)
		#在生成图中的子节点
                self.id = id
		#节点ID，格式canvas_%d
                self.name = name
		#记录所属哪种层
                self.data = data
		#神经网络层在forward中对应的输出数据变量名
       
                self.detailed_type=detailed_type
       
    def add_fa(self, f):
	#增加父节点
    	self.fa = np.append(self.fa, f)
    def add_next(self, nx):
    	self.next = np.append(self.next, nx)