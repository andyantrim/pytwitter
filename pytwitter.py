from flask import Flask, render_template, request
from tw import Twitter

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def homescreen():
    tweets = Twitter().get_all_tweets()
    if request.method == 'POST':
        if request.form['text']:
            Twitter().post_tweet(text=request.form['text'])
            return render_template('index.html', tweets=tweets, posted=True)


    if request.method == 'GET':
        return render_template('index.html', tweets=tweets)

@app.route("/me", methods=['GET', 'POST'])
def userscreen():
    tweets = Twitter().get_my_tweets()
    if request.method == 'POST':
        if request.form['text']:
            Twitter().post_tweet(text=request.form['text'])
            return render_template('index.html', tweets=tweets, posted=True)


    if request.method == 'GET':
        return render_template('index.html', tweets=tweets)

if __name__ == '__main__':
    app.debug = True
    app.run()
