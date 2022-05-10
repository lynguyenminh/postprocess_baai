from collections import namedtuple
Rectangle = namedtuple('Rectangle', 'xmin ymin xmax ymax')

hcn1 = [630,462,680,462,630,500,680,500]
hcn2 = [76,461,122,461,76,501,122,501,41]

def overlap_area(a, b):
    ra = Rectangle(a[0], a[1], a[4], a[5])
    rb = Rectangle(b[0], b[1], b[4], b[5])

    dx = min(ra.xmax, rb.xmax) - max(ra.xmin, rb.xmin)
    dy = min(ra.ymax, rb.ymax) - max(ra.ymin, rb.ymin)
    if (dx>=0) and (dy>=0):
        return dx*dy
    return 0


def area(a):
    '''input la list gom 8 toa do'''
    w = a[4] - a[0]
    h = a[5] - a[1]
    return w * h

def score(hcn1, hcn2):
    return overlap_area(hcn1, hcn2)/ min(area(hcn1), area(hcn2))
            

# print(overlap_area(hcn1, hcn2))
# print(area(hcn1))