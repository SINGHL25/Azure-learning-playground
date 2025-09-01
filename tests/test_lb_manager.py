
from src.lb_manager import create_loadbalancer_demo

def test_lb():
    r = create_loadbalancer_demo("lb1")
    assert r["status"] == "active"
