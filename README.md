# 📚 Biblioteca API

API REST para gerenciamento de livros e usuários, desenvolvida com Django, Django REST Framework, PostgreSQL e Docker.

---

## 🚀 Tecnologias

- Python 3.12
- Django 6
- Django REST Framework
- PostgreSQL 16
- Docker
- Docker Compose

---

## 📦 Como executar o projeto

### 1. Clonar o repositório

git clone https://github.com/ArthurLacerdaa/biblioteca-api.git
cd biblioteca-api

---

### 2. Criar arquivo .env

SECRET_KEY=django-secret-key
DEBUG=True

DB_NAME=biblioteca
DB_USER=admin
DB_PASSWORD=admin
DB_HOST=db
DB_PORT=5432

---

### 3. Subir o projeto

docker compose up --build

---

### 4. Rodar migrações

docker compose exec web python manage.py migrate

---

### 5. Criar superusuário (opcional)

docker compose exec web python manage.py createsuperuser

---

## 🌐 Acesso

API: http://localhost:8000/
Admin: http://localhost:8000/admin/

---

## 📌 Endpoints

### Usuários (/usuarios/)

GET    /usuarios/
POST   /usuarios/
GET    /usuarios/{id}/
PUT    /usuarios/{id}/
DELETE /usuarios/{id}/

Exemplo POST:

{
  "nome": "Arthur",
  "email": "arthur@email.com",
  "ativo": true
}

---

### Livros (/livros/)

GET    /livros/
POST   /livros/
GET    /livros/{id}/
PUT    /livros/{id}/
DELETE /livros/{id}/

Exemplo POST:

{
  "titulo": "Dom Casmurro",
  "autor": "Machado de Assis",
  "categoria": "Romance",
  "ano_publicacao": 1899,
  "disponivel": true
}

---

## 🐳 Docker Hub

docker pull arthurlacerd/biblioteca-api:1.0

docker run -p 8000:8000 \
  -e DB_NAME=biblioteca \
  -e DB_USER=admin \
  -e DB_PASSWORD=admin \
  -e DB_HOST=db \
  -e DB_PORT=5432 \
  arthurlacerd/biblioteca-api:1.0

---

## 👨‍💻 Autor

Arthur Lacerda  
GitHub: https://github.com/ArthurLacerdaa