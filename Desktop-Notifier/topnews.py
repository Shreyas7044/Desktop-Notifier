import requests
import xml.etree.ElementTree as ET

# URL of news RSS feed
RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

def loadRSS():
    """
    Utility function to load RSS feed
    """
    resp = requests.get(RSS_FEED_URL)
    return resp.content

def parseXML(rss):
    """
    Utility function to parse XML format RSS feed
    """
    root = ET.fromstring(rss)
    newsitems = []

    for item in root.findall('./channel/item'):
        news = {}
        for child in item:
            if child.tag == '{https://video.search.yahoo.com/mrss}':
                news['media'] = child.attrib.get('url', '')
            else:
                news[child.tag] = child.text
        newsitems.append(news)

    return newsitems

def topStories():
    """
    Main function to return top news stories
    """
    rss = loadRSS()
    return parseXML(rss)