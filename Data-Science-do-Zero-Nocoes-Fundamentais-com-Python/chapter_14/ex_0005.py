import os
def walk2(dirname):
    filesList = list()
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            if ('.jpg' in filename):
                filesList.append(filename)
    return filesList

fileList = walk2('documents')
for x in range(len(fileList)):
    print(fileList[x])
