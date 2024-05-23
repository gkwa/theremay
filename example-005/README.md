# theremay

```bash
incus image info example-005 &>/dev/null && incus image rm example-005; incus info example-005 &>/dev/null && incus rm --force example-005

bash -xe run.sh

rm -rf cloud-init-logs-* cloud-init.tar.gz && incus exec example-005 -- cloud-init collect-logs && incus file pull example-005/root/cloud-init.tar.gz . && tar xzf cloud-init.tar.gz && rg curl cloud-init-logs-*

```

Links
- https://github.com/lxc/terraform-provider-incus/blob/main/docs/resources/instance.md#basic-example
- https://github.com/lxc/terraform-provider-incus?tab=readme-ov-file#terraform-provider-incus
- https://github.com/lxc/terraform-provider-incus/tree/main/docs/resources
