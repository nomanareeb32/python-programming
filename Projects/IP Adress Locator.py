import requests

# Ask the user for an IP address
ip_address = input("Enter an IP address: ")

# Send request to ip-api.com with the given IP
response = requests.get(f'http://ip-api.com/json/{ip_address}')

# Parse the JSON response
data = response.json()

# Check if the lookup was successful
if data['status'] == 'success':
    print("\nResults:")
    print("IP:        ", data['query'])
    print("City:      ", data['city'])
    print("Country:   ", data['country'])
    print("Latitude:  ", data['lat'])
    print("Longitude: ", data['lon'])
else:
    print("Lookup failed:", data['message'])