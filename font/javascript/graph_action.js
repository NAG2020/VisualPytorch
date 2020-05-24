var gobalConfig = {
    //"base_url": "http://114.115.148.27:80/"
    "base_url": "http://127.0.0.1:8000/"
};

/*$(function () {
    $('#submit').click( function (e) {
        var conn_list;
        var network = [];
        conn_list = jsPlumb.getAllConnections();
        console.log(conn_list);
        for (var i = 0; i < conn_list.length; i++) {
            var source_id = conn_list[i]["sourceId"];
            var target_id = conn_list[i]["targetId"];
            var conn = {
                "source": $("#" + source_id).attr("name"),
                "target": $("#" + target_id).attr("name")
            }
            network.push(conn);
        }

       $.ajax({
            type: 'POST',
            url: gobalConfig.base_url + 'NeuralNetwork/network/',
            data: JSON.stringify(network),
            contentType: 'application/json; charset=UTF-8',
            success: function (data_return) {
                alert(data_return);
            }
        });
    });
});*/
// function get_network() {
//     var conn_list;
//     var nets_conn = [];
//     var nets = {};
//     $("#canvas").find(".node").each(function (index, element) {
//         var id = $(element).attr('id');
//         nets[id] = {
//             "type": 'base',
//             "name": $(element).attr('name'),
//             "attribute": eval('(' + window.sessionStorage.getItem(id) + ')'),
//             "left": $(element).css('left'),
//             "top": $(element).css('top')
//         }
//     });
//     conn_list = jsPlumb.getAllConnections();
//     console.log(conn_list);

//     for (var i = 0; i < conn_list.length; i++) {
//         var source_id = conn_list[i]["sourceId"];
//         var target_id = conn_list[i]["targetId"];
//         var conn = {
//             "source": {
//                 "id": source_id,
//                 "anchor_position": conn_list[i]["endpoints"][0]["anchor"]["type"]
//             },
//             "target": {
//                 "id": target_id,
//                 "anchor_position": conn_list[i]["endpoints"][1]["anchor"]["type"]
//             }
//         };
//         nets_conn.push(conn);
//     }
//     var epoch = $("#epoch").val();
//     if (epoch == "") {
//         epoch = "1";
//     }
//     var learning_rate = $("#learning_rate").val();
//     if (learning_rate == "") {
//         learning_rate = "0.5";
//     }
//     var batch_size = $("#batch_size").val();
//     if (batch_size == "") {
//         batch_size = "1";
//     }
//     var static = {
//         "epoch": epoch,
//         "optimizer": $("#optimzier").find("option:selected").val(),
//         "learning_rate": learning_rate,
//         "batch_size": batch_size
//     };
    // var data = {
    //     "name": $("#model_name").val(),
    //     "structure": {
    //         "nets": nets,
    //         "nets_conn": nets_conn,
    //         "static": static
    //     }
    // };
//     return data;
// }


function saveJSON(data, filename){
    if(!data) {
        alert('保存的数据为空');
        return;
    }
    if(!filename)
        filename = 'json.json'
    if(typeof data === 'object'){
        data = JSON.stringify(data, undefined, 4)
    }
    var blob = new Blob([data], {type: 'text/json'}),
    e = document.createEvent('MouseEvents'),
    a = document.createElement('a')
    a.download = filename
    a.href = window.URL.createObjectURL(blob)
    a.dataset.downloadurl = ['text/json', a.download, a.href].join(':')
    e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
    a.dispatchEvent(e)
}



