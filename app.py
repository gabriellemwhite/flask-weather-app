# import Flask
from flask import Flask, request, render_template
import os, requests, json

# python-dotenv reads key-value pairs from a .env file and sets them as environment variables
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# route decorator to bind the index function
@app.route('/', methods = ["GET", "POST"])
def index():
    
    # pulls information from the server
    if(request.method == 'GET'):
        
        # return index.html to the server
        return render_template("index.html")

    # sends the form data inputted by the user to the server 
    elif(request.method == 'POST'):
        
        # get user inputted values for zip code and country code
        user_zipcode = request.form.get("zip")
        user_country_code = request.form.get("country_code")
        
        # send request to openweathermap API
        openweather = requests.get("https://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}&units=imperial".format(user_zipcode, user_country_code, os.environ.get("API_KEY")))
        
        # return weather.html to the server
        return render_template('weather.html', weather=openweather.json())

# pass the zipcode and country code as keyword arguments
@app.route('/<zip>/<code>', methods = ["GET", "POST"])
def openweather_api():

    # send request to openweathermap API
    openweather = requests.get("https://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}".format(user_zipcode, user_country_code, os.environ.get("API_KEY")))
    
    # test openweather API
    print(openweather.json())

# run the application
if __name__ == '__main__':
    
    # debug set to true for testing
    app.run(debug=True)

    