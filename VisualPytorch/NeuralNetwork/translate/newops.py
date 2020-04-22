# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:22:36 2020

@author: HP
"""
s_number=0
ml_number=0
dict_number=0
model=''
def attribute_generate(modulelist):
    output=''
    for i in modulelist.keys():
        output+=i+'='+modulelist[i]+','
    output=output[0:-1]
    return output
def pool_layer_generate(modulelist):
    head='nn.'
    if(modulelist['layer_type']=='max_pool'):
        head+='MaxPool'
    else if(modulelist['layer_type']=='avg_pool'):
        head+='AvgPool'
    else if(modulelist['layer_type']=='max_unpool'):
        head+='MaxUnpool'
    head+=modulelist['type']+'('
    head+=attribute_generate(modulelist['type'])+')'
    return head
def linear_layer_generate(modulelist):
    
def generate_base_info(modulelist):
    type=modulelist['attribute']['layer_type']
    if(type=='pool_layer'):
        return pool_layer_generate(modulelist['attribute'])
    else if(type=='linear_layer'):
        return linear_layer_generate(modulelist['attribute'])
    else if(type=='view_layer'):
        return view_layer_generate(modulelist['attribute'])
    else if(type=='conv_layer'):
        return conv_layer_generate(modulelist['attribute'])
    else if(type=='element_wise_add_layer'):
        return element_layer_generate(modulelist['attribute'])
    else if(type=='concatenate_layer'):
        return concatenate_layer_generate(modulelist['attribute'])
    else if(type=='activation_layer'):
        return activation_layer_generate(modulelist['attribute'])
    else if(type=='softmax_layer'):
        return softmax_layer_generate(modulelist['attribute'])
    else if(type=='RNN_layer'):
        return RNN_layer_generate(modulelist['attribute'])
    else if(type=='LSTM_layer'):
        return LSTM_layer_generate(modulelist['attribute'])
    else if(type=='norm_layer'):
        return norm_layer_generate(modulelist['attribute'])
    else if(type=='dropout_layer'):
        return dropout_layer_generate(modulelist['attribute'])
    else:
        
def add_main_init_info():
    ans = np.array(['class NET(torch.nn.Module):', generate_n_tap(1) + '#init function', generate_n_tap(1) + 'def __init__(self):',
                    generate_n_tap(2) + 'super(NET, self).__init__()'])
def add other_init_info(kind):
    if(kind==sequential):
        tempname='class sequential_'+str(s_number)
    if(kind==modulelist):
        tempname='class modulelist_'+str(ml_number)
    if(kind==module_dict):
        tempname='class moduledict_'+str(dict_number)
    ans = np.array([tempname,'(torch.nn.Module):', generate_n_tap(1) + '#init function', generate_n_tap(1) + 'def __init__(self):',
                    generate_n_tap(2) + 'super(','tempname',',self).__init__()'])
    return ans
def generate_n_tap(n):
    ans = ''
    n = n * 4
    for i in range(n):
        ans = ans + ' '
    return ans
def add_main_net_info(canvas):
    init_func = add__main_init_info()
    forward_func = np.array([generate_n_tap(1) + 'def forward(self, x_data):'])
    init_func, forward_func = make_graph(canvas['attribute'], canvas['nets_conn'], init_func, forward_func)
    result = np.concatenate((init_func, np.append(forward_func, ret_state)))
    Model = np.concatenate(Model, result)
    return
    
def add_sequential_net_info(canvas):
    init_func = add_other_init_info('Sequential')
    forward_func = np.array([generate_n_tap(1) + 'def forward(self, x_data):'])
    init_func, forward_func = make_graph(canvas['attribute'], canvas['nets_conn'], init_func, forward_func)
     #中间处理
    result = np.concatenate((init_func, np.append(forward_func, ret_state)))
    Model = np.concatenate(Model, result)
    return
def modulelist_form(attribute,init_func,forward_func):
    modulelist_number=0
    modulelist_element=None
    for i in attribute.keys():
        if(i==nums):
            modulelist_number=int(attribute[nums])
        else 
            modulelist_element=attribute[i]
    if(modulelist[type]=='sequential'):
        s_number+=1
        add_sequential_net_info(modulelist_element)
        
    else if(modulelist[type]=='modulelist'):
        ml_number+=1
        add_modulelist_net_info(modulelist_element)
    else if(modulelist[type]=='moduledict'):
        dict_number+=1
        add moduledict_net_info(moduledict_element)
     else if(modulelist[type]=='base'):
        
def add_modulelist_net_info(canvas):
    init_func = add_other_init_info('modulelist')
    forward_func = np.array([generate_n_tap(1) + 'def forward(self, x_data):'])
    init_func, forward_func = modulist_form(canvas['attribute'], init_func, forward_func)
    #中间处理
    result = np.concatenate((init_func, np.append(forward_func, ret_state)))
    Model = np.concatenate(Model, result)
    return
def add_moduledict_net_info(canvas):
    init_func = add_other_init_info('moduledict')
    forward_func = np.array([generate_n_tap(1) + 'def forward(self, x_data):'])
    init_func, forward_func = moduledict_form(canvas['attribute'],init_func,forward_func)
    #中间处理
    result = np.concatenate((init_func, np.append(forward_func, ret_state)))
    Model = np.concatenate(Model, result)
    return
