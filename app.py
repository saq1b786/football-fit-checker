from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
  return render_template("home.html")



@app.route('/about')

def about():
  return 'about page'

@app.route('/player')
def players():
  return "player info to come soon!"

@app.route('/team')
def teams():
  return "team info coming soon"

if __name__ == '__main__':
  app.run(debug=True)