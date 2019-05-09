import pytest

def caltips(score):
    overall = sum(score)
    scale = overall / 100
    bill = 100 #default set as 100, easier to calculate
    TipPercent = 0
    if scale >= 0.95:
        TipPercent = 0.35
    elif scale >= 0.9 and scale < 0.95:
        TipPercent = 0.3
    elif scale >= 0.75 and scale < 0.89:
        TipPercent = 0.2
    elif scale >= 0.6 and scale < 0.75:
        TipPercent = 0.15
    else:
        TipPercent = 0.05

    Tips = bill * TipPercent
    return Tips


def test_95():
    score = [10,10,10,10,10,10,10,10,10,10]
    assert caltips(score) == 35

def test_75():
    score = [10,5,10,5,10,10,5,10,10,10]
    assert caltips(score) == 20

def test_60():
    score = [5, 5, 5, 10, 5, 5, 10, 5, 6, 7]
    assert caltips(score) == 15

def test_30():
    score = [5, 5, 5, 5, 5, 5, 5, 0, 0, 0]
    assert caltips(score) == 5

def test_90():
    score = [10, 10, 10, 5, 5, 10, 10, 10, 10, 10]
    assert caltips(score) == 30

def test_score_inlist():
    L = ['Tim',10,10,10,10,10,10,10,10,10,10,100,30,130]
    sum = 0
    for i in range(1,11):
        sum += L[i]
    assert sum == L[-3]

def test_totalamount():
    L = ['Tim',10,10,10,10,10,10,10,10,10,10,100,30,130]
    sum = 0
    for i in range(1,11):
        sum += L[i]
    sum += L [-2]
    assert sum == L[-1]

# @pytest.mark.xfail
def test_correctname():
    L = ['Tim', 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 100, 30, 130]

    for i in range(len(L[0])):
        assert L[0][i].isalpha() == True


@pytest.mark.xfail
def test_incorrectname():
    L = ['Tim#', 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 100, 30, 130]

    for i in range(len(L[0])):

        assert L[0][i].isalpha() == True