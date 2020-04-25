function get_content(name, parid) {
    if (name == "view_layer") {
        return "<form class=\"form-horizontal\" role=\"form\" id = 'form" + parid + "' name = 'view_layer'><div class=\"form-group\">" +
            "                    <label class=\"col-sm-5 control-label\">shape</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='shape' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["shape"] + "\" placeholder=\"1\">" +
            "                    </div>" +
            "                </form>";
    }

    if (name == "linear_layer") {
        return "<form class=\"form-horizontal\" role=\"form\" id = 'form" + parid + "' name = 'linear_layer'><div class=\"form-group\">" +
            "                    <label class=\"col-sm-5 control-label\">in_features</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='in_features' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["in_features"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">out_features</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='out_features' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["out_features"] + "\">" +
            "                    </div>" +
            "                </div>" +
            "                </form>";
    }

    if (name == "concatenate_layer") {
        return "<form class=\"form-horizontal\" role=\"form\" id = 'form" + parid + "' name = 'concatenate_layer'><div class=\"form-group\">" +
            "                    <label class=\"col-sm-5 control-label\">dim</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='dim' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["dim"] + "\" placeholder=\"0\">" +
            "                    </div>" +
            "                </div>" +
            "                </form>";
    }




    if (name == "conv1d_layer") {
        return "<form class=\"form-horizontal\" role=\"form\" id = 'form" + parid + "' name = 'conv1d_layer'><div class=\"form-group\">" +
            "                    <label class=\"col-sm-5 control-label\">in_channels</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='in_channels' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["in_channels"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">out_channels</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='out_channels' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["out_channels"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">kernel_size</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='kernel_size' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["kernel_size"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">stride</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='stride' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["stride"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">padding</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='padding' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["padding"] + "\">" +
            "                    </div></div>" +
            "                    <div class=\"form-group\">" +
            "                    <label class=\"control-label\">activity</label>" +

            "                        <select id=\"" + parid + "activity\" class=\"form-control\">\n" +
            "                            <option value=\"None\">None</option>\n" +
    "                            <option value=\"torch.nn.Relu\">relu</option>\n" +
    "                            <option value=\"torch.nn.LeakyRelu\">leaky_relu</option>\n" +
    "                            <option value=\"torch.nn.Sigmoid\">sigmoid</option>\n" +
    "                            <option value=\"torch.nn.Tanh\">tanh</option>\n" +
            "                        </select>" +

            "                    <label class=\"control-label\">pool_way</label>" +

            "                        <select id=\"" + parid + "pool_way\" name='pool_way' class=\"form-control\">\n" +
    "                            <option value=\"None\">None</option>\n" +
    "                            <option value=\"torch.nn.MaxPool1d\">max_pool1d</option>\n" +
    "                            <option value=\"torch.nn.MaxPool2d\">max_pool2d</option>\n" +
    "                            <option value=\"torch.nn.MaxPool3d\">max_pool3d</option>\n" +
    "                            <option value=\"torch.nn.AvgPool1d\">AvgPool1d</option>\n" +
    "                            <option value=\"torch.nn.AvgPool2d\">AvgPool2d</option>\n" +
    "                            <option value=\"torch.nn.AvgPool3d\">AvgPool3d</option>\n" +
            "                        </select>" +

            "                    <label class=\"col-sm-6 control-label\">pool_kernel_size</label>" +
            "                            <div class=\"col-sm-6\">" +
            "                        <input type=\"text\" id=\"" + parid + "pool_kernel_size\" name='pool_kernel_size' disabled=true class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["pool_kernel_size"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-6 control-label\">pool_stride</label>" +
            "                            <div class=\"col-sm-6\">" +
            "                        <input type=\"text\" id=\"" + parid + "pool_stride\" name='pool_stride' disabled=true class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["pool_stride"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-6 control-label\">pool_padding</label>" +
            "                            <div class=\"col-sm-6\">" +
            "                        <input type=\"text\" id=\"" + parid + "pool_padding\" name='pool_padding' disabled=true class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["pool_padding"] + "\">" +
            "                    </div>" +
            "                </div>" +
            "                </form>";
    }

    if (name == "conv2d_layer") {
        return "<form class=\"form-horizontal\" role=\"form\" id = 'form" + parid + "' name = 'conv2d_layer'><div class=\"form-group\">" +
            "                    <label class=\"col-sm-5 control-label\">in_channels</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='in_channels' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["in_channels"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">out_channels</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='out_channels' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["out_channels"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">kernel_size</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='kernel_size' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["kernel_size"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">stride</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='stride' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["stride"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">padding</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='padding' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["padding"] + "\">" +
            "                    </div></div><div class=\"form-group\">" +
            "                    <label class=\"control-label\">activity</label>" +

            "                        <select id=\"" + parid + "activity\" class=\"form-control\">\n" +
            "                            <option value=\"None\">None</option>\n" +
    "                            <option value=\"torch.nn.Relu\">relu</option>\n" +
    "                            <option value=\"torch.nn.LeakyRelu\">leaky_relu</option>\n" +
    "                            <option value=\"torch.nn.Sigmoid\">sigmoid</option>\n" +
    "                            <option value=\"torch.nn.Tanh\">tanh</option>\n" +
            "                        </select>" +

            "                    <label class=\"control-label\">pool_way</label>" +

            "                        <select id=\"" + parid + "pool_way\" name='pool_way' class=\"form-control\">\n" +
            "                            <option value=\"None\">None</option>\n" +
"                            <option value=\"None\">None</option>\n" +
    "                            <option value=\"torch.nn.MaxPool1d\">max_pool1d</option>\n" +
    "                            <option value=\"torch.nn.MaxPool2d\">max_pool2d</option>\n" +
    "                            <option value=\"torch.nn.MaxPool3d\">max_pool3d</option>\n" +
    "                            <option value=\"torch.nn.AvgPool1d\">AvgPool1d</option>\n" +
    "                            <option value=\"torch.nn.AvgPool2d\">AvgPool2d</option>\n" +
    "                            <option value=\"torch.nn.AvgPool3d\">AvgPool3d</option>\n" +
            "                        </select>" +
            "                    <label class=\"col-sm-6 control-label\">pool_kernel_size</label>" +
            "                            <div class=\"col-sm-6\">" +
            "                        <input type=\"text\" id=\"" + parid + "pool_kernel_size\" name='pool_kernel_size' disabled=true class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["pool_kernel_size"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-6 control-label\">pool_stride</label>" +
            "                            <div class=\"col-sm-6\">" +
            "                        <input type=\"text\" id=\"" + parid + "pool_stride\" name='pool_stride' disabled=true class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["pool_stride"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-6 control-label\">pool_padding</label>" +
            "                            <div class=\"col-sm-6\">" +
            "                        <input type=\"text\" id=\"" + parid + "pool_padding\" name='pool_padding' disabled=true class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["pool_padding"] + "\">" +
            "                    </div>" +
            "                </div>" +
            "                </form>";
    }



    if (name == "softmax_layer") {
        return "<form class=\"form-horizontal\" role=\"form\" id = 'form" + parid + "' name = 'softmax_layer'><div class=\"form-group\">" +
            "                    <label class=\"col-sm-5 control-label\">dim</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='dim' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["dim"] + "\" placeholder=\"0\">" +
            "                    </div>" +
            "                </div>" +
            "                </form>";
    }


    if (name == "dropout_layer") {
        return  "<form action=\" form-horizontal \" role=\"form\" id = 'form" + parid + "' name = 'dropout_layer'> " +
                "    <div class=\"form-group\"> " +
                "       <label class=\"control-label\">type</label> " +
                "           <select id=\"" + parid + "type\" class=\"form-control\">\n"+
                "               <option value=\"1d\">1d</option>\n"+
                "               <option value=\"2d\" selected >2d</option>\n"+
                "               <option value=\"3d\">3d</option>\n"+
                "           </select> "+
                "    </div> "+
                "    <div class=\"form-group\"> "+
                "        <label class=\"col-sm-5 control-label\">p</label> "+
                "        <div class=\"col-sm-7\"> "+
                "            <input type=\"text\" name='p' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["p"] + "\" placeholder=\"0.5\"> "+
                "        </div> "+
                "    </div> "+
                "</form>";

    }

    if(name == "conv_layer"){
        return  "<form class=\"form-horizontal\" role=\"form\" id = 'form" + parid + "' name = 'conv_layer'> "+
            "       <div class=\"form-group\">" +
            "           <label class=\"control-label\">layer_type</label>" +
            "           <select id=\"" + parid + "layer_type\" class=\"form-control\">\n" +
            "               <option value=\"conv\" selected >conv</option>\n" +
            "               <option value=\"conv_transpose\">conv_transpose</option>\n" +
            "           </select>" +
            "           <label class=\"control-label\">type</label> " +
            "               <select id=\"" + parid + "type\" class=\"form-control\">\n"+
            "                   <option value=\"1d\">1d</option>\n"+
            "                   <option value=\"2d\" selected>2d</option>\n"+
            "                   <option value=\"3d\">3d</option>\n"+
            "               </select> "+
            "       </div> "+
            "       <div class=\"form-group\">" +
            "           <label class=\"col-sm-5 control-label\">in_channels</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='in_channels' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["in_channels"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">out_channels</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='out_channels' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["out_channels"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">kernel_size</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='kernel_size' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["kernel_size"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">stride</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='stride' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["stride"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">padding</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='padding' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["padding"] + "\">" +
            "                    </div> "+
            "       </div>" +
            "     </form>";
    }
//layer_type:下拉框三选一，选项包括max_pool/avg_pool/max_unpool 无默认值
// type:下拉框三选一，选项包括1d/2d/3d 无默认值

// kernel_size (int) : 卷积核的尺寸 非0正数 无默认值

// stride (int) : 卷积步长 非0正数 无默认值

// padding (int) : 补充0的层数 非负整数 默认值为0

// ceil_mode:下拉框二选一，ceil/floor 默认值为floor

// count_include_pad:下拉框二选一,true/false 默认值为true
    if(name == "pool_layer"){
        return  "<form class=\"form-horizontal\" role=\"form\" id = 'form" + parid + "' name = 'pool_layer'> "+
            "       <div class=\"form-group\">" +
            "           <label class=\"control-label\">layer_type</label>" +
            "           <select id=\"" + parid + "layer_type\" class=\"form-control\">\n" +
            "               <option value=\"max_pool\" selected >max_pool</option>\n" +
            "               <option value=\"avg_pool\">avg_pool</option>\n" +
            "               <option value=\"max_unpool\">max_unpool</option>\n" +
            "           </select>" +
            "           <label class=\"control-label\">type</label> " +
            "               <select id=\"" + parid + "type\" class=\"form-control\">\n"+
            "                   <option value=\"1d\">1d</option>\n"+
            "                   <option value=\"2d\" selected>2d</option>\n"+
            "                   <option value=\"3d\">3d</option>\n"+
            "               </select> "+
            "       </div> "+
            "       <div class=\"form-group\">" +
            "                    <label class=\"col-sm-5 control-label\">kernel_size</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='kernel_size' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["kernel_size"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">stride</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='stride' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["stride"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">padding</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='padding' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["padding"] + "\">" +
            "                    </div> "+
            "       </div>" +
            "       <div class=\"form-group\">" +
            "           <label class=\"control-label\">ceil_mode</label>" +
            "           <select id=\"" + parid + "ceil_mode\" class=\"form-control\">\n" +
            "               <option value=\"floor\">floor</option>\n" +
            "               <option value=\"ceil\">ceil</option>\n" +
            "           </select>" +
            "           <label class=\"control-label\">count_include_pad</label> " +
            "               <select id=\"" + parid + "count_include_pad\" class=\"form-control\">\n"+
            "                   <option value=\"true\">true</option>\n"+
            "                   <option value=\"false\">false</option>\n"+
            "               </select> "+
            "       </div> "+
            "     </form>";
    }

// layer_type:下拉框，包括relu/sigmoid/tanh/leaky relu/PRelu/RRelu 默认值为relu

// relu：无参数

// sigmoid:无参数

// tanh:无参数

// leaky relu:

// negative_slope<正数> 默认值为0.01

// PRelu: 类似leaky relu, 但是负数部分斜率可学习

// weight<正数>权重初始化 非0正实数 默认值为0.25
// RRelu: 类似leaky relu, 但是负数部分斜率为随机均匀分布

// lower<正数>：均匀分布下限 默认值为0.125

// upper<正数>：均匀分布上限 默认值为0.333
//
    if(name == "activation_layer"){
        return  "<form class=\"form-horizontal\" role=\"form\" id = 'form" + parid + "' name = 'activation_layer'> "+
            "       <div class=\"form-group\">" +
            "           <label class=\"control-label\">layer_type</label>" +
            "           <select id=\"" + parid + "layer_type\" class=\"form-control\">\n" +
            "               <option value=\"relu\" selected >relu</option>\n" +
            "               <option value=\"sigmoid\">sigmoid</option>\n" +
            "               <option value=\"tanh\">tanh</option>\n" +
            "               <option value=\"leaky relu\">leaky relu</option>\n" +
            "               <option value=\"PRelu\">PRelu</option>\n" +
            "               <option value=\"RRelu\">RRelu</option>\n" +
            "           </select>" +
            "       </div> "+
            "       <div class=\"form-group\">" +
            "                    <label class=\"col-sm-5 control-label\">negative_slope</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='negative_slope' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["negative_slope"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">weight</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='weight' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["weight"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">lower</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='lower' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["lower"] + "\">" +
            "                    </div> "+
            "                    <label class=\"col-sm-5 control-label\">upper</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='upper' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["upper"] + "\">" +
            "                    </div> "+
            "       </div>" +
            "     </form>";
    }


// RNN_layer:递归神经网络(新增网络层)#
// input_size<正整数>：输入特征数 无默认值

// hidden_size<正整数>:隐藏层个数 无默认值

// num_layers<正整数>:递归层层数 默认值为1

// nonlinearity(二选一,tanh/relu):非线性激活 默认为tanh
//
    if(name == "RNN_layer"){
        return  "<form class=\"form-horizontal\" role=\"form\" id = 'form" + parid + "' name = 'RNN_layer'> "+
            "       <div class=\"form-group\">" +
            "                    <label class=\"col-sm-5 control-label\">input_size</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='input_size' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["input_size"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">hidden_size</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='hidden_size' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["hidden_size"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">num_layers</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='num_layers' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["num_layers"] + "\">" +
            "                    </div> "+
            "       </div>" +
            "       <div class=\"form-group\">" +
            "           <label class=\"control-label\">nonlinearity</label>" +
            "           <select id=\"" + parid + "nonlinearity\" class=\"form-control\">\n" +
            "               <option value=\"tanh\" selected>tanh</option>\n" +
            "               <option value=\"relu\">relu</option>\n" +
            "           </select>" +
            "       </div> "+
            "     </form>";
    }



    if(name == "LSTM_layer"){
        return  "<form class=\"form-horizontal\" role=\"form\" id = 'form" + parid + "' name = 'LSTM_layer'> "+
            "       <div class=\"form-group\">" +
            "                    <label class=\"col-sm-5 control-label\">input_size</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='input_size' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["input_size"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">hidden_size</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='hidden_size' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["hidden_size"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">num_layers</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='num_layers' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["num_layers"] + "\">" +
            "                    </div> "+
            "       </div>" +
            "     </form>";
    }

    if(name == "norm_layer"){
        return  "<form class=\"form-horizontal\" role=\"form\" id = 'form" + parid + "' name = 'norm_layer'> "+
            "       <div class=\"form-group\">" +
            "           <label class=\"control-label\">layer_type</label>" +
            "           <select id=\"" + parid + "layer_type\" class=\"form-control\">\n" +
            "               <option value=\"batch_norm\" selected>batch_norm</option>\n" +
            "               <option value=\"group_norm\">group_norm</option>\n" +
            "               <option value=\"instance_norm\">instance_norm</option>\n" +
            "           </select>" +
            "           <label class=\"control-label\">type</label>" +
            "           <select id=\"" + parid + "type\" class=\"form-control\">\n" +
            "               <option value=\"1d\">1d</option>\n" +
            "               <option value=\"2d\" selected >2d</option>\n" +
            "               <option value=\"3d\">3d</option>\n" +
            "           </select>" +
            "       </div> "+
            "       <div class=\"form-group\">" +
            "                    <label class=\"col-sm-5 control-label\">num_features</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='num_features' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["num_features"] + "\">" +
            "                    </div> "+
            "                    <label class=\"col-sm-5 control-label\">num_groups</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='num_groups' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["num_groups"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">num_channel</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='num_channel' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["num_channel"] + "\">" +
            "                    </div>" +
            "       </div>" +
            "     </form>";
    }
}


function set_content(name, parid) {
    var data = eval('(' + window.sessionStorage.getItem(parid) + ')');
    if (name == "conv1d_layer") {
        $("#"+parid+"activity").find("option").removeAttr("selected");
        $("#"+parid+"activity").find("option[value=\""+ data['activity'] + "\"]").attr("selected", "selected");
        $("#"+parid+"pool_way").find("option").removeAttr("selected");
        $("#"+parid+"pool_way").find("option[value=\""+ data['pool_way'] + "\"]").attr("selected", "selected");
    }

    if (name == "conv2d_layer") {
        $("#"+parid+"activity").find("option").removeAttr("selected");
        $("#"+parid+"activity").find("option[value=\""+ data['activity'] + "\"]").attr("selected", "selected");
        $("#"+parid+"pool_way").find("option").removeAttr("selected");
        $("#"+parid+"pool_way").find("option[value=\""+ data['pool_way'] + "\"]").attr("selected", "selected");
    }

    if (name == "dropout_layer") {
        $("#"+parid+"type").find("option").removeAttr("selected");
        $("#"+parid+"type").find("option[value=\""+ data['type'] + "\"]").attr("selected", "selected");
    }

    if(name == "conv_layer"){
        $("#"+parid+"layer_type").find("option").removeAttr("selected");
        $("#"+parid+"layer_type").find("option[value=\""+ data['layer_type'] + "\"]").attr("selected", "selected");
        $("#"+parid+"type").find("option").removeAttr("selected");
        $("#"+parid+"type").find("option[value=\""+ data['type'] + "\"]").attr("selected", "selected");
    }

    if(name == "pool_layer"){
        $("#"+parid+"layer_type").find("option").removeAttr("selected");
        $("#"+parid+"layer_type").find("option[value=\""+ data['layer_type'] + "\"]").attr("selected", "selected");
        $("#"+parid+"type").find("option").removeAttr("selected");
        $("#"+parid+"type").find("option[value=\""+ data['type'] + "\"]").attr("selected", "selected");
        $("#"+parid+"ceil_mode").find("option").removeAttr("selected");
        $("#"+parid+"ceil_mode").find("option[value=\""+ data['ceil_mode'] + "\"]").attr("selected", "selected");
        $("#"+parid+"count_include_pad").find("option").removeAttr("selected");
        $("#"+parid+"count_include_pad").find("option[value=\""+ data['count_include_pad'] + "\"]").attr("selected", "selected");
    }

    if(name == "activation_layer"){
        $("#"+parid+"layer_type").find("option").removeAttr("selected");
        $("#"+parid+"layer_type").find("option[value=\""+ data['layer_type'] + "\"]").attr("selected", "selected");
    }

    if(name == "RNN_layer"){
        $("#"+parid+"nonlinearity").find("option").removeAttr("selected");
        $("#"+parid+"nonlinearity").find("option[value=\""+ data['nonlinearity'] + "\"]").attr("selected", "selected");
    }

    if(name == "norm_layer"){
        $("#"+parid+"layer_type").find("option").removeAttr("selected");
        $("#"+parid+"layer_type").find("option[value=\""+ data['layer_type'] + "\"]").attr("selected", "selected");
        $("#"+parid+"type").find("option").removeAttr("selected");
        $("#"+parid+"type").find("option[value=\""+ data['type'] + "\"]").attr("selected", "selected");
    }


}

