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
    courses=["Python","Java","C++"]
    student={"name":"John","age":20,"course":"Python"}
    
    return render_template("index.html",courses=courses,student=student)

if __name__ == "__main__":
    app.run(debug=True)