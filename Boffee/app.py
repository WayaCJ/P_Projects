from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def print_message():
    return "I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response."

def order_latte(milk_type):
    if milk_type == 'a':
        return '2% latte'
    elif milk_type == 'b':
        return 'Non-fat latte'
    elif milk_type == 'c':
        return 'Soy latte'
    else:
        return print_message()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        size = request.form["size"]
        drink_type = request.form["drink_type"]
        milk_type = request.form.get("milk_type", "")
        cup = request.form["cup"]
        temp = request.form["temp"]
        name = request.form["name"]

        if drink_type == "Latte":
            drink_type = order_latte(milk_type)
        
        return render_template(
            "result.html",
            size=size,
            drink_type=drink_type,
            cup=cup,
            temp=temp,
            name=name,
        )
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
