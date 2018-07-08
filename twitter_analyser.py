'''
Created By :- 
	Dharmendra Choudhary
	VIT university,Vellore,Tamil Nadu,India
'''
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import os
import glob
import Twitter_authentication
 

class TwitterStreamer():
    
    def __init__(self):
        pass

    def stream_tweets(self, output_file, Hash_tags):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(output_file)
        auth = OAuthHandler(Twitter_authentication.CONSUMER_KEY, Twitter_authentication.CONSUMER_SECRET)
        auth.set_access_token(Twitter_authentication.ACCESS_TOKEN, Twitter_authentication.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=Hash_tags)


class StdOutListener(StreamListener):
    
    def __init__(self, output_file):
        self.output_file = output_file

    def on_data(self, data):
        try:
			
            print(data)
            with open(self.output_file, 'a') as tf:
                tf.write(data)
		return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

 
 
 
if __name__ == '__main__':
    files = glob.glob('/home/dammonoit/Desktop/twitter_app/App3/Outputs_txt/*')
    for f in files:
		os.remove(f)
    print("The data Collected From the Tweepy API is: \n")
    Hash_tags = ["India"]
    output_file = "Outputs_txt/tweets.txt"
    

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(output_file, Hash_tags)
