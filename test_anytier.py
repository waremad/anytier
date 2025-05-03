from anytier import *

def test_make_outdict():
    assert make_outdict({}) == {}
    assert make_outdict({"A":[],"B":["A","D"],"C":["A"],"D":["C"]}) == {"A":0,"B":0,"C":0,"D":0}

def test_txt_dict():
    assert txt_dict("test.txt") == {"A":[],"B":["A","D"],"C":["A"],"D":["C"]}
    assert txt_dict("test2.txt") == {"A":["A","A"],"B":["A","B"],"C":["A","C"],"D":[]}

def test_dicmin():
    assert dicmin({"A":1}) == 1
    assert dicmin({"A":1,"B":0}) == 0

