import tweepy
import pprint

#Twitter Deverloper Portalで取得したAPIキーをコーテション('')の間にそれぞれ入れる
CONSUMER_KEY = 'DXO9MO2SefHUVehYmOb70ZFwo'
CONSUMER_SECRET = 'IcfOpQePDt0MYFWM7IZaS2umhdHoDLDa8Sf1b1ApN0Q7jLiu0a'
#Twitter Deverloper Portalで取得したベアラートークンをコーテション('')の間に入れる
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAEW1gQEAAAAA4qT%2B9JI98Bd0aNLg6MC%2Fkkjym5A%3Db8gSdGEONDsSuUMQKruVbxKJZ7aMFH2Xodj6OlFecfoumByp0Y'
#Twitter Deverloper Portalで生成したアクセストークンをコーテション('')の間にそれぞれ入れる
ACCESS_TOKEN = '1563493820548804609-PK4fSXALoSGB2bvVn596Li8maA5zb0'
ACCESS_SECRET = '7JeTssSjgAfUKYRwmCbcjsuyxbXLUX41xmiua3heqzyD0'


client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET,
    bearer_token=BEARER_TOKEN
)

# 最新のツイートを取得

tweets = client.search_recent_tweets(query='#フォロー100',  # 検索ワード
                                     max_results=20  # 取得件数
                                     )


#リファレンスの内容に沿って入力（https://docs.tweepy.org/en/stable/client.html）
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

def GetTweet(tweet_id):
    # メソッド実行
    GetTwt = client.get_tweet(id=int(tweet_id), expansions=["author_id"], user_fields=["username"])
    return GetTwt

#print(client.get_users_following(id=1563493820548804609))

def FollowUser(user_id):
    fol = client.follow_user(target_user_id = user_id)
    return fol


tweets=tweets.data


for i in tweets:
    id=i.id
    newid=GetTweet(id).includes['users'][0].id
    name=GetTweet(id).includes['users'][0].name
    #try:
    FollowUser(newid)
    print(f"{name}をフォローしました")
    #except:
    print('error')
