# AFAQY
# User Profile Microservice

A RESTful microservice for managing user profiles, including user authentication, CRUD operations, external API integration, concurrency, and state management.

## Features

- **User Profile Management**: Create, read, update, and delete user profiles.
- **Authentication & Authorization**: JWT-based authentication with role-based access control (RBAC).
- **Third-Party API Integration**: Fetch current weather data for user locations from external APIs.
- **Batch Processing**: Analyze user data concurrently to calculate average temperatures.
- **State Machine Implementation**: Manage user states (Active, Inactive, Suspended) with automatic transitions.
- **Logging**: Dual handler logging with rotating file handler.
  
## API Endpoints

### User Management

- **Create User**
  - `POST /users`
  - Request: 
    ```json
    {
      "username": "johndoe",
      "name": "John Doe",
      "email": "johndoe@example.com",
      "phone": "123-456-7890",
      "city": "New York"
    }
    ```
- **Get User**
  - `GET /users/{id}`
- **Update User**
  - `PUT /users/{id}`
  - Request:
    ```json
    {
      "name": "John Doe Updated"
    }
    ```
- **Delete User**
  - `DELETE /users/{id}`

### Authentication

- **Login**
  - `POST /login`
  - Request:
    ```json
    {
      "username": "johndoe",
      "password": "your_password"
    }
    ```
  - Response:
    ```json
    {
      "access_token": "your_access_token",
      "token_type": "bearer"
    }
    ```

## Requirements

- Python 3.8+
- FastAPI
- pymongo
- pydantic
- jwt
- uvicorn

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd user_profile_microservice
