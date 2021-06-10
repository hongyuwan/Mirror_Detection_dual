# Mirror_Detection_dual
文件夹中
infer.py为predict，运行该代码可对MSD文件中的test数据集进行镜子区域预测

config.py中更改test,train以及backbone路径

dataset.py对输入数据集进行处理

evaluate.py对predict预测图像进行Acc,IoU,Mae,Ber四个方面性能评估

joint_transforms.py将模型微调以适应双任务训练

loss.py为损失函数

mirrornet.py为镜子检测子网络结构

train_mirror_C.py为镜子分类子网络train

train_dual.py为镜双任务子检测网络train

validlabel.py用来验证标签正确性

MSD数据集下载地址https://drive.google.com/file/d/1Znw92fO6lCKfXejjSSyMyL1qtFepgjPI/view?usp=sharing

Pre-trained Model地址https://drive.google.com/file/d/1jCSk3VX7nypHbEcup6eTG4K7189irwIc/view?usp=sharing

数据集引用来自

@InProceedings{Yang_2019_ICCV,
    author = {Yang, Xin and Mei, Haiyang and Xu, Ke and Wei, Xiaopeng and Yin, Baocai and Lau, Rynson W.H.},
    title = {Where Is My Mirror?},
    booktitle = {The IEEE International Conference on Computer Vision (ICCV)},
    month = {October},
    year = {2019}
}
