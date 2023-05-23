import os
import shutil
from shutil import copyfile
imgtype = ['real_A','real_B','fake_B']
for i in imgtype:
    if not os.path.exists(f'./{i}'):
        os.mkdir(f'./{i}')
for i in os.listdir('.'):
    if i.endswith('.py'):
        pass
    if os.path.isfile(f'./{i}'):
        source = f'./{i}'
        destination = f'./{i[-10:-4]}'
        shutil.copy(source, destination)