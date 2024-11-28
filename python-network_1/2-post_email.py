#!/usr/bin/python3
"""
A script that sends a POST request to a given URL with an email parameter
and displays the body of the response decoded in utf-8.
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    # Extract URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create the data payload
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send the POST request
    with urllib.request.urlopen(url, data) as response:
        # Read and decode the response
        response_body = response.read().decode('utf-8')
        print(response_body)
