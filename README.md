
# CSE-2102 Lab 4: HTTP Calls, REST, and Token-Based Authentication

## Overview

This project demonstrates how to build a simple server-client system using HTTP calls, REST principles, and token-based authentication with JWT (JSON Web Token). The system comprises three main components:

1. **Flask Server (`my-server.py`)**: A basic Flask server that provides endpoints for login and echo functionality.
2. **Client (`my-calls.py`)**: A client script using the `httpx` library to make HTTP GET and POST requests to the server.
3. **Token-Based Authentication**: JWT is used for secure communication, ensuring that only authorized users can access certain resources.

## Components

### 1. **Flask Server (`my-server.py`)**

The server is implemented using Flask and provides two main routes:
- **`/login`**: This route handles login requests. When a valid user ID is submitted, the server generates a JWT token and sends it back to the client.
- **`/echo`**: This route requires the client to provide a valid JWT token in the `Authorization` header. The server verifies the token, and if valid, it returns a message echoing back the text sent by the client.

Key functionality:
- Token generation is done via JWT.
- Token validation checks if the provided token is valid and not expired.

### 2. **Client (`my-calls.py`)**

The client uses the `httpx` library to interact with the server. It performs the following actions:
- **Login**: Sends a POST request to the `/login` endpoint to obtain a JWT token.
- **Echo**: Sends a POST request to the `/echo` endpoint, including the JWT token in the `Authorization` header. The server responds by echoing back the text provided in the request.

Key functionality:
- Demonstrates making GET and POST requests.
- Handles sending and receiving JSON data and managing token-based authorization.

### 3. **Token-Based Authentication**

JWT tokens are used for authorization. The login process generates a token, which is then used to access protected routes such as `/echo`. Tokens include a user ID and an expiration time, and they are securely signed using a secret key on the server.

Key functionality:
- Secure communication using tokens.
- Tokens are checked for validity and expiration on every protected request.

## System Diagram

Below is a simple diagram showing how the system works:

```
+---------------------+           +----------------------+
|      Client         |           |       Server          |
+---------------------+           +----------------------+
|                     |           |                      |
| 1. Login Request     +---------> | 2. Generate JWT      |
| (POST /login)        |           | and return token     |
|                     | <---------+                      |
| 3. Receive JWT       |           |                      |
|                     |           |                      |
| 4. Send Echo Request +---------> | 5. Verify Token      |
| (POST /echo)         |           | and return echo      |
| (with token)         | <---------+                      |
+---------------------+           +----------------------+
```

## How to Run the Project

1. **Start the Server**:
   ```bash
   python3 my-server.py
   ```
   
2. **Run the Client**:
   ```bash
   python3 my-calls.py
   ```

The client will:
1. Log in to receive a JWT token.
2. Use the token to make a request to the `/echo` endpoint.

## Conclusion

This project demonstrates the basics of building a RESTful service with token-based authentication using JWT. It can be expanded further with more complex authorization mechanisms and additional features such as token refresh, user roles, and more.
