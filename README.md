# User Service 🧑‍💻

This project is a **User Microservice** built with **Python**, **FastAPI**, and **Docker**.  
It is part of a larger **microservices architecture** for a future e-commerce platform.

---

## ⚡ Technologies Used

- **[Python 3.12](https://www.python.org/)** → main programming language
- **[FastAPI](https://fastapi.tiangolo.com/)** → web framework for building APIs
- **[Uvicorn](https://www.uvicorn.org/)** → ASGI server to run the FastAPI app
- **[Docker](https://www.docker.com/)** → containerization of the application
- **[Docker Compose](https://docs.docker.com/compose/)** → orchestration of containers

---

## 🚀 How to Run the Project

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   cd user-service
   ```

2. **Start the containers**

```bash
docker compose up --build
```

3. ## 🔗 Access the API

- **Root endpoint**: [http://localhost:8000](http://localhost:8000) → returns
  ```json
  { "message": "Hello World" }
  ```
