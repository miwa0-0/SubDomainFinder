import requests
from colorama import Fore
import itertools

print("Enter the target domain: ",end="")
domain=input()
with open("serviceswordlists.txt", "r") as file:
    subdomains = file.read().splitlines()

with open("validproxies.txt","r") as f:
    proxies=f.read().splitlines()

proxy_cycle = itertools.cycle(proxies)
count=0

for subdomain in subdomains:
    url1=f"http://{subdomain}.{domain}"
    url2=f"https://{subdomain}.{domain}"

    for url in (url1,url2):
        proxy=next(proxy_cycle)
        try:
            response = requests.get(url, timeout=3,proxies={"http":proxy})
        except requests.exceptions.RequestException:
            print(Fore.RED+f"Couldnt find {url}")
        else:
            if response.status_code in (200, 301, 302, 401, 403):
                print(Fore.GREEN+"[+]", end=f" Found url: {url}\n")
            count+=1
        