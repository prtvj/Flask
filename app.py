from flask import Flask
app=Flask(__name__)
@app.route("/")
def home():
    return "Home page!"
@app.route("/about")
def about():
    return "About page!"
@app.route("/contact")
def contact():
    return "Contact page!"
@app.route("/name/<name>")
#def name(name):
#    return f"Hello, {name}!"
@app.route("/toy/<name>/<toy>")
def toy(name,toy):
    return f"{name} Your favorite toy is {toy}!"
if __name__ =="__main__":
    app.run(debug=True)