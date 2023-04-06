import os
import shutil

# 設定目錄路徑和命名規則
root = os.path.dirname(os.path.abspath(__name__))
source_path = os.path.join(root,'img')
dir_path = os.path.join(root,'dir')


# 遍歷目錄下的所有檔案
for file_name in os.listdir(source_path):
    try:
        image_name = file_name.split(".")[0]
        externalpath = file_name.split(".")[1]

        dirimgfolder = dir_path+f'\\{image_name}'
        if not os.path.isdir(dirimgfolder):
            os.mkdir(dirimgfolder)
            
        dirimg = os.path.join(dirimgfolder,f'{image_name}.{externalpath}')
        sourceimg = os.path.join(source_path,file_name)
        shutil.move(sourceimg, dirimg)
    
        print("Success")
    except (IndexError, ValueError) as msg:
        print(f"Skip:{file_name}")
        print(f"Error:{msg}")