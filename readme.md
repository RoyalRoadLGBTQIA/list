Planning on the updates
1. Use the RSS syndicate to track latest update.
2. If found HIATUS, do not read the feed
```
bundle exec jekyll serve
npm run build:js .
```

```html
<script type="text/javascript" src="https://rss2json.com/gfapi.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<div id="feed"></div>
```

```js
google.load("feeds", "1");

function initialize() {
  var feed = new google.feeds.Feed("https://www.royalroad.com/syndication/50866");
  
  feed.load(function(result) {
    if (!result.error) {
      var container = document.getElementById("feed");
      var entry = result.feed.entries[0];

      $("#feed").append("<h2>"+result.feed.title+" "+entry.publishedDate+"</h2>")
    }
  });
}
google.setOnLoadCallback(initialize);
```