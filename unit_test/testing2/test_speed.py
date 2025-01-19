import pytest
from speed import speed_eval

@pytest.fixture
def values_fixture():
    val_list=[-5,221,240,0,20,40,119,120,159,200,210,220]
    ret_list=["Invalid","Invalid","Invalid","Low","Low","Normal","Normal","High","High","V.High","V.High","V.High"]
    vals=dict(zip(val_list,ret_list))
    return vals
def test_speed(values_fixture):
    for value in values_fixture:
        assert speed_eval(value) == values_fixture[value] 
