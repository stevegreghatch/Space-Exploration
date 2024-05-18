# Build stage
FROM python:3.12.3-alpine3.19

# Set working directory
WORKDIR /opt

# Copy application files
COPY requirements.txt app.py /opt/
COPY src/ /opt/src/

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r /opt/requirements.txt && \
    pip cache purge

# Set up user and directory permissions
RUN adduser -S -u 1000 -g runuser runuser && \
    mkdir -p /var/log && \
    touch /var/log/app.log && \
    chmod -R 777 /var/log

# Switch to non-root user
USER runuser

# Expose ports and set command
EXPOSE 8000 8080 5000
CMD ["python3.12", "app.py"]
