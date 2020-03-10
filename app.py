# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/Mission_Marsdb"
mongo = PyMongo(app)

# create route that renders index.html template
@app.route("/")
def index():
        mars_dict = mongo.db.mars_data.find_one()
        return render_template("index.html", mars_html=mars_dict)
    
@app.route("/scrape")
def scraped():
    mars_data = mongo.db.mars_data
    mars_data_scrape = scrape_mars.scrape()
    mars_data.update({},mars_data_scrape,upsert=True)
    return redirect("/", code=302)
    
if __name__ == "__main__":
    app.run(debug=True)