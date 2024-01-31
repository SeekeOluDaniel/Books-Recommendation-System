# Import the dependencies.
from flask import Flask, jsonify, render_template


#################################################
# Flask Setup
#################################################
app=Flask(__name__)

# #################################################
# # Flask Routes
# #################################################

@app.route("/")
def index():
    return render_template("index.html")

if __name__== "__main__":
    app.run(debug=True)