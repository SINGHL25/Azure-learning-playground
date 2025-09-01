
from src.storage_manager import create_storage_account_demo, attach_disk_demo

def test_storage_and_disk():
    s = create_storage_account_demo("stor1")
    d = attach_disk_demo("vm-test", 64)
    assert s["status"] == "created"
    assert d["status"] == "attached"
