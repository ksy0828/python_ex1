from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/") #라우터..패킷들을 최적화시켜서 도착하게 하는 것..?
def hello_world():
    return render_template("index.html")

@app.route("/rss", methods=['GET', 'POST']) 
def rss():
    rss_url = request.form['rss_url']
    print(rss_url)
    return render_template("rss.html")
    
if __name__ == '__main__':
    app.run(debug=True)