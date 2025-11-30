from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return"""
    <h1> Home Page </h1>
    <h2> welcome everybody </h2>
    <h2> I am running in Flask</h2>
 <li>
 <ol>name</ol>
 <ol>email</ol>
 <ol>phone no</ol>
 
 </li>
    """

@app.route("/about")
def about():
    return"""
    <h1> I am about page </h1>
    <h2> I am running in Flask</h2>
    """
if __name__ == '__main__':
    app.run(debug=True)