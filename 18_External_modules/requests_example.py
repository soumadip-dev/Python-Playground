# Using the requests module to fetch data from an API
# This program retrieves user information from the GitHub API
# and stores the response in a text file.

import requests

# Send a GET request to the GitHub API
response = requests.get("https://api.github.com/users/soumadip-dev")

# Write the API response data into a text file
with open("soumadip.txt", "w") as output_file:
    output_file.write(response.text)
