from volansapp import app

# Importing required functions
from flask import render_template, request


# Root endpoint
@app.get("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.post("/citas_upload")
def citas_upload():
    return render_template("citas/upload.html")


@app.post("/citas_view")
def citas_view():

    import pandas

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
