from flask import Flask

app = Flask(__name__)

# Route for root URL
@app.route('/')
def hello_world():
    return "Hello World!"

# Route for /dojo
@app.route('/dojo')
def dojo():
    return "Dojo!"

# Route for /say/<name>
@app.route('/say/<name>')
def say_name(name):
    return f"Hi {name.capitalize()}!"

# Route for /repeat/<int:num>/<word>
@app.route('/repeat/<int:num>/<word>')
def repeat_word(num, word):
    return f"{word * num}"

# Ninja Bonus: Catch-all route for undefined routes
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404

if __name__ == "__main__":
    app.run(debug=True)
