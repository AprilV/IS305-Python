# Section 2: requests Module - Reference Examples

import requests

# Download a web page
response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
response.raise_for_status()
print(len(response.text))
print(response.text[:100])

# Check status code
response = requests.get('https://nostarch.com')
print(response.status_code)
print(response.status_code == requests.codes.ok)

# Handle errors
response = requests.get('https://inventwithpython.com/nonexistent_page')
try:
    response.raise_for_status()
except Exception as exc:
    print(f'There was a problem: {exc}')

# Save downloaded file
response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
response.raise_for_status()
with open('RomeoAndJuliet.txt', 'wb') as file:
    for chunk in response.iter_content(100000):
        file.write(chunk)
print('File saved successfully')
