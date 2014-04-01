#!/usr/bin/python2.7

# vitumblr - Post to Tumblr using VIM
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pytumblr
import sys, tempfile, subprocess, re

# ------------------------- USER CONFIG -------------------------#

# Write here your account name
username = 'carpikes'

# Write here your favorite editor
editor = 'vim'

# You have to register a new application here: http://www.tumblr.com/oauth/apps
# And here you can get keys and secrets: https://api.tumblr.com/console
consumer_key    = ''
consumer_secret = ''
oauth_token     = ''
oauth_secret    = ''

# --------------------------------------------------------------- #

# Initialize tumblr client
client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_token,
    oauth_secret 
)

temp = tempfile.NamedTemporaryFile(prefix='tumblr',dir='/tmp')

edit = True
while edit:
    subprocess.call([editor, temp.name])
    text = open(temp.name, 'r').read()

    if len(text)<2:
        print("Content too short. Exiting...")
        quit()

    title = ''
    lines = text.splitlines()
    if len(lines)>1:
        title = lines[0].strip()
        if len(lines)>1 and len(lines[1].strip())==0:
            lines = lines[2:]
        else:
            lines = lines[1:]

    content = "\n".join(lines)

    if len(title)>0:
        print "=> Title: '"+title+"'"
    else:
        print "=> Title: NO"
    print "=> Content:\n"+content+"\n----"

    while True:
        state = raw_input("Post? [PUBLISH|draft|queue|private|edit]: ").lower()
        if len(state)==0:
            state='publish'

        if state=='publish' or state=='draft' or state=='private' or state=='queue':
            ret = client.create_text(username, state=state, title=title, body=content)
            if 'id' in ret:
                if state=='publish':
                    print "Posted: http://" + username + ".tumblr.com/post/" + str(ret['id']) + "/"
                else:
                    print "Posted ("+str(ret['id']) + ")"
            else:
                print "Error!"
                print ret

            edit = False
            break
        elif state=='edit':
            break
        else:
            print "What?"
