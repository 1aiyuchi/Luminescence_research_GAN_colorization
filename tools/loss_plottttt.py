import pandas as pd
import matplotlib.pyplot as plt

path_txt = './cyclegan_ngdf.txt'

file1 = open(path_txt, 'r') 
lines = file1.readlines()
da = []
ga = []
cyca = []
idta = []
db = []
gb = []
cycb = []
idtb = []
l = []
for i, line in enumerate(lines):
    if i < 2:
        continue
    parts = line.split(') ')[1].split(' ')
    parts.pop(-1)
    # dict_tmp = dict()
    da.append(float(parts[1]))
    ga.append(float(parts[3]))
    cyca.append(float(parts[5]))
    idta.append(float(parts[7]))
    db.append(float(parts[9]))
    gb.append(float(parts[11]))
    cycb.append(float(parts[13]))
    idtb.append(float(parts[15]))
    # dict_tmp['D_A'] = float(parts[1])
    # dict_tmp['G_A'] = float(parts[3])
    # dict_tmp['cycle_A'] = float(parts[5])
    # dict_tmp['idt_A'] = float(parts[7])
    # dict_tmp['D_B'] = float(parts[9])
    # dict_tmp['G_B'] = float(parts[11])
    # dict_tmp['cycle_B'] = float(parts[13])
    # dict_tmp['idt_B'] = float(parts[15])
    # dicts.append(dict_tmp)
for i in range(1,len(da)+1):
    l.append(float(i/1100)*100)

plt.xlabel('Number of epochs')
plt.ylabel('Loss')
plt.plot(l,da,label='D_A',color='blue')
plt.plot(l,ga,label='G_A',color='red')
plt.plot(l,cyca,label='cycle_A',color='green')
# plt.plot(l,idta,label='idt_A',color='orange')
plt.plot(l,db,label='D_B',color='purple')
plt.plot(l,gb,label='G_B',color='black')
plt.plot(l,cycb,label='cycle_B',color='gold')
# plt.plot(l,idtb,label='idt_B',color='brown')
plt.legend()
plt.show()

# df = pd.DataFrame(dicts)
# print(df)