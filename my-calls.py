import httpx

url = "http://127.0.0.1:5000/"  # Update this to your server URL

# First, try a GET request to check if the server is running
response = httpx.get(url)
print(response.status_code)
print(response.text)

# Now, let's attempt a login to receive a JWT token
auth_data = {
    "id": "phillip.bradford@uconn.edu"
}

# Send a POST request to login and retrieve the token
login_response = httpx.post(url + "login", data=auth_data)
print("Login response status:", login_response.status_code)

if login_response.status_code == 200:
    token = login_response.json().get('token')
    print(f"Received Token: {token}")
    
    # Perform a POST request to the echo endpoint with the JWT token in the Authorization header
    my_data = {
        "text": "Hello Phil!"
    }
    
    headers = {
        "Authorization": f"Bearer {token}"  # Attach the JWT token here
    }
    
    echo_response = httpx.post(url + "echo", data=my_data, headers=headers)
    print("Echo response status:", echo_response.status_code)
    print("Echo response body:", echo_response.json())

    # Attempt to access the echo endpoint with an invalid token
    invalid_headers = {
        "Authorization": "Bearer invalidtoken123"  # Invalid token
    }
    
    invalid_echo_response = httpx.post(url + "echo", data=my_data, headers=invalid_headers)
    print("Invalid echo response status:", invalid_echo_response.status_code)
    print("Invalid echo response body:", invalid_echo_response.json())

else:
    print("Login failed!")
