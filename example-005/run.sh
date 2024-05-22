#!/usr/bin/env bash


if ! incus image info example-005 &>/dev/null; then
    packer init .
    packer build ubuntu.pkr.hcl
fi

terraform init
terraform plan -out=tfplan
terraform apply tfplan
incus ls example-005
incus exec example-005 -- curl --version

