

### `docs/vm_basics.md`
<img width="2048" height="2048" alt="Gemini_Generated_Image_tifqa3tifqa3tifq (9)" src="https://github.com/user-attachments/assets/626d8b93-5851-411d-b761-715c4c1fe4af" />

```markdown
# VM Basics (Linux & Windows)

- VM sizes, OS images, SSH keys for Linux, RDP for Windows
- Attach managed disks: OS disk + data disks
- Availability Zones vs Availability Sets

Example CLI:
```bash
az vm create -g MyRG -n myVM --image UbuntuLTS --admin-username azureuser --ssh-key-value ~/.ssh/id_rsa.pub
