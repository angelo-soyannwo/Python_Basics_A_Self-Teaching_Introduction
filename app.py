
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="template")

@app.route("/")
def hello():
	return "Hello, World!"


if __name__ == '__main__':
	app.run(deibug=True)   


