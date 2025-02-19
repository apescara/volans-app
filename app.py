# Importing required functions
import pandas
from flask import Flask, render_template, request
from fileinput import filename

# Flask constructor
app = Flask(__name__)

# Root endpoint


@app.get("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.post("/upload-citas")
def upload_citas():
    return render_template("upload-citas.html")


@app.post("/view-citas")
def view_citas():

    # Read the File using Flask request
    file = request.files["file"]
    # save file in local directory
    file.save(file.filename)

    # Parse the data as a Pandas DataFrame type
    data = pandas.read_excel(file)

    # Return HTML snippet that will render the table
    return data.to_html()


# Main Driver Function
if __name__ == "__main__":
    # Run the application on the local development server
    app.run(debug=True, host="0.0.0.0", port="8080")
