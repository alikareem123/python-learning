links = [
    "www.google.com",
    "www.facebook.com",
    "www.youtube.com",
    "www.yahoo.com",
    "www.bing.com"
]
for link in links:
    print(link.replace("www.", ""))
cleaned_links = map(lambda link: link.replace("www.", ""), links)


print(list(cleaned_links))