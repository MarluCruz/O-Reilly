import os, hashlib, difflib
def walk2(dirname):
    filesList = list()
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            if ('.txt' in filename):
                path = open(os.path.join(root, filename))
                filesList.append(hashlib.md5(path.encode()))
    return filesList

fileList = walk2('documents')
for x in range(len(fileList)):
    print(fileList[x].hexdigest())
