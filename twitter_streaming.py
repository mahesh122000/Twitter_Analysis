import sys
import string
import time
from tweepy import stream
from tweepy.streaming import StreamListener
from twitter_client import get_twitter_auth

class CustomListener(StreamListener):
    
    def __init__(self,fname):
        safe_name=format_filename(fname)
        self.outfile="stream_%s.json1"%safe_name
        
    def on_data(self,data):
        try:
            with open(self.outfile,'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            sys.stderr.write("error on_data: {}\n".format(status))
            time.sleep(5)
        return True
        
    def on_error(self,status):
        if(status==420):
            sys.stderr.write("Rate limit exceeded\n")
            return False
        else:
            sys.stderr.write("error {}\n".format(status))
            return True
            
    def format_filename(fname):
        return ''.join(convert_valid(one_char) for one_char in fname)
    
    def convert_valid(one_char):
        valid_chars="-_.%s%s" % (string.ascii_letters,string.digits)
        if one_char in valid_chars:
            return one_char
        else:
            return '_'
    
    if __name__ == '__main__':
        query=sys.argv[1:]
        query_fname=' '.join(query)
        auth=get_twitter_auth()
        twitter_stream=stream(auth,CustomListener(query_fname))
        twitter_strean.filter(track=query,async=True)
        
        