from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")

#query your Mongo database and pass the mars data into an HTML template to display the data.
@app.route("/")
def index():
    mars_dictionary = mongo.db.collection.find_one()
    return render_template("index.html", mars=mars_dictionary)

#/scrape that will import your scrape_mars.py script and call your scrape function.
#Store the return value in Mongo as a Python dictionary.
@app.route("/scrape")
def scraper():
    mars_data = scrape_mars.scrape()
    mongo.db.collection.update({}, mars_data, upsert=True)
    return redirect("/")
    


if __name__ == "__main__":
    app.run(debug=True)
