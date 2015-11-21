__author__ = 'mehran'
import re
import csv

path="/home/mehran/PycharmProjects/Twitter Data/tweets_of_followers.json"
tweetcounter=0
linecounter=0

datafile=open(path,'r')
for line in datafile:
    try:
        linecounter=linecounter+1
        if re.search('{',line):
           tweetcounter=tweetcounter+1
        if re.search('"rootuser": "',line):
            rootuser= line.split('"rootuser": "')[1][0:-5]
        elif re.search('"tweetdate": "',line):
            tweetdate= line.split('"tweetdate": "')[1][0:-5]
        elif re.search('"tweettext": "',line):
            tweettext= line.split('"tweettext": "')[1][0:-5]
        elif re.search('"follwerID": "',line):
            follwerID= line.split('"follwerID": "')[1][0:-3]
        if linecounter%5 == 0:

            #print tweetcounter,rootuser,follwerID,tweetdate,tweettext
	    print tweetcounter
            with open('tweets_of_followers.csv', 'a') as csvfile:
                fieldnames = ["rootuser","follwerID","tweetdate","tweettext"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({"rootuser":rootuser,"follwerID":follwerID,"tweetdate":tweetdate,"tweettext":tweettext})
            csvfile.close()
    except:
        pass

datafile.close()
