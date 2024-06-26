import re
import json

patterns = [

    "file=",
    "document=",
    "folder=",
    "root=",
    "path=",
    "pg=",
    "style=",
    "pdf=",
    "template=",
    "php_path=",
    "doc=",
    "page=",
    "name=",
    "cat=",
    "dir=",
    "action=",
    "board=",
    "date=",
    "detail=",
    "download=",
    "prefix=",
    "include=",
    "inc=",
    "locate=",
    "show=",
    "site=",
    "type=",
    "view=",
    "content=",
    "layout=",
    "mod=",
    "conf=",
    "url="

]
def apply_filter(fil_urls, red_out):
    with open(fil_urls, 'r') as file:
        urls = file.readlines()

    with open(red_out, 'w') as file:
        for url in urls:
            if any(pattern in url for pattern in patterns):
                modified_url = re.sub(r'=\S*', '=', url)
                file.write(modified_url)


