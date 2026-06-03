# Exercise 51

import hashlib


class URLShortener:

    def __init__(self):
        self.urls = {}

    def shorten(self, url):

        short = hashlib.md5(
            url.encode()
        ).hexdigest()[:6]

        self.urls[short] = url

        return short

    def retrieve(self, short):
        return self.urls.get(
            short,
            "URL Not Found"
        )


shortener = URLShortener()

short_code = shortener.shorten(
    "https://www.google.com"
)

print("Short URL:", short_code)

print(
    "Original URL:",
    shortener.retrieve(short_code)
)

