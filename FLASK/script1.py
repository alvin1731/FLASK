from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Website content goes here ALVIN senyahan"

if __name__ == "__main__":
    app.run(debug=True)