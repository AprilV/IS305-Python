# Section 2: requests Module - Practice

# Q1: First install requests by running this in terminal: python -m pip install requests
# Then import requests module
# WHAT IT DOES: requests module downloads files and web pages from the internet
import requests



# Q2: Create variable named res and use requests.get() to download 'https://automatetheboringstuff.com/files/rj.txt', then call raise_for_status() on res
# WHAT IT DOES: requests.get() downloads content from a URL; raise_for_status() ensures download succeeded
# ┌─ EXAMPLE ─────────────
# │ import requests
# │ response = requests.get('https://nostarch.com')
# │ response.raise_for_status()
# └───────────────────────
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()



# Q3: Print res.status_code and check if it equals requests.codes.ok
# WHAT IT DOES: status_code attribute shows HTTP status (200 = OK); requests.codes.ok is constant for success
# ┌─ EXAMPLE ─────────────
# │ print(response.status_code)
# │ print(response.status_code == requests.codes.ok)
# └───────────────────────
print(res.status_code)
print(res.status_code == requests.codes.ok)



# Q4: Use len() to print the length of res.text, then print the first 200 characters using slicing
# WHAT IT DOES: text attribute contains downloaded content as string; len() shows total size
# ┌─ EXAMPLE ─────────────
# │ print(len(response.text))
# │ print(response.text[:150])
# └───────────────────────
print(len(res.text))
print(res.text[:200])



# Q5: Use requests.get() to download 'https://nostarch.com', store in variable named page, then use try/except to call raise_for_status() and print any exceptions
# WHAT IT DOES: try/except blocks catch errors without crashing the program
# ┌─ EXAMPLE ─────────────
# │ result = requests.get('https://example.com/missing')
# │ try:
# │     result.raise_for_status()
# │ except Exception as exc:
# │     print(f'Error: {exc}')
# └───────────────────────
page = requests.get('https://nostarch.com')
try:
    page.raise_for_status()
except Exception as exc:
    print(f'error: {exc}')



# Q6: Download 'https://automatetheboringstuff.com/files/rj.txt' and save to 'downloaded.txt' using with open in 'wb' mode, iter_content() with 100000 bytes, and write()
# WHAT IT DOES: 'wb' mode writes binary data; iter_content() loops through chunks; write() saves to disk
# ┌─ EXAMPLE ─────────────
# │ data = requests.get('https://example.com/file.txt')
# │ data.raise_for_status()
# │ with open('saved.txt', 'wb') as f:
# │     for chunk in data.iter_content(100000):
# │         f.write(chunk)
# └───────────────────────
data = requests.get('https://automatetheboringstuff.com/files/rj.txt')
data.raise_for_status()
with open('downloaded.txt', 'wb') as f:
    for chunk in data.iter_content(100000):
          f.write(chunk)


