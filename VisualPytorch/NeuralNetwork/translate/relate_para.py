# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:07:47 2020

@author: HP
"""
import numpy as np
class Global:
    def __init__(self):
        self.s_number=0
        self.ml_number=0
        self.dict_number=0
        self.model=np.array([])
        self.para_str={'ceil_mode','count_include_pad','nonlinearity'}
        
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