function get_network() {
    var conn_list;
    var nets_conn = [];
    var sequential = {};
    var nets = {};
    //console.log(model_net);
    $("#canvas").find(".node").each(function (index, element) {
        if($(element).hasClass('model_node')){
            var id = $(element).attr('id');
            var name = $(element).attr('name');
            //console.log(name);
            nets[id] =  model_net[name].canvas;
            // {
            //     "type": 'sequential',
            //     "name": $(element).attr('name'),
            //     "attribute": eval('(' + model_net[id] + ')'),
            //     "left": $(element).css('left'),
            //     "top": $(element).css('top')
            // }
        }
        else{
            var id = $(element).attr('id');
            nets[id] = {
                "type": 'base',
                "name": $(element).attr('name'),
                "attribute": eval('(' + window.sessionStorage.getItem(id) + ')'),
                "left": $(element).css('left'),
                "top": $(element).css('top')
            }
        }

    });
    console.log(nets);
    conn_list = jsPlumb.getAllConnections();
    for (var i = 0; i < conn_list.length; i++) {
        var source_id = conn_list[i]["sourceId"];
        var target_id = conn_list[i]["targetId"];
        var conn = {
            "source": {
                "id": source_id,
                "anchor_position": conn_list[i]["endpoints"][0]["anchor"]["type"]
            },
            "target": {
                "id": target_id,
                "anchor_position": conn_list[i]["endpoints"][1]["anchor"]["type"]
            }
        };
        nets_conn.push(conn);
    }
    var startid = $("#canvas").find(".start").attr("id");
    var endid = $("#canvas").find(".end").attr("id");

    //alert(endid);
    // sequential.push();

    //

    var epoch = $("#epoch").val()==""?"10":$("#epoch").val();

    var learning_rate = $("#learning_rate").val()==""?"0.01":$("#learning_rate").val();

    var batch_size = $("#batch_size").val()==""?"1":$("#batch_size").val();


    var learning_rate_scheduler = {
        "name": $("#learning_rate_scheduler").find("option:selected").val(),
        "attribute": {
            "step_size" : $("#step_size").val()==""?"50":$("#step_size").val(),
            "gramma" : $("#gamma").val()==""?"0.1":$("#gamma").val(),
            "milestones":$("#milestones").val()==""?"50":$("#milestones").val(),
            "T_max" : $("#T_max").val()==""?"50":$("#T_max").val(),
            "eta_min" : $("#eta_min").val()==""?"0":$("#eta_min").val(),
            "factor":$("#factor").val()==""?"0.1":$("#factor").val(),
            "patience" : $("#patience").val()==""?"10":$("#patience").val(),
            "cooldown" : $("#cooldown").val()==""?"10":$("#cooldown").val(),
            "verbose":$("#verbose").prop("checked")==true?"true":"false",
            "min_lr":$("#min_lr").val()==""?"0.0001":$("#min_lr").val()
        }
    }

    var platform = $("#platform").find("option:selected").val();
    var dataset = $("#dataset").find("option:selected").val();

    var ifshuffle = $("#ifshuffle").prop("checked");

    var optimizer = {
        "name": $("#optimizer").find("option:selected").val(),
        "attribute" :{
            "beta1": $("#beta1").val()==""?"0.9":$("#beta1").val(),
            "beta2": $("#beta2").val()==""?"0.999":$("#beta2").val(),
            "eps": $("#eps").val()==""?"0.00000001":$("#eps").val(),
            "weight_decay": $("#weight_decay").val()==""?"0":$("#weight_decay").val(),
            "amsgrad": $("#amsgrad").prop("checked")==true?"true":"false",
            "momentum": $("#momentum").val()==""?"0":$("#momentum").val(),
            "dampening": $("#dampening").val()==""?"0":$("#dampening").val(),
            "nesterov": $("#nesterov").prop("checked")==true?"true":"false",
            "lambd": $("#lambd").val()==""?"0.0001":$("#lambd").val(),
            "alpha": $("#alpha").val()==""?"0.75":$("#alpha").val(),
            "t0": $("#t0").val()==""?"1000000":$("#t0").val(),
            "centered": $("#centered").prop("checked")==true?"true":"false"
        }
    };


    var loss = {
        "name": $("#loss").find("option:selected").val(),
        "attribute" :{
            "reduction": $("#reduction").find("option:selected").val(),
            "weight": $("#weight").val()==""?"None":$("#weight").val(),
            "ignore_index": $("#ignore_index").val()==""?"None":$("#ignore_index").val(),
        }
    };


    var static = {
        "epoch": epoch,
        "learning_rate": learning_rate,
        "batch_size": batch_size,
        "learning_rate_scheduler":learning_rate_scheduler,
        "device":platform,
        "data":dataset,
        "optimizer":optimizer,
        "loss":loss
    };

    var structure = {
        "canvas": {
            "type": "sequential",
            //sequential表示嵌套模型，base表示单个网络层
            "name": "sequential_" + $("#model_name").val(),
            //对于Sequential为用户在保存网络层时为网络层取的名字，默认按照sequential_%d来排序
            "attribute": {
                "in": startid,
                //表示每个Sequential开始节点，即入度为0的节点，该节点一定是type="base" && attribute.layer_type = "in"
                "out": endid,
                //表示每个Sequential结束节点，即出度为0的节点，该节点一定是type="base" && attribute.layer_type = "out"
                //对于Sequential attribute的结构
                "nets": nets
            },
            "nets_conn": nets_conn
        },
        "static": static
    };

    //var graph = await canvas_gen();
    //graph.then(num =>{console.log(num)});
    //console.log(graph);

    var sharable = $("#shared").attr("disabled") == "disabled" ? false : true;

    var ret = {
        "name" : $("#model_name").val(),
        "description" : $("#model_info").val(),
        "sharable" : sharable,
        "shared" : $("#shared").is(":checked") ? true : false,
        "structure" : structure
    }
    saveJSON(ret,"a.json");
    return ret;
}

