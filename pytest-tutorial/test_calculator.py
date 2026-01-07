import pytest
from calculator import add, divide

def test_add():
    assert add(1,2) == 3 #assert : 양변이 일치할때는 반환하고 그렇지 않으면 에러 반환
    assert add(-1,1) == 0

def test_divide():
    assert divide(10,2) == 5

#예외 발생 확인
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10,0)