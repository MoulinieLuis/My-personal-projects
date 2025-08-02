import requests  # Import the requests module to make HTTP calls

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke" #The URL of the API endpoint
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        joke = response.json()  # Convert the JSON response to a Python dictionary
        print("Here's a random joke for you:")
        print(joke["setup"])
        print(joke["punchline"])
    else:
        print("Failed to retrieve a joke. Status code:", response.status_code)

# Call the function
get_joke()
