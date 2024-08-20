from flask import Flask, jsonify, request
import requests
 
app = Flask(__name__)
 
@app.route("/")
 
def chuck():
    '''Return a Chuck Norris joke'''
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    chuck_joke = response.json()["value"]
    return chuck_joke
 
@app.route("/joke")
def joke():
    joke = chuck() 
    return joke
