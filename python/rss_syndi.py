import os
import feedparser
NewsFeed = feedparser.parse("https://www.royalroad.com/syndication/50866")
entry = NewsFeed.entries[0]

print (entry.published)