# define imports
from flask import Flask
from flask import render_template



app = Flask(__name__)




@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/01")
def index01():
    return render_template('01.html')

@app.route("/02")
def index02():
    return render_template('02.html')

@app.route("/03")
def index03():
    return render_template('03.html')

@app.route("/04")
def index04():
    return render_template('04.html')

@app.route("/05")
def index05():
    return render_template('05.html')

@app.route("/06")
def index06():
    return render_template('06.html')

#-------------------------------------------------------------
# standard boilerplate
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
