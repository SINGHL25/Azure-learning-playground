

### `docs/storage.md`
```markdown
# Azure Storage

- Storage accounts: Blob, File, Queue, Table
- Managed disks and attaching data disks to VMs
- Example: upload blob via az cli:
```bash
az storage blob upload --account-name mystorage --container-name mycontainer --name file.txt --file ./file.txt
