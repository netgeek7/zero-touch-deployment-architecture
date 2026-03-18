# Zero-Touch Cloud Deployment Architecture

![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)

## Overview
This repository contains a fully automated, Infrastructure-as-Code (IaC) deployment of a containerized Python web application. It demonstrates modern DevOps practices, moving from code push to a live production environment on AWS without any manual server intervention ("Zero-Touch").

## System Architecture

```mermaid
flowchart LR
  Dev([Developer]) -- Git Push --> GH[GitHub Repository]
  GH -- Triggers --> GHA[GitHub Actions CI/CD]
  GHA -- SSH & Docker Compose --> AWS

  subgraph AWS [AWS Cloud Environment]
    subgraph VPC [Custom VPC: 10.0.0.0/16]
      IGW[Internet Gateway]
      subgraph PubSub [Public Subnet: 10.0.1.0/24]
        EC2[Ubuntu EC2 + Elastic IP]
        subgraph Docker [Docker Engine]
          Nginx[Nginx Container :80]
          App[Python App Container :8000]
          Redis[Redis Container :6379]
          Nginx -->|Proxy Pass| App
          App -->|Cache| Redis
        end
      end
      IGW --- PubSub
    end
  end
  Internet((Internet)) -->|HTTP: 80| IGW
```
# 🛠 Core Competencies & Technologies Demonstrated
1. **Infrastructure as Code (Terraform)**

    Custom VPC Networking: Abandoned the default AWS network to architect a custom VPC with dedicated public subnets, internet gateways, and custom route tables.

    Zero-Trust Security: Configured strict Security Groups acting as virtual firewalls to restrict ingress traffic to only required ports (HTTP 80, SSH 22).

    Automated Bootstrapping: Utilized user_data to inject bash scripts (setup.sh) during the EC2 boot sequence, ensuring the host is provisioned with Docker and Git before the first login.

    State Management: Handled infrastructure drift, immutable server replacements, and Elastic IP (Static Anchor) associations.

2. **Continuous Integration & Deployment (GitHub Actions)**

    Automated Workflows: Engineered a YAML-based CI/CD pipeline that triggers on git push to the main branch.

    Race Condition Mitigation: Implemented cloud-init status --wait to ensure the AWS bootstrapping phase completes before the deployment runner attempts to execute code.

    Secret Management: Utilized GitHub Secrets to securely pass SSH keys and host IPs to the runner, keeping credentials out of version control.

3. **Container Orchestration & Networking (Docker)**

    Multi-Container Environments: Managed a multi-service architecture (Web, Cache, Proxy) using docker-compose.yml.

    Reverse Proxying: Containerized Nginx instead of relying on host-OS installations, achieving true environment parity and protecting the Python application server from Slowloris attacks and direct internet exposure.

    Internal Docker Networking: Leveraged Docker's internal DNS to allow containers to communicate securely via service names rather than hardcoded IPs.

# 🚀 Deployment Instructions

  1. Provision Infrastructure Navigate to the terraform/ directory, update the variables, and run:
    Bash
```
    terraform init
    terraform plan
    terraform apply
```
  2. Update Secrets Copy the outputted Elastic IP into your GitHub Repository Secrets as EC2_HOST.

  3. Deploy Push changes to the main branch. GitHub Actions will handle the SSH connection, code pull, and container orchestration automatically.
