# Gunakan gambar python resmiversi slim (ringan)
FROM python:3.9-slim

# Setel working directory
WORKDIR /app

# Copy semua file project ke container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port flask
EXPOSE 5000

# Command untuk menjalankan app
CMD ["python", "app.py"]