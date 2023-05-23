import pandas as pd
import matplotlib.pyplot as plt

path_txt = './FastCUT_loss_log.txt'

file1 = open(path_txt, 'r') 
lines = file1.readlines()
dicts = list()
l1 = []
l2 = []
l3 = []
for i, line in enumerate(lines):
    if i < 2:
        continue
    parts = line.split(') ')[1].split(' ')
    parts.pop(-1)
    dict_tmp = dict()
    l1.append(float(parts[1]))
    # l2.append(float(parts[5]))
    dict_tmp['G_GAN'] = float(parts[1])
    dict_tmp['D_real'] = float(parts[3])
    dict_tmp['D_fake'] = float(parts[5])
    dict_tmp['NCE'] = float(parts[7])
    dicts.append(dict_tmp)


for i in range(1,len(l1)+1):
    l3.append(float(i/1550)*100)

plt.title('GAN loss for Generator')
plt.plot(l3,l1,color='silver')
# plt.plot(l3,l2,color='brown',label='fake')
plt.xlabel('Number of epochs')
plt.ylabel('Loss')
# plt.legend()
plt.show()

df = pd.DataFrame(dicts)
print(df)