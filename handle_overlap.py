from overlap_area import score, area


def check_overlap(hcn1, hcn2):
    '''
    Kiem tra xem 2 box co overlap ko
    input: 2 list, moi list gom 8 gia tri la toa do cua hcn x1, y1, x2, y2, x3, y3, x4, y4
    output: true if overlab else false
    '''
    return not (hcn1[2] < hcn2[6] or hcn1[6] > hcn2[2] or hcn1[3] > hcn2[7] or hcn1[7] < hcn2[3])


def handle_coor_infile(path_txt):
    '''
    Doc file toa do txt thanh ma tran 2D chi chua toa do'''
    f = open(path_txt, 'r')
    lines = f.readlines()
    lines = [i.split(',')[:-1] for i in lines]
    result = []
    # lay 8 phan tu dau tien (8 diem toa do)
    for i in lines: 
        result.append(i if len(i) == 8 else i[:8])
    # chuyen toa do tu string thanh int
    for i in range(len(result)):
        result[i] = [int(j) for j in result[i]]
    
    return result



def merge_n_list(array, index):
    '''
    merge n list 1d lai voi nhau thanh 1 list'''
    result = []
    for i in index: 
        result += array[i]

    # xoa phan tu trung nhau trong list
    result = list(dict.fromkeys(result))

    return result


def group(list_read_from_txt):
    '''
    gom nhom cac bound box bi overlap lai voi nhau
    list_read_from_txt la danh sach toa do cac box doc tu file txt
    thresh la nguong khi xac dinh overlap
    list_box_overlap la mang 2d, moi mang 1d la cac box bi overlap
    final_list la list cuoi cung sau khi xu ly xong'''
    thresh = 0.9
    
    list_box_overlap = []
    for i in list_read_from_txt: 
        list_temp = [] 
        for j in list_read_from_txt: 
            if score(i, j) > thresh: 
                list_temp.append(list_read_from_txt.index(j))
        list_box_overlap.append(list_temp)

    # loai bo list trung
    list_box_overlap = [list(t) for t in set(tuple(element) for element in list_box_overlap)]

    final_list = []
    for i in range(len(list_read_from_txt)):
        merge_id = []
        for j in list_box_overlap:
            if i in j: 
                merge_id.append(list_box_overlap.index(j))

        # merge nhung list trong merge_id
        final_list.append(merge_n_list(list_box_overlap, merge_id))


    #  sap xep lai cac mang trong final_list, sau do loai bo list trung
    for h in range(len(final_list)):
        final_list[h].sort() 
    final_list = [list(t) for t in set(tuple(element) for element in final_list)]
        
    return final_list


def check_fullso(strings):
    '''
    check xem 1 string co chua toan so va dau cham ko => check sdt
    '''
    so = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    for i in strings: 
        if i not in so: 
            return False
    return True


def main_handle(path_txt):
    '''
    xu ly nhom cac bounding box bi overlap'''
    group_box = group(handle_coor_infile(path_txt))

    final_box = []
    coor_file = handle_coor_infile(path_txt)
    for i in group_box: 
        if len(i) == 1: 
            # final_box.append(coor_file[i[0]])
            final_box.append(i[0])
        elif len(i) == 2: 
            # lay box co dien tich lon hon
            if area(coor_file[i[0]]) < area(coor_file[i[1]]):
                # final_box.append(coor_file[i[1]])
                final_box.append(i[1])
            else: 
                final_box.append(i[0])
                # final_box.append(coor_file[i[0]])

        elif len(i) == 3: 
            # so dien thoai(chua so va dau cham) => gop thanh 1
            f = open(path_txt, 'r')
            lines = f.readlines()
            lines = [i.split(',') for i in lines]

            if (check_fullso(lines[i[0]][8][:-1]) and check_fullso(lines[i[1]][8][:-1]) and check_fullso(lines[i[2]][8][:-1])): 
                # gop
                dt1 = area(coor_file[i[0]])
                dt2 = area(coor_file[i[1]])
                dt3 = area(coor_file[i[2]])
                # print(dt1, dt2, dt3)

                if dt1 == max(dt1, dt2, dt3):
                    # final_box.append(coor_file[i[0]])
                    final_box.append(i[0])
                elif dt2 == max(dt1, dt2, dt3):
                    # final_box.append(coor_file[i[1]])
                    final_box.append(i[1])
                elif dt3 == max(dt1, dt2, dt3):
                    # final_box.append(coor_file[i[2]])
                    final_box.append(i[2])

    return final_box


def main(path_txt):
    '''
    ham tong hop code'''
    final_box = main_handle(path_txt)

    f = open(path_txt, 'r')
    lines = f.readlines()
    # final_coor = lines[final_box]
    final_coor = []
    for i in final_box: 
        final_coor.append(lines[i])

    return final_coor

# print(main('./output/res_img_506.txt'))