# move.py，置於多資料夾的資料夾中，可將檔案取至 data 資料夾
import os
import shutil
if not os.path.exists('.\\data\\'):
    os.mkdir('.\\data\\')
i = 0
for folder_name in os.listdir("."):
    # print(folder_name)
    for file_name in os.listdir(f'.\\{folder_name}'):
        source = ".\\"+folder_name+"\\"+file_name
        destination = f".\\data\\{i}.png"
        shutil.copy(source,destination)
        print("copied",f".\\data\\{i}.png")
        i += 1