function translate_network() {
    var data = get_network()["structure"];
    console.log(data);
    $.ajax({
        type: 'POST',
        url: gobalConfig.base_url + 'api/NeuralNetwork/getcode/',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=UTF-8',
        beforeSend: function (XMLHttpRequest) {
            var token = window.sessionStorage.getItem('token');
            if (token != null) {
                XMLHttpRequest.setRequestHeader("Authorization", "JWT " + token)
            }
        },
        success: function (data_return, status, xhr) {

            if (xhr.status == 200) {
                var main = "";
                var main_print = "";
                var model = "";
                var model_print = "";
                //var ops = "";
                //var ops_print = "";
                for (var i = 0; i < data_return["Main"].length; i++) {
                    main = main + data_return["Main"][i] + "<br>";
                    main_print=main_print+data_return["Main"][i] + "\n";
                }
                for (var i = 0; i < data_return["Model"].length; i++) {
                    model = model + data_return["Model"][i] + "<br>";
                    model_print=model_print+data_return["Model"][i] + "\n";
                }
                // for (var i = 0; i < data_return["Ops"].length; i++) {
                //     ops = ops + data_return["Ops"][i] + "<br>";
                //     ops_print=ops_print+data_return["Ops"][i] + "\n";
                // }
                var code = {
                    "model": model,
                    "main": main,
                    //"ops": ops
                };
                var code_print = {
                    "model": model_print,
                    "main": main_print,
                //    "ops": ops_print
                };
                window.sessionStorage.setItem("code", JSON.stringify(data_return));
                window.sessionStorage.setItem("code_print", JSON.stringify(code_print));
                window.open("show_code.html");
                //window.location.href="show_code.html";

            }
            else {
                alert(JSON.stringify(data_return));
            }

        },
        error: function (data_return) {
            alert(data_return["responseText"]);
        }


    });
}

function save_network() {
    //首先生成缩略图
    $("#save_modal").modal('hide');
    window.pageYoffset = 0;
    document.documentElement.scrollTop = 0;
    document.body.scrollTop = 0;
    $("#" + window.sessionStorage.getItem("active_node")).removeClass("selected");
    $("#canvas").find("#border").attr("style","height:1000px;border:0px");
    //获取节点高度，后面为克隆节点设置高度。
    
    var height = $("#canvas").height()
    //克隆节点，默认为false，不复制方法属性，为true是全部复制。
    var cloneDom = $("#canvas").clone(true);
    //设置克隆节点的css属性，因为之前的层级为0，我们只需要比被克隆的节点层级低即可。
    cloneDom.css({
        "background-color": "white",
        "position": "absolute",
        "top": "0px",
        "z-index": "-1",
        "height": height
    });
    $("body").append(cloneDom);
    cloneDom.attr("id", "canvas1");

    if (typeof html2canvas !== 'undefined') {
        //以下是对svg的处理
        var nodesToRecover = [];
        var nodesToRemove = [];
        var svgElem = $("#canvas1").find('svg');//divReport为需要截取成图片的dom的id

        svgElem.each(function (index, node) {
            var parentNode = node.parentNode;
            var svg = node.outerHTML.trim();

            var canvas = document.createElement('canvas');
            canvg(canvas, svg); 
            if (node.style.position) {
                canvas.style.position += node.style.position;
                canvas.style.left += node.style.left;
                canvas.style.top += node.style.top;
            }

            nodesToRecover.push({
                parent: parentNode,
                child: node
            });
            parentNode.removeChild(node);

            nodesToRemove.push({
                parent: parentNode,
                child: canvas
            });

            parentNode.appendChild(canvas);
        });
    }
    var dataURL;
    html2canvas(document.querySelector("#canvas1"),{
        //Whether to allow cross-origin images to taint the canvas
        allowTaint: true,
        //Whether to test each image if it taints the canvas before drawing them
        taintTest: false,
    }
    ).then(canvas => {
        $("#canvas1").remove();
        document.body.appendChild(canvas);
        //$("body").append("<canvas id='cvs'><canvas>");
        $("canvas").attr("id", "cvs");
        // var cvs = document.getElementById("cvs");
        // console.log(cvs);
        var cvs = document.getElementById("cvs");
        //var cvs = $("canvas");
        //console.log(cvs);
        dataURL = cvs.toDataURL();
        //Canvas2Image.saveAsImage(canvas, 760, 1000, 'png');
        $("#canvas").find("#border").attr("style","height:1000px;border:0.5px solid black");
        $("canvas").remove();
        var data = get_network();
        data["graph"] = dataURL;
        //上一版本中的save_network
        //如果可能的话，希望使用异步回调更漂亮地解决
        save_network_origin(data);
    });
    //console.log(dataURL);
    //return Promise.resolve(dataURL);            
}

async function save_network_origin(data) {
    $("#save_modal").modal('hide');
    // if (!window.sessionStorage.hasOwnProperty("userinfo")) {
    //     jump_to_login();
    //     return
    // }
    //var data = await get_network();
    // data.then(num => {
    //     console.log(num);
    // })
    console.log(data);
    //alert(window.location.href);
    var query_object = getQueryObject(window.location.href);
    if (query_object.hasOwnProperty("id")) {
        var net_id = query_object["id"];
        $.ajax({
            type: 'PUT',
            url: gobalConfig.base_url + 'api/NeuralNetwork/network/' + net_id + '/',
            data: JSON.stringify(data),
            contentType: 'application/json; charset=UTF-8',
            beforeSend: function (XMLHttpRequest) {
                var token = window.sessionStorage.getItem('token');
                if (token != null) {
                    XMLHttpRequest.setRequestHeader("Authorization", "JWT " + token)
                }
            },
            success: function (data_return) {
                alert("保存成功！");
            },
            error: function (data_return) {
                alert(data_return["responseText"]);
            }
        });
    } else {
        $.ajax({
            type: 'POST',//这个地方wf改了一下，应该是POST
            url: gobalConfig.base_url + 'api/NeuralNetwork/network/',
            data: JSON.stringify(data),
            contentType: 'application/json; charset=UTF-8',
            beforeSend: function (XMLHttpRequest) {
                var token = window.sessionStorage.getItem('token');
                if (token != null) {
                    XMLHttpRequest.setRequestHeader("Authorization", "JWT " + token)
                }
            },
            success: function (data_return) {
                alert("保存成功！");
                console.log(data_return);
            },
            error: function (data_return) {
                alert("失败了，后端没接主post请求");
                alert(data_return["responseText"]);
            }
        });
    }
}



