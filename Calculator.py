from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    # Get the operation from the request
    operation = request.form.get("operation")

    # Get the two numbers from the request
    number1 = request.form.get("number1")
    number2 = request.form.get("number2")

    # Perform the operation on the two numbers
    result = " "
    if operation == "add":
        result = int(number1) + int(number2)
    elif operation == "subtract":
        result = int(number1) - int(number2)
    elif operation == "multiply":
        result = int(number1) * int(number2)
    elif operation == "divide":
        result = int(number1) / int(number2)

    # Render the HTML template with the result
    return render_template("calcu_index.html", operation=operation, number1=number1, number2=number2, result=result)

if __name__ == "__main__":
    app.run(debug=True)
