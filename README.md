### Reddit WallStreetBets Stock Analyzer

Script that spits out most commonly talked about stock symbols in Reddit's WallStreetBets forum.
Stock symbols are read from a text file - symbols.txt

Usage:
```
python3 stock_analyzer.py <number_of_top_posts_to_scan>
```

Sample output:
```
Dragans-MacBook-Pro:wsb-stock-analyzer dragan224$ python3 stock_analyzer.py 1000
Scanned top 1000 submissions from r/wallstreetbets
GME Mentions: 176
AMC Mentions: 53
BB Mentions: 1
```

### Requirements
Reddit praw package
```
pip3 install praw
```
