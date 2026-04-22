# 🚀 project_DevOps

> A fully automated DevOps pipeline — from code to cloud, one push at a time.

---

## 🏗️ Architecture Overview

```
Developer
    │
    ▼
  GitHub ──► GitHub Actions (CI/CD)
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
    Terraform            Docker Build
   (AWS EC2 x2)        (Docker Hub Push)
          │                   │
          └─────────┬─────────┘
                    ▼
                 Ansible
              (Deploy App)
                    │
                    ▼
            Kubernetes (k8s)
          (Orchestration & Scaling)
                    │
                    ▼
         Prometheus + Grafana
              (Monitoring)
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Terraform** | Infrastructure as Code — provisions AWS EC2 instances |
| **Docker** | Containerizes the Flask application |
| **Ansible** | Automates deployment across all servers |
| **Kubernetes** | Orchestrates containers with auto-healing & scaling |
| **GitHub Actions** | CI/CD pipeline triggered on every push |
| **Prometheus** | Collects server metrics |
| **Grafana** | Visualizes metrics on beautiful dashboards |
| **AWS EC2** | Cloud infrastructure (2 nodes) |
| **Flask (Python)** | Web application server |

---

## 📁 Project Structure

```
project_DevOps/
├── .github/
│   └── workflows/
│       └── full.yml          # CI/CD pipeline
├── app.py                    # Flask web application
├── Dockerfile                # Container definition
├── main.tf                   # Terraform — AWS infrastructure
├── inventory.tpl             # Ansible inventory template
├── install_app.yml           # Ansible playbook
├── deployment.yml            # Kubernetes Deployment + Service
├── setup.sh                  # Setup script
├── .gitignore
└── .dockerignore
```

---

## 🔄 CI/CD Pipeline

Every `git push` to `main` triggers the following automatically:

1. **Validate** — Terraform validates infrastructure code
2. **Build** — Docker builds and pushes image to Docker Hub
3. **Deploy** — SSH into AWS servers, pull latest image, restart container

---

## 🚢 Quick Start

### Prerequisites
- AWS account with EC2 access
- Terraform installed
- Ansible installed
- Docker + Docker Hub account

### 1. Provision Infrastructure
```
terraform init
terraform apply -auto-approve
```

### 2. Deploy Application
```
ssh-keyscan -H server_ID created by terraform >> ~/.ssh/known_hosts
ssh-keyscan -H server_ID created by terraform >> ~/.ssh/known_hosts

ansible-playbook -i inventory.ini install_app.yml
```

### 3. Access the App
```
http://<your-ec2-ip>:5000
```

---

## ☸️ Kubernetes

Deploy with Kubernetes for auto-healing and load balancing:

```bash
minikube start --driver=docker
kubectl apply -f deployment.yml
kubectl get pods
```

Scale up instantly:
```bash
kubectl scale deployment devops-app --replicas=5
```

---

## 🔐 Security

- SSH keys managed via AWS Key Pairs
- Sensitive files excluded via `.gitignore` and `.dockerignore`
- Security groups restrict access to ports: `22`, `80`, `5000`, `3000`

---

## 📌 GitHub Actions Secrets Required

| Secret | Description |
|--------|-------------|
| `HOST` | EC2 public IP |
| `USERNAME` | SSH username (ubuntu) |
| `SSH_KEY` | Private key for SSH access |

---
