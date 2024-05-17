FROM python:3.19.1-alpine

# For local debugging...only enabled in local sandbox testing
# Standard service endpoints
EXPOSE 8000 8080 5000

WORKDIR /opt

COPY requirements.txt app.py /opt
COPY src/ /opt/src/

USER root

# Create log file and set permissions
RUN touch /var/log/app.log && chmod 777 /var/log/app.log

# Install dependencies
RUN apk --no-cache update && \
    apk --no-cache add gcompat wget gcc build-base zlib zlib-dev librdkafka librdkafka-dev && \
    pip3.12 install --upgrade pip && \
    pip3.12 install -r /opt/requirements.txt && \
    pip3.12 cache purge && \
    apk del gcc build-base librdkafka-dev && \
    find / -name 'pip-*' -exec rm -rf '{}' + && \
    find / -name 'pip-*.whl' -exec rm -rf '{}' +

# Ensure /opt and /var/log are writable
RUN chmod -R 777 /opt && chmod -R 777 /var/log

# Remove pip due to vulnerability
RUN apk del gcc build-base librdkafka-dev

# Set user back to non-root user to run the container
RUN adduser -S -u 1000 -g runuser runuser
USER runuser

WORKDIR /opt

CMD ["python3.12", "app.py"]
