from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    return render_template('calculadora.html', error="Cannot divide by zero!")
                result = num1 / num2
            else:
                return render_template('calculadora.html', error="Invalid operation")

            return render_template('calculadora.html',
                                   num1=num1,
                                   num2=num2,
                                   operation=operation,
                                   result=round(result, 4))

        except ValueError:
            return render_template('calculadora.html', error="Please enter valid numbers")

    return render_template('calculadora.html')


if __name__ == '__main__':
    app.run(debug=True)
