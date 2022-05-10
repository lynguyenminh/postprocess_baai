import cv2
from os import listdir
from os.path import isfile, join


def list_file(mypath):
    return [mypath + '\\' + f for f in listdir(mypath) if isfile(join(mypath, f))]

txt_list = list_file(r'D:\scene-text_visualizedata\txt_output')
img_list = list_file(r'D:\scene-text_visualizedata\public_test_img')

# print(len(txt_list))
# print(len(txt_list))
# print(len(img_list))

def visulize(img_path, txt_path):
    img = cv2.imread(img_path)
    txt = open(txt_path, 'r', encoding="utf-8")
    lines = txt.readlines()

    # cv2.line(img, (20,10), (100,10), (255,0,0), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX

    # fontScale
    fontScale = 1
    
    # Blue color in BGR
    color = (255, 0, 0)
    
    # Line thickness of 2 px
    thickness = 2

    for line in lines: 
        coor = line.split(',')
        for i in range(0, 8, 1):
            coor[i] = int(coor[i])
        cv2.line(img, (coor[0], coor[1]), (coor[2],coor[3]), (255,0,0), 2)
        cv2.line(img, (coor[2], coor[3]), (coor[4],coor[5]), (255,0,0), 2)
        cv2.line(img, (coor[4], coor[5]), (coor[6],coor[7]), (255,0,0), 2)
        cv2.line(img, (coor[6], coor[7]), (coor[0],coor[1]), (255,0,0), 2)
        # Using cv2.putText() method
        # image = cv2.putText(img, coor[8], (coor[6], coor[7]), font, fontScale, color, thickness, cv2.LINE_AA)


    cv2.imwrite(r'D:\scene-text_visualizedata\visulize_predict' + '\\' + img_path.split('\\')[-1], img)



for i in txt_list:
    img_name = i[:28] + 'public_test_img\\img_' + i.split('\\')[-1][4:-3] + 'jpg'
    print(img_name)
    visulize(img_name, i)
# visulize('D:\\scene-text_visualizedata\\train_imgs\\training_img\\img_2.jpg', 'D:\\scene-text_visualizedata\\train_gt\\training_gt\\gt_img_2.txt')

