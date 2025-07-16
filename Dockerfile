
# Use an official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy script and requirements
COPY log_analysis.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["python", "log_analysis.py"]