function save_attr_linear_layer(button) {
    //这里是硬编码，考虑在b版本优化
    var id = button["id"].split("popover_")[1];
    var form = $("#" + button["id"]).parent();
    var in_features = form.find("[name = \"in_features\"]");
    var out_features = form.find("[name = \"out_features\"]");
    //todo:加入更精确的正则判断
    form.find("[name='input_error']").remove();
    //正整数
    var reg = /^\s*[1-9]\d*\s*$/;
    var flag = true;
    var check_array = [in_features, out_features];
    check_array.forEach(function (value, index, array) {
        if (!reg.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>请输入正整数</p>");
            flag = false;
        }
    });
    if (!flag) {
        return;
    }
    window.sessionStorage.setItem(id, "{\"in_features\":\"" + in_features.val() + "\", \"out_features\":\"" + out_features.val() + "\"}");
    $("#" + id).popover('hide');
}

function save_attr_view_layer(button) {
    //这里是硬编码，考虑在b版本优化
    var id = button["id"].split("popover_")[1];
    var form = $("#" + button["id"]).parent();
    var shape = form.find("[name = \"shape\"]");
    form.find("[name='input_error']").remove();
    //匹配符合要求的数组
    var reg = /^(\s*[1-9]\d*\s*)+(,\s*[1-9]\d*\s*)*$/;
    if (!reg.test(shape.val())) {
        shape.after("<p name='input_error' class='alert_font'>输入不合法</p>");
        return;

    }
    window.sessionStorage.setItem(id, "{\"shape\":\"" + shape.val() + "\"}");
    $("#" + id).popover('hide');
}

function save_attr_concatenate_layer(button) {
    var id = button["id"].split("popover_")[1];
    var form = $("#" + button["id"]).parent();
    var dim = form.find("[name = \"dim\"]");
    form.find("[name='input_error']").remove();
    var reg = /^\s*\d+\s*$/;
    if (!reg.test(dim.val())) {
        dim.after("<p name='input_error' class='alert_font'>输入不合法</p>");
        return;
    }
    window.sessionStorage.setItem(id, "{\"dim\":\"" + dim.val() + "\"}");
    $("#" + id).popover('hide');
}

function save_attr_conv1d_layer(button) {
    //这里是硬编码，考虑在b版本优化
    var id = button["id"].split("popover_")[1];
    var form = $("#" + button["id"]).parent();
    var in_channels = form.find("[name = \"in_channels\"]");
    var out_channels = form.find("[name = \"out_channels\"]");
    var kernel_size = form.find("[name = \"kernel_size\"]");
    var stride = form.find("[name = \"stride\"]");
    var padding = form.find("[name = \"padding\"]");
    var activity = form.find("[id=\"" + id + "activity\"]").find("option:selected").val();
    var pool_way = form.find("[id=\"" + id + "pool_way\"]").find("option:selected").val();
    //console.log(pool_way);
    var pool_kernel_size = form.find("[name = \"pool_kernel_size\"]");
    var pool_stride = form.find("[name = \"pool_stride\"]");
    var pool_padding = form.find("[name = \"pool_padding\"]");
    //todo:加入更精确的正则判断
    form.find("[name='input_error']").remove();
    var reg = /^\s*[1-9]\d*\s*$/;
    var reg_zero = /^\s*\d+\s*$/;
    var flag = true;
    var check_array1 = (pool_way=="None")?[in_channels, out_channels, kernel_size, stride]:[in_channels, out_channels, kernel_size, stride,pool_kernel_size,pool_stride];
    check_array1.forEach(function (value, index, array) {
        if (!reg.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>输入不合法</p>");
            flag = false;
        }
    });
    var check_array2 = (pool_way=="None")?[padding]:[padding,pool_padding];
    check_array2.forEach(function (value, index, array) {
        if (!reg_zero.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>输入不合法</p>");
            flag = false;
        }
    });
    if (!flag) {
        return;
    }
    //var activity = form.find("[name = \"activity\"]").val();
    //var pool_way = form.find("[name = \"pool_way\"]").val();
    window.sessionStorage.setItem(id, "{\"in_channels\":\"" + in_channels.val() + "\", \"out_channels\":\"" + out_channels.val() + "\", \"kernel_size\":\"" + kernel_size.val() + "\", " +
        "\"stride\":\"" + stride.val() + "\", \"padding\":\"" + padding.val() + "\",\"activity\":\"" + activity + "\",\"pool_way\":\"" + pool_way + "\",\"pool_kernel_size\":\"" + pool_kernel_size.val() + "\"," +
        "\"pool_stride\":\"" + pool_stride.val() + "\",\"pool_padding\":\"" + pool_padding.val() + "\"}");
    $("#" + id).popover('hide');
}

