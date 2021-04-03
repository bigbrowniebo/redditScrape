import praw
import urllib.request
import os
import datetime

reddit = praw.Reddit(
     client_id="client id", #enter your client id
     client_secret="client secret", #enter your client secret
     user_agent="scrape",
     username="username", #enter your reddit username
     password="password"  #enter your reddit password
 )
count = 1
date = datetime.datetime.now().date()
directory = str(date)
parent_dir = "Directory"  \\enter the directory you want your images to be saved
path = os.path.join(parent_dir, directory)
os.mkdir(path) 
os.chdir(path)

for submission in reddit.subreddit("subreddit").hot(limit=None): #enter a valid subreddit name in place of subreddit
	if not submission.stickied:
		url = str(submission.url)
		title = str(submission.title)
		if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):
			urllib.request.urlretrieve(url, f"{title}({count}).jpg")
			count += 1
			if count == 10:  #you can change the count to number of images you want to download
				break

	
