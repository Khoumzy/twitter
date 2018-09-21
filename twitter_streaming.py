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
    access_token = "1038381241836417024-yW1e6RLMNPRGfA7h023ZcnmqxxX8ny"
    access_token_secret = "qunZX9c8wQCc2Rc7SqOqLfc5NT6dn5VztlshQWFOazQRD"
    consumer_key = "athGwMUF53WAkPGlxCQKr6zK2"
    consumer_secret = "NyKW22UcGA7YhD0UQGLqIJj886dWj0jCyszUS36060JduOxPHg"

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