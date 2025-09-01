

### `docs/vm_basics.md`
```markdown
# VM Basics (Linux & Windows)

- VM sizes, OS images, SSH keys for Linux, RDP for Windows
- Attach managed disks: OS disk + data disks
- Availability Zones vs Availability Sets

Example CLI:
```bash
az vm create -g MyRG -n myVM --image UbuntuLTS --admin-username azureuser --ssh-key-value ~/.ssh/id_rsa.pub
