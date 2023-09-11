document.getElementById('loginForm').addEventListener('submit', function (e) {
    e.preventDefault();

    // You would normally make an API request here to authenticate the user.
    // User credentials
const email = 'gayathri.bs@hgshealthcare.com';
const password = '12345678';

// API endpoint for login
const loginEndpoint = 'http://ec2-18-218-33-23.us-east-2.compute.amazonaws.com:9001/login';

// Data to send in the request body
const data = {
    email,
    password,
};

// Fetch options for the POST request
const requestOptions = {
    method: 'POST',
    headers: { 
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
};

// Make the API request
fetch(loginEndpoint, requestOptions)
    .then(response => {
        if (!response.ok) {
            throw new Error('Authentication failed');
        }
        return response.json();
    })
    .then(data => {
        // Assuming the API response contains a 'token' field
        const { token } = data;

        // Store the token securely, e.g., in localStorage
        localStorage.setItem('jwtToken', token);

        // Redirect to the dashboard or perform other actions as needed
        window.location.href = 'dashboard.html';
    })
    .catch(error => {
        console.error(error);
        // Handle authentication failure, display an error message, etc.
    });
});
