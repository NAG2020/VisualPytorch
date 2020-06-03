def cut(str):
    end = 0
    count = 0
    for i in str:
        if (i == '\\' or i == '/'):
            end = count
        count += 1
    return str[end+1:]

print(cut("/home/VisualPytorch-develop/font/media/inference_img/bee2.jpg" ))
