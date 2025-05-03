#
"""
A---A----A
B-|   |
C---C-|
D-|

B-|
D---D

"""
ls = {"A":[],"B":["A","D"],"C":["A"],"D":["C"]}

def make_outdict(dic):
    out = {}
    for i in list(dic.keys()):
        