function save_attr_conv2d_layer(button) {
    //这里是硬编码，考虑在b版本优化
    var id = button["id"].split("popover_")[1];
    var form = $("#" + button["id"]).parent();
    var in_channels = form.find("[name = \"in_channels\"]");
    var out_channels = form.find("[name = \"out_channels\"]");
    var kernel_size = form.find("[name = \"kernel_size\"]");
    var stride = form.find("[name = \"stride\"]");
    var padding = form.find("[name = \"padding\"]");
    var activity = form.find("[id=\"" + id + "activity\"]").find("option:selected").val();
    var pool_way = form.find("[id=\"" + id + "pool_way\"]").find("option:selected").val();
    var pool_kernel_size = form.find("[name = \"pool_kernel_size\"]");
    var pool_stride = form.find("[name = \"pool_stride\"]");
    var pool_padding = form.find("[name = \"pool_padding\"]");
    //todo:加入更精确的正则判断
    form.find("[name='input_error']").remove();
    var reg = /^\s*[1-9]\d*\s*$/;
    var reg_zero = /^\s*\d+\s*$/;
    var flag = true;
    var check_array1 = (pool_way=="None")?[in_channels, out_channels, kernel_size, stride]:[in_channels, out_channels, kernel_size, stride,pool_kernel_size,pool_stride];
    check_array1.forEach(function (value, index, array) {
        if (!reg.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>输入不合法</p>");
            flag = false;
        }
    });
    var check_array2 = (pool_way=="None")?[padding]:[padding,pool_padding];
    check_array2.forEach(function (value, index, array) {
        if (!reg_zero.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>输入不合法</p>");
            flag = false;
        }
    });
    if (!flag) {
        return;
    }
    //var activity = form.find("[name = \"activity\"]").val();
    //var pool_way = form.find("[name = \"pool_way\"]").val();
    window.sessionStorage.setItem(id, "{\"in_channels\":\"" + in_channels.val() + "\", \"out_channels\":\"" + out_channels.val() + "\", \"kernel_size\":\"" + kernel_size.val() + "\", " +
        "\"stride\":\"" + stride.val() + "\", \"padding\":\"" + padding.val() + "\",\"activity\":\"" + activity + "\",\"pool_way\":\"" + pool_way + "\",\"pool_kernel_size\":\"" + pool_kernel_size.val() + "\"," +
        "\"pool_stride\":\"" + pool_stride.val() + "\",\"pool_padding\":\"" + pool_padding.val() + "\"}");
    $("#" + id).popover('hide');
}




function save_attr_linear_layer_form(id) {
    //这里是硬编码，考虑在b版本优化

    var form = $("#form" + id).parent();
    var in_features = form.find("[name = \"in_features\"]");
    var out_features = form.find("[name = \"out_features\"]");
    //todo:加入更精确的正则判断
    form.find("[name='input_error']").remove();
    //正整数
    var reg = /^\s*[1-9]\d*\s*$/;
    var flag = true;
    var check_array = [in_features, out_features];
    check_array.forEach(function (value, index, array) {
        if (!reg.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>请输入正整数</p>");
            flag = false;
        }
    });
    if (!flag) {
        return;
    }
    window.sessionStorage.setItem(id, "{\"in_features\":\"" + in_features.val() + "\", \"out_features\":\"" + out_features.val() + "\"}");
    $("#" + id).popover('hide');
}

function save_attr_view_layer_form(id) {
    //这里是硬编码，考虑在b版本优化
    var form = $("#form" + id).parent();
    var shape = form.find("[name = \"shape\"]");
    form.find("[name='input_error']").remove();
    //匹配符合要求的数组
    //var reg = /^((\s*[1-9]\d*\s*)|(\-1))+((,\s*[1-9]\d*\s*)|(,\-1))*$/;
    var reg = /^(\+?\d+|\-1)(\s*,\s*(\+?\d+|\-1))*$/;
    if (!reg.test(shape.val())) {
        shape.after("<p name='input_error' class='alert_font'>输入不合法</p>");
        return;

    }
    window.sessionStorage.setItem(id, "{\"shape\":\"" + shape.val() + "\"}");
    $("#" + id).popover('hide');
}

function save_attr_concatenate_layer_form(id) {
    var form = $("#form" + id).parent();
    var dim = form.find("[name = \"dim\"]");
    form.find("[name='input_error']").remove();
    var reg = /^\s*\d+\s*$/;
    if (!reg.test(dim.val())) {
        dim.after("<p name='input_error' class='alert_font'>输入不合法</p>");
        return;
    }
    window.sessionStorage.setItem(id, "{\"dim\":\"" + dim.val() + "\"}");
    $("#" + id).popover('hide');
}

