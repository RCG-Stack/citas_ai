# Imagen base de Python
FROM python:3.11-slim

# Configurar directorio de trabajo
WORKDIR /app

# Evitar buffers en logs
ENV PYTHONUNBUFFERED=1

# Copiar requerimientos e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Exponer el puerto donde correrá FastAPI
EXPOSE 8000

# Comando de arranque
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

