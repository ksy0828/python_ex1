from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

#DB 연결
client = MongoClient('mongodb://localhost:27017') 
db = client['shodan_db']
collection = db['webcam_results']

@app.route('/')
def index():
    results = collection.find()
    print(results)    
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)