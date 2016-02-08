# pytwitter
A web UI that interfaces with your twitter account, basic little home project to learn flask and the twitter API

# Install
This should work on any OS but I set mine up on OpenSuse, so the install script is to set it up for that.
Firstly create the directory /etc/pytwitter
Then create a file called config, this file will have 4 lines including keys and secret keys from the twitter API (to allow the program to use your account you will need to set up api keys at https://apps.twitter.com/)
Then in each new line of the program add in order
access_token
access_token_secret
consumer_key
consumer_secret
At the moment the program strips of the last two characters as they are new line characters (Made the config in vi, not sure how this will react in other programs but will when I encounter any problems)
Now The script installs the pip dependecies using:
pip install -r req.txt
That should be the project all setup 


# Disclaimer
I am not a graphic designer, I know it looks like garbage, but i'm more interested in learning how to use flask and APIs
Feel free to fork off, and do whatever, this is all just for fun!
