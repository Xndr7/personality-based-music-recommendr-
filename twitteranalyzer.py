import sys
import requests
import json
import twitter
import config


def convert_status_to_pi_content_item(s):
    # My code here
    return {
        'userid': str(s.user.id),
        'id': str(s.id),
        'sourceid': 'python-twitter',
        'contenttype': 'text/plain',
        'language': s.lang,
        'content': s.text,
        'created': s.created_at_in_seconds,
        'reply': (s.in_reply_to_status_id == None),
        'forward': False
    }


handles = ["Annemazer","ASWinn","Cbarzak","chuckpalahnuik","DebraSnider","hamishmacdonald","OrnaRoss"
        ,"warrenadler","Charlottehughes","clairecameron","jamesscottbell","libbyfh","thrillerchick","Annewhitefield"
,"jennablack","AlanBaxter","joe_hill","matociquala","neilhimself","sherrilynkenyon",
"TheKJA","tobiasbuckell","Sandra_Gullard","stephenfry","realjohngreen","judyblume",
"MargaretAtwood","Writer_DG","JaneEspenson","StephenKing","PhilipPullman","jonfmerz"]

music_handles =["Behzinga","miniminter","Tobjizzle","wroetoshaw","KSIOlajidebt","Vikkstar123","ZerkaaHD"]

twitter_api = twitter.Api(consumer_key = config.twitter_consumer_key,
                          consumer_secret = config.twitter_consumer_secret,
                          access_token_key = config.twitter_access_token,
                          access_token_secret = config.twitter_access_secret,
                          debugHTTP=True)
def personalityinsights(handle):
        max_id = None
        statuses = []
        for x in range(0, 16):  # Pulls max number of tweets from an account
                if x == 0:
                        statuses_portion = twitter_api.GetUserTimeline(screen_name=handle,
                                                       count=200,
                                                       include_rts=False)
                        status_count = len(statuses_portion)
                        max_id = statuses_portion[status_count - 1].id - 1  # get id of last tweet and bump below for next tweet set
                else:
                        statuses_portion = twitter_api.GetUserTimeline(screen_name=handle,
                                                       count=200,
                                                       max_id=max_id,
                                                       include_rts=False)
                        status_count = len(statuses_portion)
                        max_id = statuses_portion[status_count - 1].id - 1  # get id of last tweet and bump below for next tweet set
                for status in statuses_portion:
                        statuses.append(status)

        pi_content_items_array = map(convert_status_to_pi_content_item, statuses)
        pi_content_items = {'contentItems': pi_content_items_array}

        r = requests.post(config.pi_url + '/v2/profile?headers=True',
                  auth=(config.pi_username, config.pi_password),
                  headers={
                      "content-type": "text/plain",
                      "accept": "text/csv"
                  },
                  data=json.dumps(pi_content_items)
                  )

        print("Profile Request sent. Status code: %d, content-type: %s" % (r.status_code, r.headers['content-type']))
#print json.loads(r.text)
        with open('pi_5.csv','w') as f:
                print >> f, r.text
