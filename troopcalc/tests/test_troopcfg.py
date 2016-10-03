
import pytest
from troopcalc.troopcfg import TroopCfg

def test_properties():
    """Test property accessors"""
    cost = {"1": 50, "2": 80}
    archer = TroopCfg("archer","elixir",25,1,cost)
    assert archer.name == "archer"
    assert archer.type == "elixir"
    assert archer.buildTime == 25
    assert archer.space == 1
    assert archer.cost == cost
    with pytest.raises(AttributeError):
      archer.name = "junk"
    with pytest.raises(AttributeError):
      archer.type = "junk"
    with pytest.raises(AttributeError):
      archer.buildTime = "junk"
    with pytest.raises(AttributeError):
      archer.space = "junk"
    with pytest.raises(AttributeError):
      archer.cost = cost

