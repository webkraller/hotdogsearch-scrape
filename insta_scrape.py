import time
import re
import urllib
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox


def recent_post_links(username, post_count=10):
    """
    With the input of an account page, scrape the 10 most recent posts urls

    Args:
    username: Instagram username
    post_count: default of 10, set as many or as few as you want

    Returns:
    A list with the unique url links for the most recent posts for the provided user
    """
    url = "https://www.instagram.com/" + username + "/"
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    browser = Firefox(firefox_options=firefox_options)
    browser.get(url)
    post = 'https://www.instagram.com/p/'
    post_links = []
    while len(post_links) < post_count:
        links = [a.get_attribute('href')
                 for a in browser.find_elements_by_tag_name('a')]
        for link in links:
            if post in link and link not in post_links:
                post_links.append(link)
        scroll_down = "window.scrollTo(0, document.body.scrollHeight);"
        browser.execute_script(scroll_down)
        time.sleep(10)
    else:
        browser.stop_client()
        return post_links[:post_count]


def insta_link_comments(url):
    """
    Take a post url and return post details

    Args:
    urls: a list of urls for Instagram posts 

    Returns:
    A list of dictionaries with details for each Instagram post, including link,
    post type, like/view count, age (when posted), and initial comment
    """
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    browser = Firefox(firefox_options=firefox_options)
    browser.get(url)

    comment = browser.find_element_by_xpath(
        """//*[@id="react-root"]/section/main/div/div[1]/
			article/div/div[3]/div[1]/ul/div/li/div/div/div[2]/span""").text
    post_details = {'link': url,
                    'name': comment,
                    }
    time.sleep(1)
    browser.close()
    return post_details
