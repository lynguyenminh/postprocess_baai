from os import listdir
from os.path import isfile, join
import argparse
import os


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--txt_1', type=str, required=True)
    parser.add_argument('--txt_2', type=str, required=True)
    return parser.parse_args()

def list_all_file(mypath):
    onlyfiles = [f  for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles

def get_content_file(file_path):
    try:
        f1 = open(file_path, 'r')
        lines = f1.readlines()
        f1.close()
    except: 
        lines = []
    return lines

def merge(args):
    path_1 = args.txt_1 if args.txt_1[-1] != '/' else (args.txt_1 + '/')
    path_2 = args.txt_2 if args.txt_2[-1] == '/' else (args.txt_2 + '/')

    # vi model yolo co the predict thieu file khi no khong detect dc chu trong anh. Nen ta lay tat ca file ma 2 model predict dc
    folder1 = list_all_file(path_1)
    folder2 = list_all_file(path_2)
    all_txt = folder1 + list(set(folder2) - set(folder1))

    for file in all_txt: 
        lines_1 = get_content_file(path_1 + file)
        lines_2 = get_content_file(path_2 + file)
        merge = lines_1 + lines_2
        f = open('./results/' +  file, 'w')
        for j in merge: 
            f.write(j)
        f.close()
        
if __name__=="__main__":
    if not os.path.exists('./results'):
        os.makedirs('./results')
        
    args = get_parser()
    merge(args)
