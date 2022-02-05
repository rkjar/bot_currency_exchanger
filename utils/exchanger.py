import re
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}

DOLLAR_RUB = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&rlz=1C1BNSD_ruRU962RU962&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+&aqs=chrome.1.69i57j0i67i131i433j0i131i433i512j0i67l2j0i131i433i512l2j0i512j0i67l2.5704j1j7&sourceid=chrome&ie=UTF-8'
DOLLAR_EURO = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B5%D0%B2%D1%80%D0%BE&newwindow=1&rlz=1C1BNSD_ruRU962RU962&sxsrf=APq-WBtiTouDM1KWxkFbGZVo7Y1oMsW7Yw%3A1643823504020&ei=kMH6YdRj7o-uBNj4jNAG&ved=0ahUKEwjU657gx-H1AhXuh4sKHVg8A2oQ4dUDCA4&uact=5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=Cgdnd3Mtd2l6EAMyDQgAEIAEELEDEEYQggIyCggAEIAEEIcCEBQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoHCAAQsAMQQzoNCAAQgAQQhwIQsQMQFDoHCAAQgAQQCjoICAAQgAQQsQNKBAhBGABKBAhGGABQSVisBmD3B2gBcAJ4AIABhAGIAfkCkgEDMy4xmAEAoAEByAEKwAEB&sclient=gws-wiz'
DOLLAR_BTC = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D1%83&rlz=1C1BNSD_ruRU962RU962&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D0%B1%D0%B8%D1%82%D0%BA&aqs=chrome.0.0i512j69i57j0i512l2j0i22i30l4j0i10i22i30j0i22i30.7308j1j7&sourceid=chrome&ie=UTF-8'
DOLLAR_ETH = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%8D%D1%84%D0%B8%D1%80%D1%83&newwindow=1&rlz=1C1BNSD_ruRU962RU962&sxsrf=APq-WBsW6B7t-s40dp4YZgF6HSKurtljsA%3A1643822003119&ei=s7v6YcDjBpWfrwTC-aW4DA&ved=0ahUKEwiAiceUwuH1AhWVz4sKHcJ8CccQ4dUDCA4&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%8D%D1%84%D0%B8%D1%80%D1%83&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggI6BwgAEEcQsAM6CggAEEcQsAMQyQM6BwgAELADEEM6DQgAEIAEEIcCEMkDEBQ6BQgAEIAEOgoIABCABBCHAhAUOggIABCABBDJAzoHCAAQgAQQCjoHCAAQyQMQCjoECAAQCjoGCAAQFhAeOggIIRAWEB0QHjoECCMQJzoKCAAQsQMQgwEQQzoHCAAQsQMQQzoLCAAQgAQQsQMQgwE6DQgAEIAEEIcCELEDEBQ6BAgAEEM6CggAELEDEIMBEApKBAhBGABKBAhGGABQuwFYlh5gxR9oBXACeACAAcQEiAHwDJIBBzUuNS41LTGYAQCgAQHIAQrAAQE&sclient=gws-wiz'

info = {
    'DOLLAR to RUB': DOLLAR_RUB,
    'DOLLAR to EURO': DOLLAR_EURO,
    'DOLLAR to BTC': DOLLAR_BTC,
    'DOLLAR to ETH': DOLLAR_ETH,
}


def get_amount(currency: str, amount: float = 1) -> float:
    full_page = requests.get(url=info[currency], headers=HEADERS)
    soup = BeautifulSoup(full_page.content, "html.parser")
    convert = soup.find_all("input", {"class": "a61j6", "aria-label": "Поле для ввода суммы в валюте"})
    value = re.split("value=", str(convert[0]))[-1]
    value = float(re.search(r"\d+.*\d+", value).group(0))
    return value * amount
