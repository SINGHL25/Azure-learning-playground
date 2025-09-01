
from src.security_manager import create_nsg_rule_demo

def test_nsg_rule():
    r = create_nsg_rule_demo("nsg1","AllowSSH",22)
    assert r["port"] == 22