function save_attr_conv1d_layer_form(id) {
    //这里是硬编码，考虑在b版本优化
    var form = $("#form" + id).parent();
    var in_channels = form.find("[name = \"in_channels\"]");
    var out_channels = form.find("[name = \"out_channels\"]");
    var kernel_size = form.find("[name = \"kernel_size\"]");
    var stride = form.find("[name = \"stride\"]");
    var padding = form.find("[name = \"padding\"]");
    var activity = form.find("[id=\"" + id + "activity\"]").find("option:selected").val();
    var pool_way = form.find("[id=\"" + id + "pool_way\"]").find("option:selected").val();
    //console.log(pool_way);
    var pool_kernel_size = form.find("[name = \"pool_kernel_size\"]");
    var pool_stride = form.find("[name = \"pool_stride\"]");
    var pool_padding = form.find("[name = \"pool_padding\"]");
    //todo:加入更精确的正则判断
    form.find("[name='input_error']").remove();
    var reg = /^\s*[1-9]\d*\s*$/;
    var reg_zero = /^\s*\d+\s*$/;
    var flag = true;
    var check_array1 = (pool_way=="None")?[in_channels, out_channels, kernel_size, stride]:[in_channels, out_channels, kernel_size, stride,pool_kernel_size,pool_stride];
    check_array1.forEach(function (value, index, array) {
        if (!reg.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>输入不合法</p>");
            flag = false;
        }
    });
    var check_array2 = (pool_way=="None")?[padding]:[padding,pool_padding];
    check_array2.forEach(function (value, index, array) {
        if (!reg_zero.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>输入不合法</p>");
            flag = false;
        }
    });
    if (!flag) {
        return;
    }
    //var activity = form.find("[name = \"activity\"]").val();
    //var pool_way = form.find("[name = \"pool_way\"]").val();
    window.sessionStorage.setItem(id, "{\"in_channels\":\"" + in_channels.val() + "\", \"out_channels\":\"" + out_channels.val() + "\", \"kernel_size\":\"" + kernel_size.val() + "\", " +
        "\"stride\":\"" + stride.val() + "\", \"padding\":\"" + padding.val() + "\",\"activity\":\"" + activity + "\",\"pool_way\":\"" + pool_way + "\",\"pool_kernel_size\":\"" + pool_kernel_size.val() + "\"," +
        "\"pool_stride\":\"" + pool_stride.val() + "\",\"pool_padding\":\"" + pool_padding.val() + "\"}");
    $("#" + id).popover('hide');
}

function save_attr_conv2d_layer_from(id) {
    //这里是硬编码，考虑在b版本优化
    var form = $("#form" + id).parent();
    var in_channels = form.find("[name = \"in_channels\"]");
    var out_channels = form.find("[name = \"out_channels\"]");
    var kernel_size = form.find("[name = \"kernel_size\"]");
    var stride = form.find("[name = \"stride\"]");
    var padding = form.find("[name = \"padding\"]");
    var activity = form.find("[id=\"" + id + "activity\"]").find("option:selected").val();
    var pool_way = form.find("[id=\"" + id + "pool_way\"]").find("option:selected").val();
    var pool_kernel_size = form.find("[name = \"pool_kernel_size\"]");
    var pool_stride = form.find("[name = \"pool_stride\"]");
    var pool_padding = form.find("[name = \"pool_padding\"]");
    //todo:加入更精确的正则判断
    form.find("[name='input_error']").remove();
    var reg = /^\s*[1-9]\d*\s*$/;
    var reg_zero = /^\s*\d+\s*$/;
    var flag = true;
    var check_array1 = (pool_way=="None")?[in_channels, out_channels, kernel_size, stride]:[in_channels, out_channels, kernel_size, stride,pool_kernel_size,pool_stride];
    check_array1.forEach(function (value, index, array) {
        if (!reg.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>输入不合法</p>");
            flag = false;
        }
    });
    var check_array2 = (pool_way=="None")?[padding]:[padding,pool_padding];
    check_array2.forEach(function (value, index, array) {
        if (!reg_zero.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>输入不合法</p>");
            flag = false;
        }
    });
    //var activity = form.find("[name = \"activity\"]").val();
    //var pool_way = form.find("[name = \"pool_way\"]").val();
    window.sessionStorage.setItem(id, "{\"in_channels\":\"" + in_channels.val() + "\", \"out_channels\":\"" + out_channels.val() + "\", \"kernel_size\":\"" + kernel_size.val() + "\", " +
        "\"stride\":\"" + stride.val() + "\", \"padding\":\"" + padding.val() + "\",\"activity\":\"" + activity + "\",\"pool_way\":\"" + pool_way + "\",\"pool_kernel_size\":\"" + pool_kernel_size.val() + "\"," +
        "\"pool_stride\":\"" + pool_stride.val() + "\",\"pool_padding\":\"" + pool_padding.val() + "\"}");
    $("#" + id).popover('hide');
}

function save_attr_softmax_layer_form(id){
    var form = $("#form" + id).parent();
    var dim = form.find("[name = \"dim\"]");
    form.find("[name='input_error']").remove();
    var reg = /^\s*\d+\s*$/;
    if (!reg.test(dim.val())) {
        dim.after("<p name='input_error' class='alert_font'>输入不合法</p>");
        return;
    }
    window.sessionStorage.setItem(id, "{\"dim\":\"" + dim.val() + "\"}");
    $("#" + id).popover('hide');
}

