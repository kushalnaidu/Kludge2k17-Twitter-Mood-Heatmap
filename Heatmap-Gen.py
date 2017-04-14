import re
from textblob import TextBlob
from tweepy import OAuthHandler
from textblob import TextBlob
import tweepy
import matplotlib
class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'ZHVw6g8pHNsKTgZw3Z2zmf8gD'
        consumer_secret = 'kmTLUtrnRGrHItrbdqPS2zOv6Lnd1SlFY2RbHqUhLi53yPX9m0'
        access_token = '3306838494-XqZSCK7IFlZMUB48hC1TJnwZHj57wDapky196Oo'
        access_token_secret = '84MdMlsysDfVM6tTxiYGXfoK4es2u7E0CJgf5KLhHrTyV'
 
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0.1:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        elif analysis.sentiment.polarity<0.1:
            return 'negative'
 
    def get_tweets(self, query, gc,count = 100):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []
 
        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = 4000000,geocode=gc,until="2016-04-14")
            print len(fetched_tweets)
            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}
 
                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
 
                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
            # return parsed tweets
            return tweets
 
        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))
 
def main():
    # creating object of TwitterClient Class
    negative=[]
    latitudes=[]
    longitudes=[]
    positive=[]
    api = TwitterClient()
    lat_s=12.85
    lat_n=13.16
    long_e=77.76
    long_w=77.45
    '''
    for i in [12.85,12.90,12.95,13,13.05,13.1,13.15]:
        for j in [77.45,77.5,77.55,77.6,77.65,77.70,77.75]:
            latitudes.append((i-12.85)*100)
            longitudes.append((j-77.45)*100)
            
    # calling function to get tweets
    #tweets = api.get_tweets(query = 'Kill OR Trump OR Protest OR Riot OR Fight OR War OR Bomb OR Mob OR Moab OR Condemn:( -#IPL')
            tweets = api.get_tweets(query = 'at OR of OR jam OR Traffic OR Kill OR Trump OR Protest OR Riot OR Fight OR War OR Bomb OR Mob OR A OR a OR Moab OR Condemn OR The OR a OR world OR peace OR IPL OR #', gc=str(i)+","+str(j)+",5km")
            if(len(tweets)!=0):
                # picking positive tweets from tweets
                ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
                # percentage of positive tweets
                
                # picking negative tweets from tweets
                
                ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
                # percentage of negative tweets
                if(len(ntweets)!=0 and len(ptweets)!=0):
                    print len(ntweets),len(ptweets)
                    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))    
                    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
                    # percentage of neutral tweets
                    negative.append(100*len(ntweets)/len(tweets))
                    
                    print("Neutral tweets percentage: {} % \
                        ".format((100*len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
                    positive.append(100*len(ptweets)/len(tweets))
                    
                    print("\n\nPositive tweets:")
                    for tweet in ptweets[:2]:
                    # printing first 5 positive tweets
                        print(tweet['text'])
                 
                    # printing first 5 negative tweets
                    print("\n\nNegative tweets:")
                    for tweet in ntweets[:2]:
                        print(tweet['text'])
                    
                    print
                    print
                    print
                else:
                    negative.append(-1)
                    positive.append(-1)
            else:
                positive.append(-1)
                negative.append(-1)
    print negative
    print len(negative)
 
    
    
    import pandas as pd
    df=pd.DataFrame()
    df['Lat']=latitudes
    df['Longi']=longitudes
    df['Pos']=positive    
    df['Neg']=negative
        
    df.to_csv("data.csv");
    '''
    import pandas as pd
    df=pd.read_csv("data.csv");
    latitudes=df['Lat']
    longitudes=df['Longi']
    negative=df["Neg"]
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from pylab import rcParams
    rcParams['figure.figsize'] = 15,10
    from scipy.misc import imread
    fig5 = plt.figure()
    ax5 = fig5.add_subplot(111, aspect='equal')
    count=0
    
    nneg=[]
    for i in range(len(negative)):
        nneg.append((negative[i]-min(negative))/((max(negative)-min(negative))*1.0))
    #print nneg
    
    #print len(nneg)
    #print len(latitudes)
    for i in range(49):
            
            #print i+5,j+6465
            p=patches.Circle((((latitudes[i]+2.5)*46.67),(longitudes[i]+2.5)*46.67), 2.5*140/3.0,alpha=negative[i]/100.0)
            p.set_facecolor('r')
            ax5.add_patch(p)
    #p=patches.Circle((0,0), 5*50/3,alpha=0.1)
    #ax5.add_patch(p)
    #fig5.savefig('circle5.png', dpi=90, bbox_inches='tight')
    img=imread("./pic.jpg")
    plt.imshow(img,extent=[0, 1400, 0, 1400])
    
    plt.show()
if __name__ == "__main__":
    # calling main function
    main()