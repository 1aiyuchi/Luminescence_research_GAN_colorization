import pandas as pd
import matplotlib.pyplot as plt

path_txt = './copix2pix2_loss_log.txt'

file1 = open(path_txt, 'r') 
lines = file1.readlines()
dicts = list()
l1 = []
l2 = []
l3 = []
l4 = []
num = []
for i, line in enumerate(lines):
    if i < 2:
        continue
    parts = line.split(') ')[1].split(' ')
    parts.pop(-1)
    dict_tmp = dict()
    l1.append(float(parts[1]))
    l2.append(float(parts[3]))
    l3.append(float(parts[5]))
    l4.append(float(parts[7]))
    # dict_tmp['G_GAN'] = float(parts[1])
    # dict_tmp['G_L1'] = float(parts[3])
    # dict_tmp['D_real'] = float(parts[5])
    # dict_tmp['D_fake'] = float(parts[7])
    # dicts.append(dict_tmp)


for i in range(1,len(l1)+1):
    num.append(float(i/1050)*100)

# plt.title('pix2pix loss (ngf&ndf changed)')
plt.plot(num,l1,color='red',label='G_GAN')
plt.plot(num,l2,color='orange',label='G_L1')
plt.plot(num,l3,color='green',label='D_real')
plt.plot(num,l4,color='blue',label='D_fake')
plt.xlabel('Number of epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# df = pd.DataFrame(dicts)
# print(df)