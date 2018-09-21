from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener



# Basic listener 
class Listener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

	# User credentials
    access_token = "your access token"
    access_token_secret = "your access token secret"
    consumer_key = "your consumer key"
    consumer_secret = "your consumer secret"

    #Twitter authetification and Connection to Twitter Streaming API
    listener = Listener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream_data = Stream(auth, listener)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    word_to_track = [  

                        'Data Science','datascience',
                        'Machine Learning','machinelearning',
                        'Deep Learning','deeplearning',
                        'Artificial Intelligence','artificialintelligence'
                        'Blockchain',

                    ]
    stream_data.filter(track = word_to_track)
