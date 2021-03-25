# Python requests package
# Connect to live web using python requests api
# Connect to website to check if website is live

import requests


def status_code_check(website):
    response = requests.get(website)    # Website to check goes here
    if response:                        # Status code 200 means working and online
        return "Website is currently online with code: " + str(response.status_code)
    else:                      # 400 or 404 is not working and should be displayed
        return "Error: " + str(response.status_code)


print(status_code_check("https://www.marvel.com/404"))
