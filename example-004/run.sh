#!/usr/bin/env bash

terraform init
terraform plan -out=tfplan
terraform apply tfplan