function save_attr_dropout_layer_form(id){
    var form = $("#form" + id).parent();
    var p = form.find("[name = \"p\"]");
    var type = form.find("[id=\"" + id + "type\"]").find("option:selected").val();
    //console.log(type);
    form.find("[name='input_error']").remove();
    var reg = /^\s*\d+\s*$/;
    if (!reg.test(p.val())) {
        p.after("<p name='input_error' class='alert_font'>输入不合法</p>");
        return;
    }

    window.sessionStorage.setItem(id, "{\"type\":\"" + type +" \",\"p\":\"" + p.val() + "\"}");
    $("#" + id).popover('hide');
}

function save_attr_conv_layer_form(id){
    //这里是硬编码，考虑在b版本优化
    var form = $("#form" + id).parent();
    var layer_type = form.find("[id=\"" + id + "layer_type\"]").find("option:selected").val();
    var type = form.find("[id=\"" + id + "type\"]").find("option:selected").val();
    var in_channels = form.find("[name = \"in_channels\"]");
    var out_channels = form.find("[name = \"out_channels\"]");
    var kernel_size = form.find("[name = \"kernel_size\"]");
    var stride = form.find("[name = \"stride\"]");
    var padding = form.find("[name = \"padding\"]");

//in_channel(int):输入通道数 非0正数 无默认值

// out_channel(int):输出通道数 非0正数 无默认值

// kernel_size (int) : 卷积核的尺寸 非0正数 无默认值

// stride (int) : 卷积步长 非0正数 默认值为1

// padding (int) : 补充0的层数 非负整数 默认值为0
    //todo:加入更精确的正则判断
    form.find("[name='input_error']").remove();
    var reg = /^\s*[1-9]\d*\s*$/;
    var reg_zero = /^\s*\d+\s*$/;
    var flag = true;
    var check_array1 = [in_channels, out_channels, kernel_size, stride];
    check_array1.forEach(function (value, index, array) {
        if (!reg.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>输入不合法</p>");
            flag = false;
        }
    });
    var check_array2 = [padding];
    check_array2.forEach(function (value, index, array) {
        if (!reg_zero.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>输入不合法</p>");
            flag = false;
        }
    });
    if (!flag) {
        return;
    }
    //var activity = form.find("[name = \"activity\"]").val();
    //var pool_way = form.find("[name = \"pool_way\"]").val();
    window.sessionStorage.setItem(id, "{ \"layer_type\":\""+layer_type+"\",\"type\":\""+ type +"\",\"in_channels\":\"" + in_channels.val() + "\", \"out_channels\":\"" + out_channels.val() + "\", \"kernel_size\":\"" + kernel_size.val() + "\", " +
        "\"stride\":\"" + stride.val() + "\", \"padding\":\"" + padding.val() + "\"}");
    $("#" + id).popover('hide');
}

function save_attr_pool_layer_form(id){
    var form = $("#form" + id).parent();
    var layer_type = form.find("[id=\"" + id + "layer_type\"]").find("option:selected").val();
    var type = form.find("[id=\"" + id + "type\"]").find("option:selected").val();
    var kernel_size = form.find("[name = \"kernel_size\"]");
    var stride = form.find("[name = \"stride\"]");
    var padding = form.find("[name = \"padding\"]");
    var ceil_mode = form.find("[id=\"" + id + "ceil_mode\"]").find("option:selected").val();
    var count_include_pad = form.find("[id=\"" + id + "count_include_pad\"]").find("option:selected").val();
//layer_type:下拉框三选一，选项包括max_pool/avg_pool/max_unpool 无默认值
// type:下拉框三选一，选项包括1d/2d/3d 无默认值

// kernel_size (int) : 卷积核的尺寸 非0正数 无默认值

// stride (int) : 卷积步长 非0正数 无默认值

// padding (int) : 补充0的层数 非负整数 默认值为0

// ceil_mode:下拉框二选一，ceil/floor 默认值为floor

// count_include_pad:下拉框二选一,true/false 默认值为true
    //todo:加入更精确的正则判断
    form.find("[name='input_error']").remove();
    var reg = /^\s*[1-9]\d*\s*$/;
    var reg_zero = /^\s*\d+\s*$/;
    var flag = true;
    var check_array1 = [kernel_size, stride];
    check_array1.forEach(function (value, index, array) {
        if (!reg.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>输入不合法</p>");
            flag = false;
        }
    });
    var check_array2 = [padding];
    check_array2.forEach(function (value, index, array) {
        if (!reg_zero.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>输入不合法</p>");
            flag = false;
        }
    });
    if (!flag) {
        return;
    }
    //var activity = form.find("[name = \"activity\"]").val();
    //var pool_way = form.find("[name = \"pool_way\"]").val();
    window.sessionStorage.setItem(id, "{ \"layer_type\":\""+ layer_type + "\",\"type\":\""+ type +"\",\"kernel_size\":\"" + kernel_size.val() + "\", " + "\"stride\":\"" + stride.val() + "\", \"padding\":\"" + padding.val() + "\",\"ceil_mode\":\""+ ceil_mode + "\",\"count_include_pad\":\"" + count_include_pad + "\"}");
    $("#" + id).popover('hide');

}

