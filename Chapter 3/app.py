from flask import Flask, render_template, request
app = Flask(__name__, template_folder="template")

@app.route("/food", methods=["POST"])
def food():
    food = request.form.get('food')
    return render_template("index.html")
    print(food)
    return render_template('index.html', result = food)

if __name__ == "__main__":
    app.run(debug=True)

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     <form action="{{url_for('home')}}">
#         <input type="text" name="food" id="">
#     </form>
#     <h3 id="result">
#         My facourite food is {{ result }}
#         </h3>
# </body>
# </html>