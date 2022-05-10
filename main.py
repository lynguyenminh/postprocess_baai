from multiprocessing.spawn import old_main_modules
from handle_overlap import main

from os import listdir
from os.path import isfile, join


def list_file(mypath):
    onlyfiles = [mypath + '/' + f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles



txt_file = list_file('./output')

for i in txt_file: 
    non_overlap = main(i)
    print(i)
    f = open('./non_overlap/' + i.split('/')[-1], 'w')
    for j in non_overlap: 
        f.writelines(j)
    f.close()