from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        username = request.form.get('uname')
        password = request.form.get('psw')

        if username == 'dev' and password == '123':
            return render_template('index.html')
        else:
            return "Invalid credentials, please try again."

if __name__ == "__main__":
    app.run(debug=True)
