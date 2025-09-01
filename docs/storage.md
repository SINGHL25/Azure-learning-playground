

### `docs/storage.md`
<img width="2048" height="2048" alt="Gemini_Generated_Image_tifqa3tifqa3tifq (8)" src="https://github.com/user-attachments/assets/c25f8b41-4cdc-4adb-a68e-da9ec2a5e877" />

```markdown
# Azure Storage

- Storage accounts: Blob, File, Queue, Table
- Managed disks and attaching data disks to VMs
- Example: upload blob via az cli:
```bash
az storage blob upload --account-name mystorage --container-name mycontainer --name file.txt --file ./file.txt
