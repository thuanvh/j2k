import json
import shutil
import os
mediamapfile = r"C:\Users\Thuan\Downloads\Core 2k_6k Optimized Japanese Vocabulary (1).apkg\media"
mediafolder = r"C:\Users\Thuan\Downloads\Core 2k_6k Optimized Japanese Vocabulary (1).apkg"
outputfolder = r"..\media"
data = json.load(open(mediamapfile,"r", encoding="utf-8"))
#os.mkdir(outputfolder)
print(type(data))
print(len(data))
#uncomment to gen file
# for k,v in data.items():
#   print(k,v)
#   print("copy", mediafolder + "\\" + k, outputfolder + "\\" + v)
#   shutil.copy(mediafolder + "\\" + k, outputfolder + "\\" + v)