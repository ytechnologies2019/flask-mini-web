from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return "Welcome to Flask! GET Method"
    elif request.method == 'POST':
        return "Welcome to Flask! Post Method"
    else:
        return "Sorry, method is not allowed"

@app.route('/home/')
def home():
    name = "Welcome to my Website"
    message = "This was made by Jinja Language"
    return render_template('home.html', name=name, message=message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == "dev" and password == "123":
            return render_template('main.html')
        else: 
            return render_template('incorrect.html')

@app.route('/fileupload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return "No file part", 400
        
        file = request.files['file']
        
        # If user does not select file, browser also
        # submits an empty part without filename
        if file.filename == '':
            return "No selected file", 400
        
        # Here you can save the file if you want
        # file.save(os.path.join('uploads', file.filename))  # Make sure to create 'uploads' directory

        return "File successfully uploaded"
    
    return render_template('fileupload.html')

if __name__ == "__main__":
    app.run(debug=True)
