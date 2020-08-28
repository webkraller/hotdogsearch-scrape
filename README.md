### What Hot Dog You Are Scrape

I was sent a link to an instagram site where I could find what hotdog I was. But on Instagram you cannot search by plaintext comments! Was I really expected to scroll through the entire published body of work to find what hotdog I was?

Instead of wasting my time, I wrote a simple Instagram post indexer with Python and Selenium, then dumped the resulting json data into a searchable site.
The actual instagram scrape code is built on top of the work done by https://github.com/jnawjux/web_scraping_corgis.

### Quick Start

Installation: Clone this repo and cd into it. Make sure geckodriver the Firefox Selenium Driver is executable in project path.
Edit the scrape.py file with your desired account names and post counts.
Then run `python scrape.py` to run the scraper(s).
After getting the JSON data you can import into whatever search you want!
JSON format = {"link": "<instagram_post_link>", "name": <name_from_comment>}
