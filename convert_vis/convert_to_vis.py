import json,os
import re
import zipfile


COORS_8            = '^'+ ','.join(['\s*(-?[0-9]+)\s*']*8)
POINT_TRANS_8      = COORS_8 + ',(.*)$'

with zipfile.ZipFile('visualize.zip', 'a') as viszip:

    with zipfile.ZipFile('output-20220423T011651Z-001.zip', 'r') as archive:
        for name in archive.namelist():
            if not name.endswith('.txt'):
                continue
            json_name = name.split('/')[-1].split('.')[0]
            with archive.open(name) as f:
                lines = f.readlines()
                lines = [x.decode().strip('\n') for x in lines]
                write_dict = []
                for line in lines:
                    m = re.match(POINT_TRANS_8,line)
                    coors = [m.group(i) for i in range(1,9)]
                    all_points_x = list(map(int,coors[::2]))
                    all_points_y = list(map(int,coors[1::2]))
                    coors = list(zip(all_points_x,all_points_y))
                    trans = m.group(9)
                    write_dict.append({"transcription": trans,
                                        "points": coors})
            with open(json_name+'.json','w') as outjson:
                json.dump(
                    write_dict
                    ,outjson
                    ,indent=2)
            viszip.write(json_name+'.json', compress_type=zipfile.ZIP_DEFLATED)
            if os.path.exists(json_name+'.json'):
                os.remove(json_name+'.json')