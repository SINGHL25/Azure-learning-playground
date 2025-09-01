
from src.vnet_manager import create_vnet_demo, create_peering_demo

def test_vnet_and_peering():
    v = create_vnet_demo("testvnet")
    p = create_peering_demo("v1","v2")
    assert "vnet" in v
    assert p["status"] == "peered"
