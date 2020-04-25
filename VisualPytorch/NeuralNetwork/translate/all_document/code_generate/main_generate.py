import numpy as np
def add_main_info(load_dict):
    code_str=np.array([
        'import os',
        'import numpy as np',
        'import torch',
        'import torchvision',
        'import torch.utils.data as Data',
        'from torchvision import transforms',
        'from model import NET',
        'import torch.optim as optim'
    ])
    
    code_str = np.append(code_str,'epoch = %s\n' % load_dict['epoch'])
    code_str = np.append(code_str,'learning_rate = %s\n' % load_dict['learning_rate'])
    code_str = np.append(code_str,'batch_size = %s\n' % load_dict['batch_size'])
    if load_dict['if_shuffle'] == 'False':
        code_str = np.append(code_str,'if_shuffle=False')
    else:
        code_str = np.append(code_str,'if_shuffle=True')
    if load_dict['platform'] == 'gpu':
        code_str = np.append(code_str,'if_gpu=True\n')
    else:
        code_str = np.append(code_str,'if_gpu=False\n')
    code_str =np.concatenate((code_str,
    np.array(['train_loader=None',
    'test_loader=None',
    'train = True',
    'DOWNLOAD_MNIST = False',
    'num_work=0',
    'trainset=None',
    'testset=None',
    'optimizer=None',
    'loss_func=None',
    'average = None',
    'var = None',
    'device = torch.device("cuda:0" if torch.cuda.is_available() and if_gpu else "cpu")',
    'net = NET().to(device)'])))
    
    
    optimizer = load_dict['optimizer']['name']
    optimizer_attr = load_dict['optimizer']['attribute']
    if optimizer == 'Adam':
        temp_str=''
        temp_str+='optimizer = torch.optim.Adam(net.parameters(), lr=learning_rate, betas=(%s' % optimizer_attr['beta1']
        temp_str+= ',%s)' % optimizer_attr['beta2']
        temp_str+= ', eps=%s' % optimizer_attr['eps']
        temp_str+= ', weight_decay=%s' % optimizer_attr['weight_decay']
        temp_str+= ', amsgrad=%s)\n' % optimizer_attr['amsgrad']
        code_str=np.append(code_str,temp_str)
    elif optimizer == 'SGD':
        temp_str=''
        temp_str+= 'optimizer = optim.SGD(net.parameters(), lr=learning_rate, momentum=%s' % optimizer_attr['momentum']
        temp_str+= ', weight_decay=%s' % optimizer_attr['weight_decay']
        temp_str+= ', dampening=%s' % optimizer_attr['dampening']
        temp_str+= ', nesterov=%s)\n' % optimizer_attr['nesterov']
        code_str=np.append(code_str,temp_str)
    elif optimizer == 'ASGD':
        temp_str=''
        temp_str+= 'optimizer = optim.SGD(net.parameters(), lr=learning_rate, lambd=%s' % optimizer_attr['lambd']
        temp_str+= ', alpha=%s' % optimizer_attr['alpha']
        temp_str+= ', t0=%s' % optimizer_attr['t0']
        temp_str+= ', weight_decay=%s)\n' % optimizer_attr['weight_decay']
        code_str=np.append(code_str,temp_str)
    elif optimizer == 'RMSprop':
        temp_str=''
        temp_str+= 'optimizer = optim.RMSprop(net.parameters(), lr=learning_rate, momentum=%s' % optimizer_attr['momentum']
        temp_str+= code_str,', alpha=%s' % optimizer_attr['alpha']
        temp_str+= code_str,', eps=%s' % optimizer_attr['eps']
        temp_str+= ', centered=%s' % optimizer_attr['centered']
        temp_str+= ', weight_decay=%s)\n' % optimizer_attr['weight_decay']
        code_str=np.append(code_str,temp_str)
    elif optimizer == 'Adammax':
        temp_str=''
        temp_str+= 'optimizer = optim.RMSprop(net.parameters(), lr=learning_rate, beta1=%s' % optimizer_attr['beta1']
        temp_str+= ', beta2=%s' % optimizer_attr['beta2']
        temp_str+= ', eps=%s' % optimizer_attr['eps']
        temp_str+= ', weight_decay=%s)\n' % optimizer_attr['weight_decay']
        code_str=np.append(code_str,temp_str)
    lr_scheduler=None
    lr_scheduler_attr=None
    if 'learning_rate_scheduler' not in load_dict or  load_dict['learning_rate_scheduler']=='None' or load_dict['learning_rate_scheduler']['name']=='None':
        pass 
    else:
        lr_scheduler = load_dict['learning_rate_scheduler']['name']
        lr_scheduler_attr = load_dict['learning_rate_scheduler']['attribute']
    if lr_scheduler == 'stepLR':
        temp_str=''
        temp_str+='scheduler = torch.optim.lr_scheduler.%s' % lr_scheduler
        temp_str+='(optimizer, step_size=%s' % lr_scheduler_attr['step_size'] + ', gamma=%s)\n' % lr_scheduler_attr['gamma']
        code_str=np.append(code_str,temp_str)
    elif lr_scheduler == 'MultiStepLR':
        temp_str=''
        temp_str+= 'scheduler = torch.optim.lr_scheduler.%s' % lr_scheduler
        temp_str+= '(optimizer, milestones=%s' % lr_scheduler_attr['milestones'] + ', gamma=%s)\n' % lr_scheduler_attr['gamma']
        code_str=np.append(code_str,temp_str)
    elif lr_scheduler == 'ExponentialLR':
        temp_str=''
        temp_str+= 'scheduler = torch.optim.lr_scheduler.%s' % lr_scheduler
        temp_str+= '(gamma=%s)\n' % lr_scheduler_attr['gamma']
        code_str=np.append(code_str,temp_str)
    elif lr_scheduler == 'CosineAnnealingLR':
        temp_str=''
        temp_str+= 'scheduler = torch.optim.lr_scheduler.%s' % lr_scheduler
        temp_str+= '(optimizer, T_max=%s' % lr_scheduler_attr['T_max'] + ', eta_min=%s)\n' % lr_scheduler_attr['eta_min']
        code_str=np.append(code_str,temp_str)
    elif lr_scheduler == 'ReduceLROnPleateau':
        temp_str=''
        temp_str+= 'scheduler = torch.optim.lr_scheduler.%s' % lr_scheduler
        temp_str+= '(optimizer, factor=%s' % lr_scheduler_attr['factor'] + ', patience=%s' % lr_scheduler_attr['patience']
        temp_str+= ', cooldown=%s' % lr_scheduler_attr['cooldown']
        temp_str+= ', verbose=%s' % lr_scheduler_attr['verbose']
        temp_str+= ', min_lr=%s)\n' % lr_scheduler_attr['min_lr']
        code_str=np.append(code_str,temp_str)
    
    loss = load_dict['loss']['name']
    loss_attr = load_dict['loss']['attribute']
    if loss in ['MSELoss', 'L1Loss']:
        code_str = np.append(code_str,'loss_func = torch.nn.%s' % loss + '(reduction = \"%s\")\n' % loss_attr['reduction'])
    elif loss in ['CrossEntropyLoss', 'NLLLoss']:
        temp_str=''
        temp_str+='loss_func = torch.nn.%s' % loss + '(reduction = \"%s\"' % loss_attr['reduction']
        if loss_attr['ignore_index'] != 'None':
            temp_str+=', ignore_index = %s)' % loss_attr['ignore_index']
        temp_str+= ')\n'
        code_str=np.append(code_str,temp_str)
    elif loss == 'BCELoss':
        code_str = np.append(code_str,'loss_func = torch.nn.%s' % loss + '(reduction = \"%s\")\n' % loss_attr['reduction'])
    
    dataset = load_dict['dataset']
    if dataset == 'mnist' or dataset=='jena' or dataset=='glove':
        code_str = np.concatenate((code_str,
np.array(['def dataset_prepare():',
'     global train_loader, test_loader, DOWNLOAD_MNIST, num_work',
'     if not (os.path.exists(\'./mnist/\')) or not os.listdir(\'./mnist/\'):',
'        DOWNLOAD_MNIST = True',
'     transform = transforms.Compose([',
'     transforms.ToTensor(),',
'     transforms.Normalize((0.1307,), (0.3081,)),',
'     ])',
'     train_data = torchvision.datasets.MNIST(',
'     root=\'./mnist/\',',
'     train=True,', 
'     transform=transform,', 
'     download=DOWNLOAD_MNIST'
'     )',
'     test_data = torchvision.datasets.MNIST(root=\'./mnist/\', train=False,download=True)',
'     train_loader = Data.DataLoader(dataset=train_data, batch_size=batch_size, shuffle=if_shuffle)',
'     test_loader = Data.DataLoader(dataset=test_data, batch_size=batch_size, shuffle=False)'
    ])))
    elif dataset == 'cifar10':
        code_str = np.concatenate((code_str,
np.array(['def dataset_prepare():',
'    global train_loader,test_loader',
'    transform_train = transforms.Compose([',
'    transforms.RandomCrop(32, padding=4), ',
'    transforms.RandomHorizontalFlip(),',
'    transforms.ToTensor(),',
'    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),',
'    ])',
'    transform_test = transforms.Compose([',
'    transforms.ToTensor(),',
'    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),',
'    ])',
'    trainset = torchvision.datasets.CIFAR10(root=\'./cifa10/\', train=True, download=True, transform=transform_train)',
'    train_loader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=if_shuffle, num_workers=num_work)',
'    testset = torchvision.datasets.CIFAR10(root=\'./cifa10/\', train=False, download=True, transform=transform_test)',
'    test_loader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False, num_workers=num_work)',
'    classes = (\'plane\', \'car\', \'bird\', \'cat\', \'deer\', \'dog\', \'frog\', \'horse\', \'ship\', \'truck\')'
        ])))
    elif dataset == 'stl10':
        code_str = np.concatenate((code_str,
np.array(['def dataset_prepare():',
'    global train_loader,test_loader',
'    transform_train=transforms.Compose([',
'    transforms.Pad(4),',
'    transforms.RandomCrop(96),',
'    transforms.RandomHorizontalFlip(),',
'    transforms.ToTensor(),',
'    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),',
'    ])',
'    transform_test = transforms.Compose([',
'    transforms.ToTensor(),',
'    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),',
'    ])',
'    trainset=torchvision.datasets.STL10(root=\'./stl10/\', split=\'train\', download=True,transform=transform_train)',
'    train_loader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=if_shuffle, num_workers=num_work)',
'    testset=torchvision.datasets.STL10(root=\'./stl10/\', split=\'test\', download=True,transform=transform_test)',
'    test_loader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False, num_workers=num_work)'
])))
    elif dataset == 'svhn':
        code_str =np.concatenate((code_str,
np.array(['def dataset_prepare():',
'    global train_loader,test_loader',
'    transform_train=transforms.Compose([',
'    transforms.ToTensor(),',
'    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),',
'    ])',
'    transform_test = transforms.Compose([',
'    transforms.ToTensor(),',
'    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),',
'    ])',
'    trainset=torchvision.datasets.SVHN(root=\'./svhn/\', split=\'train\', download=True,transform=transform_train)',
'    train_loader = torch.utils.data.DataLoader(trainset, batch_size=batch_size, shuffle=if_shuffle, num_workers=num_work)',
'    testset=torchvision.datasets.SVHN(root=\'./svhn/\', split=\'test\', download=True,transform=transform_test)',
'    test_loader = torch.utils.data.DataLoader(testset, batch_size=batch_size, shuffle=False, num_workers=num_work)'
])))
    
    code_str =np.concatenate((code_str,
np.array(['def train():',
'    global optimizer',
'    running_loss=0',
'    for epo in range(epoch):',
'        for step, (b_x, b_y) in enumerate(train_loader,0): ',
'            b_x,b_y=b_x.to(device),b_y.to(device)',
'            optimizer.zero_grad()',
'            outputs=net(b_x)',
'            loss=loss_func(outputs,b_y)',
'            loss.backward()',
'            optimizer.step()',
'            running_loss+=loss.item()',
'            if step%300 == 0:',
'                print(\'[%d,%5d] loss:%.3f\' % (epoch+1,step+1,running_loss))',
'                running_loss=0',
'def test():',
'    total=0',
'    correct=0',
'    with torch.no_grad():',
'        for data in test_loader:',
'            images,labels=data',
'            images,labels=images.to(device),labels.to(device)',
'            outputs=net(images)',
'            _,predicted=torch.max(outputs.data,dim=1)',
'            total+=labels.size(0)',
'            correct+=(predicted==labels).sum().item()',
'    print(\'accuracy on test_data= %d %%\'%(100*correct/total))',
'dataset_prepare()',
'train()',
'test()'
])))
    return code_str
