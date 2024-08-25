import requests


def generateProxies():
    # URL of the proxy list API
    url = "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=ipport&format=text"
    response = requests.get(url)

    if response.status_code == 200:
        proxies = response.text.strip().split("\n")
        with open("proxies.txt", "w") as file:
            for proxy in proxies:
                file.write(f"{proxy}")
        print("Proxies scraped and saved to proxies.txt")
    else:
        print(f"""Failed to retrieve proxies. Status code: {
              response.status_code}""")
