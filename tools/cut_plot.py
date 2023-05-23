import pandas as pd
import matplotlib.pyplot as plt

path_txt = './CUT_loss_log.txt'

file1 = open(path_txt, 'r') 
lines = file1.readlines()
dicts = list()
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
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
    l5.append(float(parts[9]))
    dict_tmp['G_GAN'] = float(parts[1])
    dict_tmp['D_real'] = float(parts[3])
    dict_tmp['D_fake'] = float(parts[5])
    dict_tmp['NCE'] = float(parts[9])
    dict_tmp['NCE_Y'] = float(parts[11])
    dicts.append(dict_tmp)


for i in range(1,len(l1)+1):
    l6.append(float(i/1390)*100)

# plt.title('NCE_Y Loss')
# plt.plot(l3,l1,color='purple')
# plt.plot(l3,l2,color='green',label='D_fake')
plt.plot(l6,l1,color='blue',label='G_GAN')
plt.plot(l6,l2,color='red',label='D_real')
plt.plot(l6,l3,color='orange',label='D_fake')
plt.plot(l6,l4,color='green',label='NCE')
plt.plot(l6,l5,color='gold',label='NCE_Y')
plt.xlabel('Number of epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# df = pd.DataFrame(dicts)
# print(df)