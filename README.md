# Space Exploration Service

The Space Exploration Service provides backend functionality for querying and processing data related to space exploration missions. It utilizes FastAPI to expose endpoints that interact with the persistence service for data retrieval and manipulation.

## Overview

The Space Exploration Service acts as the backend engine, serving data via HTTP endpoints to the frontend UI. It connects to the Persistence Service for GraphQL-based data operations and management.

## Running Locally

To run the Space Exploration Service locally, you'll need to set it up alongside the Space Exploration Persistence Service and the Space Exploration UI.

### Prerequisites

- Ensure Docker is installed and running on your machine.
- Clone the necessary repositories:

  ```sh
  git clone https://github.com/stevegreghatch/Space-Exploration.git
  ```

### Setup and Installation

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/stevegreghatch/Space-Exploration.git
   cd Space-Exploration
   ```

2. **Build and Run with Docker**:

   ```sh
   docker build -t space-exploration-service:latest .
   docker run -d -p 8000:8000 --name space-exploration-service space-exploration-service:latest
   ```

   This command builds the Docker image and runs the service in a Docker container.

3. **Access the API**:

   Once running, the API endpoints can be accessed locally at `http://localhost:8000`.

## Project Links

- **Persistence Service**: [Space Exploration Persistence Service](https://github.com/stevegreghatch/space-exploration-persistence-service)
- **Frontend UI**: [Space Exploration UI](https://github.com/stevegreghatch/space-exploration-ui)

For more details and updates, visit the [Space Exploration Service repository](https://github.com/stevegreghatch/Space-Exploration).
