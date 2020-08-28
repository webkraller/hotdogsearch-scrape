import pandas as pd
import urllib.request
import json
import os
from collections import Counter
from insta_scrape import recent_post_links, insta_link_comments

accounts_to_scrape = [
    {'name': 'what_hot_dog_are_you', 'post_count': 280},
    {'name': 'what_hotdog_are_you', 'post_count': 440}
]
for account in accounts_to_scrape:
    post_urls = recent_post_links(
        account['name'], post_count=account['post_count']
    )
    print(post_urls)
    account_comments = [insta_link_comments(url) for url in post_urls]
    path = os.path.join('scrapes', account['name'] + '.json')
    with open(path, 'w') as json_file:
        json.dump(account_comments, json_file)
