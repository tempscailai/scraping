FROM python:3.11-slim

# Install OS deps required by lxml (used by BeautifulSoup when parsing HTML)
RUN apt-get update && apt-get install -y \
    libxml2 \
    libxml2-dev \
    libxslt1-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first (so Docker can cache pip install)
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY scraper.py /app/scraper.py

# Default execution (Cloud Run Job or Docker run)
CMD ["python", "scraper.py"]
