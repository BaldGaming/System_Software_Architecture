class Twitter:
    def send(self, msg):
        print(msg)

class TwitterAdapter:
    def __init__(self):
        self.tweet = Twitter()

    def send(self, msg):
        self.tweet.send(msg)

def main():
    tweetAdapter = TwitterAdapter()
    tweetAdapter.send("posting on twitter")
main()