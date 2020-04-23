# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:22:36 2020

@author: HP
"""
import numpy as np
import queue
from relate_para import Node
from relate_para import Global
from relate_para import ModelError
GL=Global()
def para_check(key,value):
    if(key in GL.inttype):
        try:
            temp=int(value)
            if((key in GL.notzero and temp==0) or temp<0):
                raise ModelError('%s should be bigger than 0' % key)
        except:
            raise ModelError('%s should be int' % key)
    if(key in GL.doubletype):
        try:
            temp=float(value)
            if((key in GL.notzero and temp==0) or temp<0):
                raise ModelError('%s should be bigger than 0' % key)
        except:
            raise ModelError('%s should be double' % key)  
    if(key=='shape'):
        try:
            temp1 = list(map(int, value.split(',')))
            for i in temp1:
                try:
                    temp2=int(i)
                except:
                    raise ModelError('shape element should be int')
                if(temp2!=-1 and temp2<=0):
                    raise ModelError('shape element should be positive or be -1')
        except:
            raise ModelError('Invalid  shape')
def generate_model_static():
    ans = np.array([
                  'import os',
                  'import torch',
                  'import numpy as np',
                  'import torch.nn as nn',
                  'class VIEW(nn.Module):',
                  '    def __init__(self,*view):',
                  '        super(VIEW, self).__init__()',
                  '        self.temp=view',
                  '    def forward(self, x):',
                  '        return x.view(self.temp)',
                  '',
                  'class WISE_ADD(nn.Module):',
                  '    def __init__(self):',
                  '        super(WISE_ADD, self).__init__()',
                  '    def forward(self,*input):',
                  '        x=input[0]',
                  '        for i in range(1,len(input)):',
                  '            x.add_(input[i])',
                  '        return x',
                  '',
                  'class CHANNEL(nn.Module):' ,
                  '    def __init__(self,dim=1):',
                  '        super(CHANNEL, self).__init__()',
                  '        self.dim=dim',
                  '    def forward(self,*input):',
                  '         return torch.concat(*input,self.dim)',
                  ''
    	])
    return ans

def test(input):
    for i in input:
        print(i)
def add_sequential_layer(init_func,forward_func,out_data,layer_number,in_data,sequential_number):
    init=generate_n_tap(2) +'self.layer_'+str(layer_number)+'=sequential_'+str(sequential_number)+'()'
    forward= generate_n_tap(2) + out_data + ' = ' + 'self.layer_'+str(layer_number) + '(' + in_data + ')'
    init_func=np.append(init_func,init)
    forward_func=np.append(forward_func,forward)
    return init_func,forward_func
def add_modulelist_layer(init_func,forward_func,out_data,layer_number,in_data,modulelist_number):
    init=generate_n_tap(2) +'self.layer_'+str(layer_number)+'=modulelist_'+str(modulelist_number)+'()'
    forward= generate_n_tap(2) + out_data + ' = ' + 'self.layer_'+str(layer_number) + '(' + in_data + ')'
    init_func=np.append(init_func,init)
    forward_func=np.append(forward_func,forward)
    return init_func,forward_func
def add_moduledict_layer(init_func,forward_func,out_data,layer_number,in_data,moduledict_number):
    init=generate_n_tap(2) +'self.layer_'+str(layer_number)+'=moduledict_'+str(moduledict_number)+'()'
    forward= generate_n_tap(2) + out_data + ' = ' + 'self.layer_'+str(layer_number) + '(' + in_data + ')'
    init_func=np.append(init_func,init)
    forward_func=np.append(forward_func,forward)
    return init_func,forward_func
def add_element_wise_add_layer(init_func, forward_func, node, out_data,layer_number,graph):
    init=generate_n_tap(2) +'self.layer_'+str(layer_number)+'= WISE_ADD()'
    forward=generate_n_tap(2) + out_data + ' = ' + 'self.layer_'+str(layer_number) + '(' 
    if len(node.fa) == 0:
        raise ModelError('element_wise_add_layer has no inputs')
    parameter=graph[node.fa[0]].data
    for i in range(1, len(node.fa)):
         parameter = parameter + ', ' + graph[node.fa[i]].data 
    forward+=parameter+')'
    init_func=np.append(init_func,init)
    forward_func=np.append(forward_func,forward)
    return init_func,forward_func
def add_concatenate_layer(init_func, forward_func, node, out_data,layer_number,graph,nets):
    init=generate_n_tap(2) +'self.layer_'+str(layer_number)+'=CHANNEL('+nets['attribute']['attribute']['dim']+')'
    forward=generate_n_tap(2) + out_data + ' = ' + 'self.layer_'+str(layer_number) + '(' 
    if len(node.fa) == 0:
        raise ModelError('concatenate layer has no inputs')
    parameter=graph[node.fa[0]].data
    for i in range(1, len(node.fa)):
         parameter = parameter + ', ' + graph[node.fa[i]].data 
    forward+=parameter+')'
    init_func=np.append(init_func,init)
    forward_func=np.append(forward_func,forward)
    return init_func,forward_func
    
def add_layer_except_add_and_concate(init_func, forward_func, in_data, out_data, nets,layer_number):
    init=generate_n_tap(2) +'self.layer_'+str(layer_number)+'='+generate_base_info(nets)
    forward= generate_n_tap(2) + out_data + ' = ' + 'self.layer_'+str(layer_number) + '(' + in_data + ')'
    init_func=np.append(init_func,init)
    forward_func=np.append(forward_func,forward)
    return init_func,forward_func
def generate_variable_name(layer_count):
    return 'x_data_'+str(layer_count),layer_count+1
def generate_n_tap(n):
    ans = ''
    n = n * 4
    for i in range(n):
        ans = ans + ' '
    return ans
def attribute_generate(modulelist):
    output=''
    for i in modulelist.keys():
        if i not in GL.para_group:
            raise ModelError('in attribute_generate %s: No such attribute' % i)
        if(i=='type'or i=='layer_type'):
            continue
        para_check(i,modulelist[i])
        if(i in GL.para_str):
            output+=i+'=\''+modulelist[i]+'\','  
        else :output+=i+'='+modulelist[i]+','
    output=output[0:-1]
    return output
def pool_layer_generate(modulelist):
    head='nn.'
    if(modulelist['layer_type']=='max_pool'):
        head+='MaxPool'
    elif(modulelist['layer_type']=='avg_pool'):
        head+='AvgPool'
    elif(modulelist['layer_type']=='max_unpool'):
        head+='MaxUnpool'
    else:
        raise ModelError('in pool_layer_generate %s: No such pool layer' % modulelist['layer_type'])
    if(modulelist['attribute']['type'] not in GL.type):
        raise ModelError('in pool_layer_generate %s: No such type' % modulelist['attribute']['type'])
    head+=modulelist['attribute']['type']+'('
    head+=attribute_generate(modulelist['attribute'])+')'
    return head
def linear_layer_generate(modulelist):
    head='nn.Linear('
    head+=attribute_generate(modulelist)+')'
    return head
def view_layer_generate(modulelist):
    head='VIEW('
    head+=modulelist['shape']+')'
    return head
def conv_layer_generate(modulelist):
    head='nn.'
    if(modulelist['layer_type']=='conv'):
        head+='Conv'
    elif(modulelist['layer_type']=='conv_transpose'):
        head+='ConvTranspose'
    else:
        raise ModelError('in conv_layer_generate %s: No such conv layer' % modulelist['layer_type'])
    if(modulelist['attribute']['type'] not in GL.type):
        raise ModelError('in conv_layer_generate %s: No such type' % modulelist['attribute']['type'])
    head+=modulelist['attribute']['type']+'('
    head+=attribute_generate(modulelist['attribute'])+')'
    return head
def element_layer_generate(modulelist):
    head='WISE_ADD()'
    return  head
def concatenate_layer_generate(modulelist):
    head='CHANNEL('
    head+=attribute_generate(modulelist)+')'
    return head
def activation_layer_generate(modulelist):
    head='nn.'
    if(modulelist['layer_type']=='relu'):
        head+='ReLU'
    elif(modulelist['layer_type']=='sigmoid'):
        head+='Sigmoid'
    elif(modulelist['layer_type']=='tanh'):
        head+='Tanh'
    elif(modulelist['layer_type']=='leaky relu'):
        head+='LeakyReLU'
    elif(modulelist['layer_type']=='elu'):
        head+='ELU'
    elif(modulelist['layer_type']=='PRelu'):
        head+='PReLU'
    elif(modulelist['layer_type']=='RRelu'):
        head+='RReLU'
    else:
        raise ModelError('in activation_layer_generate %s: No such activate layer' % modulelist['layer_type'])
    head+='('
    if 'attribute' in modulelist:
        head+=attribute_generate(modulelist['attribute'])
    head+=')'
    return head
def softmax_layer_generate(modulelist):
    head='nn.Softmax('
    head+=attribute_generate(modulelist)+')'
    return head
def RNN_layer_generate(modulelist):
    head='nn.RNN('
    head+=attribute_generate(modulelist)+')'
    return head
def LSTM_layer_generate(modulelist):
    head='nn.LSTM('
    head+=attribute_generate(modulelist)+')'
    return head
def norm_layer_generate(modulelist):
    head='nn.'
    if(modulelist['layer_type']=='batch_norm'):
        head+='BatchNorm'
    elif(modulelist['layer_type']=='group_norm'):
        head+='GroupNorm'
    elif(modulelist['layer_type']=='instance_norm'):
        head+='InstanceNorm'
    if(modulelist['layer_type']!='group_norm'):
        if(modulelist['attribute']['type'] not in GL.type):
                raise ModelError('in norm_layer_generate %s: No such type' % modulelist['attribute']['type'])
        head+=modulelist['attribute']['type']
    else:
        raise ModelError('in norm_layer_generate %s: No such norm layer' % modulelist['layer_type'])
    head+='('+attribute_generate(modulelist['attribute'])+')'
    return head
def dropout_layer_generate(modulelist):
    head='nn.Dropout'
    if(modulelist['type'] not in GL.type):
        raise ModelError('in dropout_layer_generate %s: No such type' % modulelist['type'])
    if(modulelist['type']!='1d'):
        head+=modulelist['type']
    head+='('+attribute_generate(modulelist)+')'
    return head
def generate_base_info(modulelist):
    type=modulelist['attribute']['layer_type']
    
    if(type=='pool_layer'):
        return pool_layer_generate(modulelist['attribute']['attribute'])
    elif(type=='linear_layer'):
        return linear_layer_generate(modulelist['attribute']['attribute'])
    elif(type=='view_layer'):
        return view_layer_generate(modulelist['attribute']['attribute'])
    elif(type=='conv_layer'):
        return conv_layer_generate(modulelist['attribute']['attribute'])
    elif(type=='element_wise_add_layer'):
        return element_layer_generate(modulelist['attribute']['attribute'])
    elif(type=='concatenate_layer'):
        return concatenate_layer_generate(modulelist['attribute']['attribute'])
    elif(type=='activation_layer'):
        return activation_layer_generate(modulelist['attribute']['attribute'])
    elif(type=='softmax_layer'):
        return softmax_layer_generate(modulelist['attribute']['attribute'])
    elif(type=='RNN_layer'):
        return RNN_layer_generate(modulelist['attribute']['attribute'])
    elif(type=='LSTM_layer'):
        return LSTM_layer_generate(modulelist['attribute']['attribute'])
    elif(type=='norm_layer'):
        return norm_layer_generate(modulelist['attribute']['attribute'])
    elif(type=='dropout_layer'):
        return dropout_layer_generate(modulelist['attribute']['attribute'])
    else:
        raise ModelError('in generate_base_info %s: No such layer' % type)
        
def add_main_init_info():
    ans = np.array(['class NET(torch.nn.Module):', generate_n_tap(1) + 'def __init__(self):',
                    generate_n_tap(2) + 'super(NET, self).__init__()'])
    return ans
def add_other_init_info(kind):
    type=''
    if(kind=='sequential'):
        tempname='class sequential_'+str(GL.s_number)
        type='sequential_'+str(GL.s_number)
    elif(kind=='modulelist'):
        tempname='class modulelist_'+str(GL.ml_number)
        type='modulelist_'+str(GL.ml_number)
    elif(kind=='moduledict'):
        tempname='class moduledict_'+str(GL.dict_number)
        type='moduledict_'+str(GL.dict_number)
    else:
        raise ModelError('type %s doe not exist' % kind)
    ans = np.array([tempname+'(torch.nn.Module):', generate_n_tap(1) + 'def __init__(self):',
                    generate_n_tap(2) + 'super('+type+',self).__init__()'])
    return ans

def get_next_nodes_and_update_pre_nodes(nets, nets_conn, cur_id,graph,done):
    next_nodes = np.array([], dtype = str)
    fa_nodes = np.array([], dtype = str)
    flag = True

    for edge in nets_conn:
        if edge['source']['id'] == cur_id:
            next_nodes = np.append(next_nodes, edge['target']['id'])
            if edge['target']['id'] not in done.keys():
                graph[edge['target']['id']] = Node(id = edge['target']['id'])
                graph[edge['target']['id']].name = nets[edge['target']['id']]['type']
                if(nets[edge['target']['id']]['type']=='base'):
                    graph[edge['target']['id']].detailed_type=nets[edge['target']['id']]['attribute']['layer_type']
                done[edge['target']['id']] = False
        if edge['target']['id'] == cur_id:
            fa_nodes = np.append(fa_nodes, edge['source']['id'])
            if edge['source']['id'] not in done.keys() or not done[edge['source']['id']]:
            	flag = False
    graph[cur_id].next = next_nodes
    graph[cur_id].fa = fa_nodes
    if(nets[cur_id]['type']=='base'):
        temp_type=nets[cur_id]['attribute']['layer_type']
        if temp_type in GL.start_layer or temp_type not in GL.multi_layer:
            if temp_type == 'start' and len(graph[cur_id].fa) != 0:
                raise ModelError('start: can not have father nodes')
            elif temp_type != 'start' and len(graph[cur_id].fa) != 1:
                raise ModelError('%s: should have one and only one father node' % temp_type) 
    return next_nodes, flag

def make_graph(nets, nets_conn, init_func, forward_func):
    start_id=nets['in']
    end_id=nets['out']
    layer_number=0
    graph={}
    done={}
    layer_count=0
    Q = queue.Queue()
    graph[start_id] = Node(id = start_id, name = 'start', data = 'x_data')
    done[start_id] = True
    cur_id = start_id
    next_nodes, flag = get_next_nodes_and_update_pre_nodes(nets['nets'], nets_conn, cur_id,graph,done)
    for node_id in next_nodes:
        Q.put(node_id)
    while not Q.empty():
        cur_id = Q.get()
        if done[cur_id]:
            continue
        next_nodes, flag = get_next_nodes_and_update_pre_nodes(nets['nets'], nets_conn, cur_id,graph,done)
        if cur_id != start_id and flag is False:
            Q.put(cur_id)
            continue
        for node_id in next_nodes:
            Q.put(node_id)
        out_data,layer_count = generate_variable_name(layer_count)
        graph[cur_id].data = out_data
        if (nets['nets'][cur_id]['type']=='sequential'):
            sequential_number=GL.s_number+1
            in_data = graph[graph[cur_id].fa[0]].data
            add_sequential_net_info(nets['nets'][cur_id])     
            init_func,forward_func=add_sequential_layer(init_func,forward_func,out_data,layer_number,in_data,sequential_number)
        elif nets['nets'][cur_id]['type']=='modulelist':
            modulelist_number=GL.ml_number+1
            in_data = graph[graph[cur_id].fa[0]].data
            add_modulelist_net_info(nets['nets'][cur_id])   
            init_func,forward_func=add_modulelist_layer(init_func,forward_func,out_data,layer_number,in_data,modulelist_number)
        elif nets['nets'][cur_id]['type']=='moduledict':
            moduledict_number=GL.dict_number+1
            in_data = graph[graph[cur_id].fa[0]].data
            add_moduledict_net_info(nets['nets'][cur_id]) 
            init_func,forward_func=add_moduledict_layer(init_func,forward_func,out_data,layer_number,in_data,moduledict_number)
        elif nets['nets'][cur_id]['attribute']['layer_type'] == 'concatenate_layer':
            init_func, forward_func = add_concatenate_layer(init_func, forward_func, graph[cur_id], out_data,layer_number,graph,nets['nets'][cur_id])
        elif nets['nets'][cur_id]['attribute']['layer_type'] == 'element_wise_add_layer':
            init_func, forward_func = add_element_wise_add_layer(init_func, forward_func, graph[cur_id], out_data,layer_number,graph)
        elif nets['nets'][cur_id]['attribute']['layer_type'] == 'start':
            break
        elif nets['nets'][cur_id]['attribute']['layer_type'] == 'end':
            break
        else:
            in_data = graph[graph[cur_id].fa[0]].data
            init_func, forward_func = add_layer_except_add_and_concate(init_func, forward_func, in_data, out_data, nets['nets'][cur_id],layer_number)
        layer_number+=1
        done[cur_id] = True
    forward_func=np.append(forward_func,generate_n_tap(2)+'return '+graph[graph[end_id].fa[0]].data)
    return init_func, forward_func   
def add_main_net_info(canvas):
    GL.Model=generate_model_static()
    init_func = add_main_init_info()
    forward_func = np.array([generate_n_tap(1) + 'def forward(self, x_data):'])
    init_func, forward_func = make_graph(canvas['attribute'], canvas['nets_conn'], init_func, forward_func)
    result = np.concatenate((init_func,forward_func))
    GL.Model = np.concatenate((GL.Model, result))
    return
    
def add_sequential_net_info(canvas):
    GL.s_number+=1
    init_func = add_other_init_info('sequential')
    forward_func = np.array([generate_n_tap(1) + 'def forward(self, x_data):'])
    init_func, forward_func = make_graph(canvas['attribute'], canvas['nets_conn'], init_func, forward_func)
     #中间处理
    result = np.concatenate((init_func,forward_func))
    GL.Model = np.concatenate((GL.Model, result))
def modulelist_form(attribute,init_func,forward_func):
    modulelist_number=''
    modulelist_element=None
    init_head=''
    for i in attribute.keys():
        if(i=='num'):
            modulelist_number=attribute['num']
        else :
            modulelist_element=attribute[i]
    if(modulelist_element['type']=='sequential'):
        sequential_number=GL.s_number+1
        add_sequential_net_info(modulelist_element)
        init_head='sequential_'+str(sequential_number)+'()'
    elif(modulelist_element['type']=='modulelist'):
        modulelist_number=GL.ml_number+1
        add_modulelist_net_info(modulelist_element)
        init_head='modulelist_'+str(modulelist_number)+'()'
    elif(modulelist_element['type']=='moduledict'):
        moduledict_number=GL.dict_number+1
        add_moduledict_net_info(modulelist_element)
        init_head='moduledict_'+str(moduledict_number)+'()'
    elif(modulelist_element['type']=='base'):
        init_head=generate_base_info(modulelist_element)
    init_head=np.array([generate_n_tap(2)+'self.layer=nn.ModuleList(['+init_head+' for i in range('+modulelist_number+')])'])
    init_func=np.concatenate((init_func,init_head))
    line_first=np.array([generate_n_tap(2)+'for x,i in enumerate(self.layer):'])
    line_second=np.array([generate_n_tap(3)+'x_data=i(x_data)'])
    line_third=np.array([generate_n_tap(2)+'return x_data'])
    forward_func=np.concatenate((forward_func,line_first,line_second,line_third))
    return init_func,forward_func
def moduledict_form(attribute,init_func,forward_func):
    canvas_name={}
    #cavas
    canvas_inform={}
    default=None
    if('choose' in attribute and attribute['choose']!=None and attribute['choose']!=''):
        default=attribute['choose']
    else:
        default=attribute['default']
    nets_count=0
    for i in attribute['nets'].keys():
        head=''
        element=attribute['nets'][i]
        canvas_name[i]='layer_'+str(nets_count)
        if(attribute['nets'][i]['type']=='sequential'):
            sequential_number=GL.s_number+1
            add_sequential_net_info(element)
            head='sequential_'+str(sequential_number)+'()'
        elif(attribute['nets'][i]['type']=='modulelist'):
            modulelist_number=GL.ml_number+1
            add_modulelist_net_info(element)
            head='modulelist_'+str(modulelist_number)+'()'
        elif(attribute['nets'][i]['type']=='moduledict'):
            moduledict_number=GL.dict_number+1
            add_moduledict_net_info(element)
            head='moduledict_'+str(moduledict_number)+'()'
        elif(attribute['nets'][i]['type']=='base'):
            head=generate_base_info(element)
        canvas_inform[i]=head
        nets_count+=1
    init_head=np.array([generate_n_tap(2)+ 'self.choices = nn.ModuleDict({'])
    temp_count=0
    for i in canvas_name.keys():
        if(temp_count==len(canvas_name.keys())-1):
           temp=np.array([generate_n_tap(3)+'\''+canvas_name[i]+'\':'+canvas_inform[i]]) 
        else: 
            temp=np.array([generate_n_tap(3)+'\''+canvas_name[i]+'\':'+canvas_inform[i]+','])
        init_head=np.concatenate((init_head,temp))
        temp_count+=1
    init_func=np.concatenate((init_func,init_head,np.array([generate_n_tap(2)+'})'])))
    line_first=np.array([generate_n_tap(2)+'x_data=self.choices[\''+canvas_name[default]+'\'](x_data)'])
    line_second=np.array([generate_n_tap(2)+'return x_data'])
    forward_func=np.concatenate((forward_func,line_first,line_second))
    return init_func,forward_func
    
def add_modulelist_net_info(canvas):
    GL.ml_number+=1
    init_func = add_other_init_info('modulelist')
    forward_func = np.array([generate_n_tap(1) + 'def forward(self, x_data):'])
    init_func, forward_func = modulelist_form(canvas['attribute'], init_func, forward_func)
    #中间处理
    result = np.concatenate((init_func, forward_func))
    GL.Model = np.concatenate((GL.Model, result))
    return
def add_moduledict_net_info(canvas):
    GL.dict_number+=1
    init_func = add_other_init_info('moduledict')
    forward_func = np.array([generate_n_tap(1) + 'def forward(self, x_data):'])
    init_func, forward_func = moduledict_form(canvas['attribute'],init_func,forward_func)
    #中间处理
    result = np.concatenate((init_func, forward_func))
    GL.Model = np.concatenate((GL.Model, result))
    return
def model_output():
    fo=open("mytest.txt","w")
    for i in GL.Model:
        fo.write(i)
        fo.write('\n')
    fo.close()




base_start={
  "type": "base",
  "name": "base_start",
  "attribute": {
    "layer_type": "start",
  }
}
base_end={
  "type": "base",
  "name": "base_end",
  "attribute": {
    "layer_type": "end",
  }
}
base_pool={
  "name": "base_1",
  "attribute": {
    "layer_type": "pool_layer",
    "attribute": {
      "layer_type": "max_pool",
      "attribute": {
	    "type":"1d",
        "kernel_size": '2',
        "stride": '2',
        "padding": '0'
      }
    }
  }
}
base_concate= {
  "type": "base",
  "name": "base_2",
  "attribute": {
    "layer_type": "concatenate_layer",

    "attribute": {
		"dim":"1"
    }
  }
}
base_view= {
  "type": "base",
  "name": "base_3",
  "attribute": {
    "layer_type": "view_layer",

    "attribute": {
		"shape":"1,2,3,4"
    }
  }
}
base_element={

  "type": "base",
  "name": "base_4",
  "attribute": {
    "layer_type": "element_wise_add_layer",

  }
}
base_softmax={
  "type": "base",
  "name": "base_5",
  "attribute": {
    "layer_type": "softmax_layer",

    "attribute": {
		"dim":"1"
    }
  }

}
base_linear={
  "type": "base",
  "name": "base_6",
  "attribute": {
    "layer_type": "linear_layer",

    "attribute": {
		"in_channel":"1",
		"out_channel":"2"
    }
  }

}
base_conv={
  "type": "base",
  "name": "base_7",
     "attribute": {
      "layer_type": "conv_layer",
      "attribute": {
	  "layer_type":"conv",
	  "attribute": {
	  
        "type": "1d",
        "in_channel":"1",
		"out_channel":"2",
		"kernel_size":"3",
		"stride":"1",
		"padding":"0"
      }
    }
}
}
base_act={
  "type": "base",
  "name": "base_8",
     "attribute": {
      "layer_type": "activation_layer",
      "attribute": {
        "layer_type":"leaky relu",
		"attribute":{
		"negative_slope":"0.001"
      }
    }
}
}
base_RNN={
  "type": "base",
  "name": "base_9",
     "attribute": {
      "layer_type": "RNN_layer",
      "attribute": {
		"input_size":"5",
		"hidden_size":"10",
		"num_layers":"20",
		"nonlinearity":"tanh"
    }
}
}
base_LSTM={
  "type": "base",
  "name": "base_10",
     "attribute": {
      "layer_type": "LSTM_layer",
      "attribute": {
		"input_size":"5",
		"hidden_size":"10",
		"num_layers":"20"
    }
}
}
base_norm={
  "type": "base",
  "name": "base_10",
     "attribute": {
      "layer_type": "norm_layer",
      "attribute": {
		"layer_type":"batch_norm",
		"attribute":{
		"type":"1d",
		"num_features":"4"
    }
	}
}
}
modulelist1={
  "type": "modulelist",
  "name": "ml1",
  "attribute": {
    "canvas1": base_norm,
    "num": '10'
  }
}
moduledict1={
  "type": "moduledict",
  "name": "dict1",
  "attribute": {
    "default": "canvas_1",
    "choose": "canvas_2",
    "nets": {
      "canvas_1": base_linear,
      "canvas_2": base_RNN
    }
  }
}
sequential2={
  "type": "sequential",
  "name": "sequential2",
  "attribute": {
    "in": "canvas_1",
    "out": "canvas_13",
    "nets": {
      "canvas_1": base_start,
      "canvas_2": base_view,
	  "canvas_3":base_concate,
	  "canvas_4":base_act,
	  "canvas_5":base_element,
      "canvas_6":base_conv,
      "canvas_7":base_conv,
      "canvas_8":base_softmax,
      "canvas_9":base_RNN,
      "canvas_10":base_LSTM,
      "canvas_11":base_linear,
      "canvas_12":base_norm,
      "canvas_13":base_end
    }
	},
    "nets_conn": [
               {
             "source": {
                "id": "canvas_1"
             },
             "target": {
                 "id": "canvas_2"
             }
         },
		                {
             "source": {
                "id": "canvas_2"
             },
             "target": {
                 "id": "canvas_3"
             }
         },
		                {
             "source": {
                "id": "canvas_3"
             },
             "target": {
                 "id": "canvas_4"
             }
         },
		                {
             "source": {
                "id": "canvas_4"
             },
             "target": {
                 "id": "canvas_5"
             }
         }  ,		                {
             "source": {
                "id": "canvas_5"
             },
             "target": {
                 "id": "canvas_6"
             }
         },		                {
             "source": {
                "id": "canvas_6"
             },
             "target": {
                 "id": "canvas_7"
             }
         } ,		                {
             "source": {
                "id": "canvas_7"
             },
             "target": {
                 "id": "canvas_8"
             }
         },
             {
             "source": {
                "id": "canvas_8"
             },
             "target": {
                 "id": "canvas_9"
             }
         },
             		                {
             "source": {
                "id": "canvas_9"
             },
             "target": {
                 "id": "canvas_10"
             }
         },		{
             "source": {
                "id": "canvas_10"
             },
             "target": {
                 "id": "canvas_11"
             }
         },
                {
             "source": {
                "id": "canvas_11"
             },
             "target": {
                 "id": "canvas_12"
             }
         },		                {
             "source": {
                "id": "canvas_12"
             },
             "target": {
                 "id": "canvas_13"
             }
         }
    ]
  
}
sequential3={
  "type": "sequential",
  "name": "sequential3",
  "attribute": {
    "in": "canvas_1",
    "out": "canvas_10",
    "nets": {
      "canvas_1": base_start,
      "canvas_2": modulelist1,
	  "canvas_3":moduledict1,
	  "canvas_4":base_act,
      "canvas_5":sequential2,
      "canvas_7":base_concate,
      "canvas_8":base_element,
      "canvas_9":base_element,
	  "canvas_10":base_end
    }
	},
    "nets_conn": [
               {
             "source": {
                "id": "canvas_1"
             },
             "target": {
                 "id": "canvas_2"
             }
         },
		                {
             "source": {
                "id": "canvas_2"
             },
             "target": {
                 "id": "canvas_3"
             }
         },
		                {
             "source": {
                "id": "canvas_3"
             },
             "target": {
                 "id": "canvas_4"
             }
         },
		                {
             "source": {
                "id": "canvas_4"
             },
             "target": {
                 "id": "canvas_5"
             }
         }   ,
              {
             "source": {
                "id": "canvas_5"
             },
             "target": {
                 "id": "canvas_7"
             }
         } ,   {
             "source": {
                "id": "canvas_4"
             },
             "target": {
                 "id": "canvas_7"
             }
         } ,{
             "source": {
                "id": "canvas_5"
             },
             "target": {
                 "id": "canvas_8"
             }
         },{
             "source": {
                "id": "canvas_4"
             },
             "target": {
                 "id": "canvas_8"
             }
         },{
             "source": {
                "id": "canvas_7"
             },
             "target": {
                 "id": "canvas_9"
             }
         },{
             "source": {
                "id": "canvas_8"
             },
             "target": {
                 "id": "canvas_9"
             }
         },{
             "source": {
                "id": "canvas_9"
             },
             "target": {
                 "id": "canvas_10"
             }
         }
    ]
  
}
add_main_net_info(sequential3)
model_output()
