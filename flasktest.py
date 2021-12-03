

from flask import Flask

def main():
	app = Flask(__name__)

	@app.route("/")
	def hello():
    		return "Hello, World!"


if __name__ == '__main__':
	main()
