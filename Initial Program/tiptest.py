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


def test_one():
    score = [10,10,10,10,10,10,10,10,10,10]
    assert caltips(score) == 35

def test_two():
    score = [10,5,10,5,10,10,5,10,10,10]
    assert caltips(score) == 20

def test_three():
    score = [5, 5, 5, 10, 5, 5, 10, 5, 6, 7]
    assert caltips(score) == 15

def test_four():
    score = [5, 5, 5, 5, 5, 5, 5, 0, 0, 0]
    assert caltips(score) == 5

def test_five():
    score = [10, 10, 10, 5, 5, 10, 10, 10, 10, 10]
    assert caltips(score) == 30