# 🧱 FastAPI Clean Architecture Orders
```
Modern and scalable project with **FastAPI + Clean Architecture + DDD**   
modeling an **ordering platform** with PostgreSQL, gRPC for communication between microservices,  
resilience and performance.
```

*Projeto moderno e escalável com **FastAPI + Clean Architecture + DDD**, modelando uma **plataforma de pedidos** com PostgreSQL, gRPC para comunicação entre microsserviços, resiliência e performance.*

---

## 📌 Technologies and Patterns
#### *(Tecnologias e padrões)*
- **FastAPI**
- **Clean Architecture**
- **DDD**
- **SQLAlchemy**
- **Tenacity**
- **gRPC**
- **Docker**

---

## 🚀 Running app locally
#### *(Executando o projeto localmente)*
###
### Prerequisites
#### *(Pré-requisitos)*
- Python 3.11+
- Docker
- Git

### Clone project Github:
#### *(Clonar o projeto github)*
```bash
git clone https://github.com/victorbfcastro/fastapi-clean-architecture-orders.git
cd fastapi-clean-architecture-orders
```

### Initiate PostgreSQL with Docker:
#### *(Inicie o PostgreSQL com Docker)*
```
docker-compose up -d
```

### Install dependencies:
#### *(Instale as dependências)*
```
pip install -r requirements.txt
```

### Run application:
#### *(Execute a aplicação)*
```
uvicorn app.main:app --reload
```

## 📂 Project Structure (Clean Architecture)
#### *(Estrutura do projecto)*
```
app/
├── domain/             
├── application/        
├── infrastructure/     
├── interfaces/         
├── main.py
```

## ✨ Author
#### Victor B. F. Castro — Senior Software Engineer | Node.js, Nestjs, Python & AWS | Clean Architecture
[LinkedIn](https://www.linkedin.com/in/victorbfcastro/) · [GitHub](https://github.com/victorbfcastro)