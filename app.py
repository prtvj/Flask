from flask import Flask,request


app = Flask(__name__)


#READ QUERY PARAMETER
#@app.route("/search")
#def search():
#    name=request.args.get("name")    #for default just add"guest" in get method
#    return f"Hello: {name}"

#multiple read query parameter
@app.route("/search")
def search():
    name=request.args.get("name") 
    course=request.args.get("course")  
    return f"Hello: {name} is learning {course}"

if __name__ == "__main__":
    app.run(debug=True)