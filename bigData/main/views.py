import csv, re

from datetime import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from bigData.main.models import User, Tweet

def index(request, template_name):
    """
    Render index page
    """
    return render_to_response(template_name, context_instance=RequestContext(request))


def traverse_data(request):
    linecounter = 0
    data = []
    f = open("root_users.csv", 'wt')
    writer = csv.writer(f)

    with open("root_users.txt") as f:
        for line in f:
            data.append(line.replace('\"', '').rstrip('\n').lstrip('\n'))
            linecounter+=1
            print linecounter
            if linecounter % 10000:
                for d in data:
                    writer.writerow([d, 'r'])
                data = []
#    path = "tweets_of_followers.json"
#    tweetcounter = 0
#    linecounter = 0
    data = []
    full_data = []

#    datafile = open(path,'r')
#    for line in datafile:
#        linecounter = linecounter+1
#        if re.search('{',line):
#           tweetcounter = tweetcounter+1
#        if re.search('"rootuser": "',line):
#            rootuser = line.split('"rootuser": "')[1][0:-5]
        #elif re.search('"tweetdate": "',line):
        #    tweetdate = line.split('"tweetdate": "')[1][0:-5]
        #elif re.search('"tweettext": "',line):
        #    tweettext = line.split('"tweettext": "')[1][0:-5]
        #elif re.search('"follwerID": "',line):
        #    follwerID = line.split('"follwerID": "')[1][0:-3]
#        if linecounter % 5 == 0:

#            print tweetcounter,rootuser#,follwerID,tweetdate,tweettext

#            try:
#                user, created = User.objects.get_or_create(username = rootuser)
#            except:
#                pass
            #if rootuser not in full_data:
            #    data.append(user)
            #full_data.append(rootuser)

#            follower, created = User.objects.get_or_create(username = follwerID)
#            e = ExtendedUser.objects.get(user = follower)
#            e.type = 'f'
#            e.save()

#            try:
#                date_object = datetime.strptime(tweetdate, '%Y-%m-%d %H:%M%:%S')
#            except:
#                date_object = None

#            data.append(Tweet(seed_user = seed_user, follower = follower, text = tweettext, date = date_object))

#            if not (tweetcounter % 5000):
#                try:
#                    User.objects.bulk_create(data)
#                except:
#                data = []

 #   datafile.close()
    return HttpResponseRedirect(reverse('/'))