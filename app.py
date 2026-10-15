from flask import Flask,request,render_template


app = Flask(__name__)


#READ QUERY PARAMETER
#@app.route("/search")
#def search():
#    name=request.args.get("name")    #for default just add"guest" in get method
#    return f"Hello: {name}"

#multiple read query parameter
@app.route("/")
def home():
    #name=request.args.get("name") 
    #course=request.args.get("course")  
    first_name="Mohit"
    last_name="Kumar"
    age=23
    price=500
    course=["Python", "Java", "C++"]
    return render_template("index.html",first_name=first_name,last_name=last_name
                           ,age=age,price=price,course=course)

if __name__ == "__main__":
    app.run(debug=True)