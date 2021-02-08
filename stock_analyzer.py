
import praw
import sys

class stock_analyzer(object):

    def __init__(self):
        self.r = praw.Reddit(user_agent='WSB Stock Analyzer', client_id='gLYszkvAMDEmCg', client_secret='lHNozyOHkP7eMUOlEJiZnw6rnP1DxA')
        self.main()
        
    def read_symbols(self):
        f = open("./symbols.txt", "r")
        self.symbol_dict = {x.strip().upper(): 0 for x in f.readlines()}

    def get_subreddit_subs(self, subreddit):
        wsb = self.r.subreddit(subreddit)
        self.submissions = wsb.hot(limit=self.limit)
        
    def populate_symbols_dict(self):
        for submission in self.submissions:
            title = submission.title.upper()

            for word in title.split():
                if word.startswith('$'): # $AAPL == AAPL
                    word = word[1:]

                if word in self.symbol_dict.keys():
                    self.symbol_dict[word] += 1

    def sort_symbols_mentions(self):
        self.symbol_dict = dict(sorted(self.symbol_dict.items(), key=lambda item: item[1], reverse=True))

    def build_output(self):
        print ('Scanned top %d submissions from r/wallstreetbets' % self.limit)
        for key in self.symbol_dict.keys():
            if self.symbol_dict[key] > 0:
                print ('%s Mentions: %d' %(key.upper(), self.symbol_dict[key]))

    def main(self):
        self.limit = int(sys.argv[1])

        self.read_symbols()
        self.get_subreddit_subs("wallstreetbets")
        self.populate_symbols_dict()
        self.sort_symbols_mentions()
        self.build_output()

if __name__ == "__main__":
    stock_analyzer()