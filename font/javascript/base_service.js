function getQueryObject(url) {
    url = url == null ? window.location.href : url;
    var search = url.substring(url.lastIndexOf("?") + 1);
    var obj = {};
    //一个经典漂亮的正则表达式
    var reg = /([^?&=]+)=([^?&=]*)/g;
    search.replace(reg, function (rs, $1, $2) {
        var name = decodeURIComponent($1);
        var val = decodeURIComponent($2);
        val = String(val);
        obj[name] = val;
        return rs;
    });
    return obj;
}

function login() {

    var username = $("#username_log").val();
    var password = $("#pwd_log").val();

    var data = {
        "username": username,
        "password": password
    };

    $.ajax({
        type: 'POST',
        url: gobalConfig.base_url + 'api/user/login/',
        async: false,//note：这里ajax必须为同步请求，两个ajax必须先拿token,再拿用户信息
        data: JSON.stringify(data),
        contentType: 'application/json; charset=UTF-8',
        success: function (data_return) {
            var token = data_return["token"];
            window.sessionStorage.setItem('token', token)
        },
        error: function (data_return) {
            alert("账号密码错误或账号未激活，请重新登录");
            console.log(data_return["responseText"])
        }
    });
    $.ajax({
        type: 'GET',
        async: false,
        url: gobalConfig.base_url + 'api/user/info/',
        beforeSend: function (XMLHttpRequest) {
            var token = window.sessionStorage.getItem('token');
            if (token != null) {
                XMLHttpRequest.setRequestHeader("Authorization", "JWT " + token)
            }
        },
        success: function (data_return) {
            window.sessionStorage.setItem('userinfo', JSON.stringify(data_return));
            //window.location.href = "canvas.html"
            window.location.reload();
        }
    });
}


function register() {
    //todo:加正则判断
    var username = $("#username_reg").val();
    var password = $("#pwd_reg").val();
    if ($('#pwd_confirm_reg').val() != password) {
        alert("两次输入密码不一致");
        return;
    }
    var email = $("#email_reg").val();

    var data = {
        "username": username,
        "email": email,
        "password": password,
        "is_active": false,
    };

    $.ajax({
        type: 'POST',
        url: gobalConfig.base_url + 'api/user/register/',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=UTF-8',
        success: function (data_return) {
            // var token = data_return["token"];
            // window.sessionStorage.setItem('token', token);
            // window.sessionStorage.setItem('userinfo', JSON.stringify(data_return));
            window.location.reload();
            alert("注册成功，请前往邮箱验证后登录")
        },
        error: function (data_return) {
            alert("用户名或邮箱已被注册")
            //iconsole.log(data_return["responseText"])
            window.location.reload();
        }
    })

}

function logout() {
    window.sessionStorage.removeItem('token');
    window.sessionStorage.removeItem('userinfo');
    window.location.reload();
}

function add_comment() {
    var title = $("#contact-info").val();
    var context = $("#question-describe").val();
    var picname = $("#contact-info").val();
    alert(picname);
    var data = {
        "title": title,
        "context": context,
    };
    $.ajax({
        type: 'POST',
        url: gobalConfig.base_url + 'api/comments/',
        data: JSON.stringify(data),
        contentType: 'application/json; charset=UTF-8',
        beforeSend: function (XMLHttpRequest) {
            var token = window.sessionStorage.getItem('token');
            if (token != null) {
                XMLHttpRequest.setRequestHeader("Authorization", "JWT " + token)
            }
        },
        success: function (data_return) {
            //alert("success");
            window.location.href = "feedback.html"
        },
        error: function (data_return) {
            //alert("error")
        }
    });
}


function loadImage(img) {
    var filePath = img.value;
    var fileExt = filePath.substring(filePath.lastIndexOf("."))
        .toLowerCase();

    if (!checkFileExt(fileExt)) {
        alert("您上传的文件不是jpg格式图片,请重新上传！");
        img.value = "";
        return;
    }
    if (img.files && img.files[0]) {
//                alert(img);
//                alert(img.files[0])
        if (img.files[0].size / 1024 > 5120) {
            img.value = "";
            alert("您上传的图片过大，请保证图片在5M以内")
            return;
        }

        alert('你选择的文件大小' + (img.files[0].size / 1024).toFixed(0) + "kb");
//                var xx = img.files[0];
//                for (var i in xx) {
//                    alert(xx[i])
//                }
    }
}

function checkFileExt(ext) {
    if (!ext.match(/.jpg/i)) {
        return false;
    }
    return true;
}


function isImage(filepath) {
    var extStart = filepath.lastIndexOf(".");
    var ext = filepath.substring(extStart, filepath.length).toUpperCase();
    if (ext != ".PNG" && ext != ".JPG" && ext != ".JPEG") {
        alert("图片只能为png,jpeg,jpg格式");
        window.location.reload();
        return false;
    }
    return true;
}

function checkFileSize(filepath) {
    var maxsize = 5 * 1024 * 1024;//2M
    var errMsg = "上传的待预测图片文件不能超过5M!";
    var tipMsg = "您的浏览器暂不支持上传图片，确保上传文件不要超过5M，建议使用Chrome/New Edge/FireFox浏览器。";

    try {
        var filesize = 0;
        var ua = window.navigator.userAgent;
        if (ua.indexOf("MSIE") >= 1) {
            //IE
            var img = new Image();
            img.src = filepath;
            filesize = img.fileSize;
        } else {
            //file_size = document.getElementById("imageFile").files[0].size;
            filesize = $("#photoFile")[0].files[0].size; //byte
        }

        if (filesize > 0 && filesize > maxsize) {
            alert(errMsg);
            return false;
        } else if (filesize == -1) {
            alert(tipMsg);
            return false;
        }
    } catch (e) {
        alert("上传失败，请重试");
        return false;
    }
    return true;
}