# This script was made by Marl0nX.
import re
import requests


def extract_proxies(urls: list):
    LIST = []
    for _ in urls:
        r = requests.get(_)
        t = r.content.decode('utf-8')
        locProxies = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,5}\b", t)
        for _ in locProxies:
            LIST.append(_)
    return LIST
