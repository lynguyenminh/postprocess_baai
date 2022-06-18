import cv2
from os import listdir
from os.path import isfile, join
import argparse

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, required=True)
    parser.add_argument('--txt', type=str, required=True)
    return parser.parse_args()


def list_file(mypath):
    return [f for f in listdir(mypath) if isfile(join(mypath, f))]

def draw_bbox(img_path, txt_path):
    img = cv2.imread(img_path)
    try: 
        txt = open(txt_path, 'r', encoding="utf-8")
        lines = txt.readlines()
        txt.close()
    except: 
        cv2.imwrite(r'./results/' + img_path.split('/')[-1], img)

    color = (255, 0, 0)
    thickness = 2

    for line in lines: 
        coor = line.split(',')
        for i in range(0, 8, 1):
            coor[i] = int(coor[i])
        cv2.line(img, (coor[0], coor[1]), (coor[2],coor[3]), color, thickness)
        cv2.line(img, (coor[2], coor[3]), (coor[4],coor[5]), color, thickness)
        cv2.line(img, (coor[4], coor[5]), (coor[6],coor[7]), color, thickness)
        cv2.line(img, (coor[6], coor[7]), (coor[0],coor[1]), color, thickness)
    cv2.imwrite(r'./results/' + img_path.split('/')[-1], img)

def visulize(args):
    img_path = args.image if args.image[-1] =='/' else (args.image + '/')
    txt_path = args.txt if args.txt[-1] == '/' else (args.txt + '/')

    img_list = list_file(img_path)
    for i in img_list: 
        draw_bbox(img_path + i, txt_path + 'res_' + i[:-3] + 'txt')

if __name__=="__main__":
    args = get_parser()
    visulize(args)