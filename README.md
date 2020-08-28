### What Hot Dog You Are Scrape

I was sent a link to an instagram site where I could find what hotdog I was. But on Instagram you cannot search by plaintext comments! Was I really expected to scroll through the entire published body of work to find what hotdog I was?

Instead of wasting my time, I pieced together a simple Instagram post indexer with Python and Selenium, then dumped the resulting json data into a [searchable site](https://search.hotdog.fan/).
The instagram scrape functionality is built on top of the work done by https://github.com/jnawjux/web_scraping_corgis.

### Quick Start

1. Installation: Clone this repo and cd into it. Make sure geckodriver the Firefox Selenium Driver is executable in project path.
1. Edit the scrape.py file with your desired account names and post counts.
1. Run `python scrape.py` to run the scraper(s).
1. After getting the JSON data you can import into whatever search you want!

JSON format = {"link": "<instagram_post_link>", "name": <name_from_comment>}
