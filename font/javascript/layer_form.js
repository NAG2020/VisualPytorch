function get_content(name, parid) {
    if (name == "view_layer") {
        return "<form class=\"form-horizontal\" role=\"form\" id = 'form" + parid + "' name = 'view_layer'><div class=\"form-group\">" +
            "                    <label class=\"col-sm-5 control-label\">shape</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='shape' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["shape"] + "\" placeholder=\"1\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">这个什么用户输入多个数字分开的是什么玩意</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='shape' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["shape"] + "\" placeholder=\"1\">" +
            "                    </div>" +
            "                </div>" +
            "                </form>";
    }

    if (name == "linear_layer") {
        return "<form class=\"form-horizontal\" role=\"form\" id = 'form" + parid + "' name = 'linear_layer'><div class=\"form-group\">" +
            "                    <label class=\"col-sm-5 control-label\">in_channels</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='in_channels' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["in_channels"] + "\">" +
            "                    </div>" +
            "                    <label class=\"col-sm-5 control-label\">out_channels</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='out_channels' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["out_channels"] + "\">" +
            "                    </div>" +
            "                </div>" +
            "                </form>";
    }

    if (name == "concatenate_layer") {
        return "<form class=\"form-horizontal\" role=\"form\" id = 'form" + parid + "' name = 'concatenate_layer'><div class=\"form-group\">" +
            "                    <label class=\"col-sm-5 control-label\">dim</label>" +
            "                            <div class=\"col-sm-7\">" +
            "                        <input type=\"text\" name='dim' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["dim"] + "\" placeholder=\"1\">" +
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
            "                        <input type=\"text\" name='dim' class=\"form-control\" value=\"" + eval('(' + window.sessionStorage.getItem(parid) + ')')["dim"] + "\" placeholder=\"1\">" +
            "                    </div>" +
            "                </div>" +
            "                </form>";
    }


    if (name == "dropout_layer") {
        return  "<form action=\" form-horizontal \" role=\"form\" id = 'form" + parid + "' name = 'dropout_layer'> " +
                "    <div class=\"form-group\"> " +
                "       <label class=\"control-label\">type</label> " +
                "           <select id=\"" + parid + "type\" class=\"form-control\">\n"+
                "               <option value=\"None\">None</option>\n"+
                "               <option value=\"1d\">1d</option>\n"+
                "               <option value=\"2d\">2d</option>\n"+
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
            "               <option value=\"None\">None</option>\n" +
            "               <option value=\"1d\">1d</option>\n" +
            "               <option value=\"2d\">2d</option>\n" +
            "               <option value=\"3d\">3d</option>\n" +
            "           </select>" +
            "           <label class=\"control-label\">type</label> " +
            "               <select id=\"" + parid + "type\" class=\"form-control\">\n"+
            "                   <option value=\"None\">None</option>\n"+
            "                   <option value=\"1d\">1d</option>\n"+
            "                   <option value=\"2d\">2d</option>\n"+
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
            "               <option value=\"None\">None</option>\n" +
            "               <option value=\"1d\">1d</option>\n" +
            "               <option value=\"2d\">2d</option>\n" +
            "               <option value=\"3d\">3d</option>\n" +
            "           </select>" +
            "           <label class=\"control-label\">type</label> " +
            "               <select id=\"" + parid + "type\" class=\"form-control\">\n"+
            "                   <option value=\"None\">None</option>\n"+
            "                   <option value=\"1d\">1d</option>\n"+
            "                   <option value=\"2d\">2d</option>\n"+
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
}

