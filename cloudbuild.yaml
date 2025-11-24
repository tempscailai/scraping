FROM python:3.11-slim

# Install OS build deps for lxml + bs4
RUN apt-get update && apt-get install -y \
    libxml2-dev \
    libxslt1-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY scraper.py .

# Cloud Run uses PORT env var automatically
CMD ["python", "scraper.py"]
