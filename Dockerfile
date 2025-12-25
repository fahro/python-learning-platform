# Multi-stage build for full-stack deployment
FROM node:18-slim AS frontend-build

WORKDIR /frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Backend with frontend static files
FROM python:3.11-slim

WORKDIR /app

# Install nginx for serving frontend
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# Copy backend
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

# Copy built frontend to nginx
COPY --from=frontend-build /frontend/dist /var/www/html

# Nginx config for SPA + API proxy
RUN echo 'server { \n\
    listen 80; \n\
    root /var/www/html; \n\
    index index.html; \n\
    \n\
    location /api { \n\
        proxy_pass http://127.0.0.1:8000; \n\
        proxy_set_header Host $host; \n\
        proxy_set_header X-Real-IP $remote_addr; \n\
    } \n\
    \n\
    location /docs { \n\
        proxy_pass http://127.0.0.1:8000; \n\
    } \n\
    \n\
    location /openapi.json { \n\
        proxy_pass http://127.0.0.1:8000; \n\
    } \n\
    \n\
    location /health { \n\
        proxy_pass http://127.0.0.1:8000; \n\
    } \n\
    \n\
    location / { \n\
        try_files $uri $uri/ /index.html; \n\
    } \n\
}' > /etc/nginx/sites-available/default

# Seed database
RUN python -c "from app.seed_data import seed_database; seed_database()"

# Start script
RUN echo '#!/bin/bash\n\
sed -i "s/listen 80/listen $PORT/" /etc/nginx/sites-available/default\n\
nginx\n\
uvicorn app.main:app --host 127.0.0.1 --port 8000' > /start.sh && chmod +x /start.sh

EXPOSE 80

CMD ["/start.sh"]
