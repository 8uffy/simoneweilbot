# Add all import statements at top of file
import tweepy
from time import sleep
from credentials import *
auth = tweepy.OAuthHandler('ARTZH4SKe6ZmlQZ7y2C3oOJ15', 'yvnYmzpHpub7z1v27XYIU63mmk0XWYlgHeAYCJq4KVA9uIvYTu')
auth.set_access_token('1410680712630394881-CjtJGrWTfHiOGXaGsrEpKgdSNx0UBu', 'SXJZEdK1I3RH9bCR6f3jYFWu7MZ1PVHUT5ndIxouRwxpY')
api = tweepy.API(auth)

my_file=open('gravityandgrace1.txt','r')
file_lines=my_file.readlines()
my_file.close()

for line in file_lines:
# Add try ... except block to catch and output errors
    try:
        print(line)
        if line != '\n':
            api.update_status(line)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
    sleep(1800)

