# Space-Exploration Service

The Space-Exploration Service provides backend functionality for querying and processing data related to space exploration missions. It utilizes FastAPI to expose endpoints that interact with the persistence service for data retrieval and manipulation.

## Overview

The Space-Exploration Service acts as the backend engine, serving data via HTTP endpoints to the frontend UI. It connects to the Persistence Service for GraphQL-based data operations and management.

## Running Locally

To run the Space-Exploration Service locally, you'll need to set it up alongside the Space-Exploration Persistence Service and the Space-Exploration UI.

### Prerequisites

- Python 3.7 or higher installed.
- Clone the necessary repositories:

  ```sh
  git clone https://github.com/stevegreghatch/Space-Exploration.git
  git clone https://github.com/stevegreghatch/space-exploration-ui.git
  ```

### Setup and Installation

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/stevegreghatch/Space-Exploration.git
   cd Space-Exploration
   ```

2. **Install Dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Data Service**:

   ```sh
   uvicorn main:app --reload
   ```

   This command starts the FastAPI application with automatic reloads on code changes.

4. **Access the API**:

   Once running, the API endpoints can be accessed locally at `http://localhost:8000`.

## Project Links

- **Persistence Service**: [Space-Exploration Persistence Service](https://github.com/stevegreghatch/space-exploration-persistence-service)
- **Frontend UI**: [Space-Exploration UI](https://github.com/stevegreghatch/space-exploration-ui)

For more details and updates, visit the [Space-Exploration Service repository](https://github.com/stevegreghatch/Space-Exploration).
