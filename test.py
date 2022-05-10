from overlap_area import area

f = open('./output/res_img_506.txt', 'r')
lines = f.readlines()
lines = [i.split(',') for i in lines]

result = []

for i in lines: 
    result.append(i if len(i) == 8 else i[:8])

for i in range(len(result)):
    result[i] = [int(j) for j in result[i]]


print(area(result[13]))
print(area(result[18]))
print(area(result[19]))