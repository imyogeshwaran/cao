from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Signed Magnitude Addition
@app.route('/add', methods=['POST'])
def signed_magnitude_addition():
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    result = num1 + num2  # Simple addition (as an example)
    return jsonify(result=result)

# Signed Magnitude Subtraction
@app.route('/subtract', methods=['POST'])
def signed_magnitude_subtraction():
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    result = num1 - num2  # Simple subtraction (as an example)
    return jsonify(result=result)

# Binary Multiplication
@app.route('/multiply', methods=['POST'])
def binary_multiplication():
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    result = bin(int(num1) * int(num2))[2:]  # Multiplying in binary
    return jsonify(result=result)

# Booth Multiplication
@app.route('/booth', methods=['POST'])
def booth_multiplication():
    # Booth’s multiplication algorithm is more complex, here's a simple example:
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    result = int(num1) * int(num2)  # Placeholder for Booth's multiplication
    return jsonify(result=bin(result)[2:])

# Binary Division (Restoring Method)
@app.route('/divide', methods=['POST'])
def binary_division():
    data = request.get_json()
    num1 = data.get("num1")
    num2 = data.get("num2")
    if int(num2) == 0:
        return jsonify(result="Division by zero error")
    quotient = int(num1) // int(num2)  # Integer division
    remainder = int(num1) % int(num2)  # Remainder
    return jsonify(result=f"Quotient: {bin(quotient)[2:]}, Remainder: {bin(remainder)[2:]}")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