function save_attr_activation_layer_form(id){
    var form = $("#form" + id).parent();
    var layer_type = form.find("[id=\"" + id + "layer_type\"]").find("option:selected").val();
    var negative_slope = form.find("[name = \"negative_slope\"]");
    var weight = form.find("[name = \"weight\"]");
    var lower = form.find("[name = \"lower\"]");
    var upper = form.find("[name = \"upper\"]");
    form.find("[name='input_error']").remove();
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
//
    var positive = /^([1-9][0-9]*(\.\d+)?)|(0\.\d+)$/;
    var flag = true;
    var check_array1 = [negative_slope, weight,lower,upper];
    check_array1.forEach(function (value, index, array) {
        if (!positive.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>输入不合法</p>");
            flag = false;
        }
    });
    if (!flag) {
        return;
    }
    window.sessionStorage.setItem(id,"{\"layer_type\":\""+ layer_type +"\",\"negative_slope\":\""+ negative_slope.val() +"\",\"weight\":\""+ weight.val() +"\",\"lower\":\""+ lower.val() +"\",\"upper\":\"" + upper.val()+ "\"}");
    $("#" + id).popover('hide');

}
function save_attr_RNN_layer_form(id){
    var form = $("#form" + id).parent();
    var input_size = form.find("[name = \"input_size\"]");
    var hidden_size = form.find("[name = \"hidden_size\"]");
    var num_layers = form.find("[name = \"num_layers\"]");
    var nonlinearity = form.find("[id=\"" + id + "nonlinearity\"]").find("option:selected").val();
    form.find("[name='input_error']").remove();
// RNN_layer:递归神经网络(新增网络层)#
// input_size<正整数>：输入特征数 无默认值

// hidden_size<正整数>:隐藏层个数 无默认值

// num_layers<正整数>:递归层层数 默认值为1

// nonlinearity(二选一,tanh/relu):非线性激活 默认为tanh
    var positive_integer = /^[1-9]\d*$/;
    var flag = true;
    var check_array1 = [input_size, hidden_size,num_layers];
    check_array1.forEach(function (value, index, array) {
        if (!positive_integer.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>输入不合法</p>");
            flag = false;
        }
    });
    if (!flag) {
        return;
    }

    window.sessionStorage.setItem(id,"{\"input_size\":\""+input_size.val()+"\",\"hidden_size\":\""+input_size.val()+"\",\"num_layers\":\""+num_layers.val()+"\",\"nonlinearity\":\""+nonlinearity+"\"}");
    $("#" + id).popover('hide');
}

function save_attr_LSTM_layer_form(id){
    var form = $("#form" + id).parent();
    var input_size = form.find("[name = \"input_size\"]");
    var hidden_size = form.find("[name = \"hidden_size\"]");
    var num_layers = form.find("[name = \"num_layers\"]");
    form.find("[name='input_error']").remove();
// input_size<正整数>:输入特征数 无默认值

// hidden_size<正整数> :隐藏层个数 无默认值

// num_layers<正整数>:递归层层数 默认值为1
    var positive_integer = /^[1-9]\d*$/;
    var flag = true;
    var check_array1 = [input_size, hidden_size,num_layers];
    check_array1.forEach(function (value, index, array) {
        if (!positive_integer.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>输入不合法</p>");
            flag = false;
        }
    });
    if (!flag) {
        return;
    }

    window.sessionStorage.setItem(id,"{\"input_size\":\""+input_size.val()+"\",\"hidden_size\":\""+input_size.val()+"\",\"num_layers\":\""+num_layers.val()+"\"}");
    $("#" + id).popover('hide');
}


function save_attr_norm_layer_form(id){
    var form = $("#form" + id).parent();
    var layer_type = form.find("[id=\"" + id + "layer_type\"]").find("option:selected").val();
    var type = form.find("[id=\"" + id + "type\"]").find("option:selected").val();
    var num_features = form.find("[name = \"num_features\"]");
    var num_groups = form.find("[name = \"num_groups\"]");
    var num_channel = form.find("[name = \"num_channel\"]");
    form.find("[name='input_error']").remove();
// 下拉框,选项包括batch_norm/group_norm/instance_norm 默认值为batch_norm

// batch_norm参数:

// type:下拉框，包括1d/2d/3d 默认值为2d

// num_features<正整数>:输入特征数 无默认值

// group_norm参数:

// num_groups<正整数>:input_channel分组数 无默认值

// num_channel<正整数>:input_channel个数无默认值

// instance_norm参数:

// type:下拉框，包括1d/2d/3d 默认值为2d

// num_features<正整数>:输入特征数 无默认值
    var positive_integer = /^[1-9]\d*$/;
    var flag = true;
    var check_array1 = [num_features, num_groups,num_channel];
    check_array1.forEach(function (value, index, array) {
        if (!positive_integer.test(value.val())) {
            value.after("<p name='input_error' class='alert_font'>输入不合法</p>");
            flag = false;
        }
    });
    if (!flag) {
        return;
    }

    window.sessionStorage.setItem(id,"{\"layer_type\":\""+layer_type+"\",\"type\":\""+type+"\",\"num_features\":\""+num_features.val()+"\",\"num_groups\":\""+num_groups.val()+"\",\"num_channel\":\""+num_channel.val()+"\"}");
    $("#" + id).popover('hide');
}



