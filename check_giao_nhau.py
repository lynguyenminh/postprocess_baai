
from overlap_area import score


def check_overlap(hcn1, hcn2):
    return not (hcn1[2] < hcn2[6] or hcn1[6] > hcn2[2] or hcn1[3] > hcn2[7] or hcn1[7] < hcn2[3])


def handle_coor_infile(path_txt):
    f = open(path_txt, 'r')
    lines = f.readlines()
    lines = [i.split(',')[:-1] for i in lines]
    result = []

    for i in lines: 
        result.append(i if len(i) == 8 else i[:8])

    for i in range(len(result)):
        result[i] = [int(j) for j in result[i]]
    
    return result


def group(list_rec):
    thresh = 0.4
    final_list = []
    for i in list_rec: 
        list_temp = [] 
        for j in list_rec: 
            if score(i, j) > thresh: 
                list_temp.append(list_rec.index(j))
        final_list.append(list_temp)
    return final_list



print(group(handle_coor_infile('./img_501.txt')))