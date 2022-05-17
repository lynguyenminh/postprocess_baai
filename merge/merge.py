from os import listdir
from os.path import isfile, join

def list_dir(mypath):
    onlyfiles = [f  for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles




txt_file = list_dir('./submission_dictguided_40kiter')

print(txt_file)

for i in txt_file: 
    try:
        f1 = open('./500iters0.25/' + i, 'r')
        line1 = f1.readlines()
        f1.close()
    except: 
        line1 = []

    try: 
        f2 = open('./submission_dictguided_40kiter/' + i, 'r')
        line2 = f2.readlines()
        f2.close()
    except:
        line2 = []

    merge = line1 + line2
    f = open('./result/' +  i, 'w')
    for j in merge: 
        f.write(j)
    
    f.close()