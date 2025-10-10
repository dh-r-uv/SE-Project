# Scientific Calculator with a DevOps CI/CD Pipeline

This project is a command-line scientific calculator built in Python, integrated with a full DevOps toolchain for continuous integration, testing, and deployment. The entire process, from code commit to application deployment, is automated using Jenkins, Docker, and Ansible.

This was developed as a mini-project for the **CS 816 - Software Production Engineering** course.

---

## ✨ Features

The calculator provides a user menu to perform the following scientific operations
* **Square Root Function** - $\sqrt{x}$ 
* **Factorial Function** - $x!$ 
* **Natural Logarithm** - $\ln(x)$ (base e) 
* **Power Function** - $x^b$ 



---

## 🔄 DevOps Pipeline Overview

The project implements a complete CI/CD pipeline that automates the build, test, and deployment lifecycle. The workflow is as follows:

**Code Push (GitHub) → Jenkins Trigger → Run Unit Tests → Build Docker Image → Push to Docker Hub → Deploy with Ansible -> Post Actions**
#### Trigger:

Automatically runs on every GitHub push (githubPush() trigger, configured via webhook)

This pipeline ensures that every code change is automatically tested and deployed, promoting reliability and speed.

---

## 🛠️ Technology Stack

* **🐍 Language:** Python
* **🧪 Testing:** PyUnit (unittest) 
* **📦 Containerization:** Docker 
* **🔄 CI/CD Automation:** Jenkins 
* **⚙️ Configuration & Deployment:** Ansible 
* **☁️ Image Registry:** Docker Hub 
* **📚 Source Control:** Git & GitHub 
* **Local Jenkins instance** ngrok 
---
## Project Structure
```
SE-Project/
├── __pycache__/
├── calculator.py
├── deploy.yml
├── Dockerfile
├── inventory.ini
├── Jenkinsfile
├── README.md
└── test_calculator.py
```
### File Descriptions

| File                 | Description                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| `calculator.py`      | The main Python application code for the scientific calculator.             |
| `test_calculator.py` | Unit tests for the calculator functions using PyUnit.                    |
| `Dockerfile`         | Instructions to build the application into a portable Docker image.       |
| `Jenkinsfile`        | The declarative pipeline script that automates the entire CI/CD workflow.   |
| `deploy.yml`         | The Ansible playbook responsible for deploying the Docker container.        |
| `inventory.ini`      | The Ansible inventory file, defining the hosts for deployment.              |
| `README.md`          | This documentation file, explaining the project and how to use it.          |


---

## 📋 Prerequisites

Before you begin, ensure you have the following installed on your local machine (or WSL environment):
* Git
* Docker and Docker Desktop
* Jenkins (with 17 or 21)
* Ansible

**Required Jenkins Plugins:**
* Docker Pipeline
* Ansible

---

## 🚀 Setup and Installation

Follow these steps to configure and run the pipeline.

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/dh-r-uv/SE-Project
cd SE-Project
```
### 2. To run code locally
```bash
python3 calculator.py
```
```bash
Calculator Menu
1. Square Root (√x)
2. Factorial (!x)
3. Logorithm (ln(x))
4. Power (x^b)
5. Exit

Enter your option (1-5):
```
### 3. Test it on unittests
```bash
python3 -m unittest test_calculator.py
```
### 4. Run the container hosted on Docker hub
```bash
docker build -t dhruvk321/sci-calc
docker run -it dhruvk321/sci-calc
```
### Deploy using Ansible
- Connects to the target, pulls latest docker image and runs the container on the host, locally.
```bash
ansible-playbook -i inventory.ini deploy.yml
```
Now one can access the container by attaching to running container.
```bash
docker attach sci-calc
```

