from flask import Flask
from flask import render_template

app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Welcome to Python Flask!"

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username']
    password = request.form['password']
    return json.dumps({'status':'OK','user':user,'pass':password})

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

if __name__ == "__main__":
    app.run(debug=True)
#    app.run(debug=True,host='0.0.0.0')

