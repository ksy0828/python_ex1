from flask import Flask, render_template, request
import feedparser

#https://www.dailysecu.com/rss/allArticle.xml

app = Flask(__name__)

@app.route("/") #라우터..패킷들을 최적화시켜서 도착하게 하는 것..?
def index():
    return render_template("index.html")

@app.route("/rss", methods=['GET', 'POST']) 
def rss():
    rss_url = request.form['rss_url']
    # print(rss_url)
    feed = feedparser.parse(rss_url)
    # print(feed)
    return render_template("rss.html", feed=feed) #'보낼때 변수명'='원래사용한변수' 
    
if __name__ == '__main__':
    app.run(debug=True)