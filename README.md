# 🚀 Zero-Touch Deployment Architecture

A fully containerized, multi-tier microservice web application demonstrating modern DevOps CI/CD practices, reverse proxy routing, and secure Linux system administration.

## 🏗️ Architecture Overview

This project simulates a production-grade infrastructure environment. Traffic is securely routed through a reverse proxy, handled by a containerized Python backend, and state is maintained in an in-memory Redis cache. Deployments are fully automated via GitHub Actions.


🛠️ **Tech Stack & Skills Demonstrated**

   Infrastructure Automation: Bash, Systemd, Cron

   Containerization: Docker, Docker Compose, Alpine Linux

   CI/CD: GitHub Actions (Self-Hosted Runner)

   Networking & Security: Nginx, Firewalld, SELinux, SSH (ed25519)

   Backend & State: Python 3.12, Redis



```mermaid
graph TD;
    Client([🌍 Public Internet]) -->|HTTPS| Cloudflare[(Cloudflare Zero Trust Tunnel)];
    Cloudflare -->|Port 80| Nginx[Nginx Reverse Proxy];
    
    subgraph "Docker Compose Isolated Network"
        Nginx -->|Proxy Pass :8000| WebApp[Python Web App];
        WebApp -->|Internal DNS :6379| Redis[(Redis Cache)];
    end
