
from src.vm_manager import create_vm_demo

def test_create_vm_demo():
    res = create_vm_demo("testvm")
    assert res["status"] in ["created"]
