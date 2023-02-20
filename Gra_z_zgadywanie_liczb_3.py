from flask import Flask, request, render_template

app = Flask(__name__)


def checking_number(min, max):
    """
    Returns the value which is guessed by computer
    :param min: int, minumum value of range
    :param max: int, maximum value of rnage
    :return: int, returns the counted value from range
    """
    return int((max-min)/2) + min


@app.route("/", methods=["GET", "POST"])
def guess_the_number():
    """
    Check if the value suggested by application is our chosen value. Comment the value given in each step.
    On base of our comment function will guess our number in max 10 steps.
    """
    if request.method == 'GET':
        min = 0
        max = 1000
        guess = checking_number(min, max)
        ctx = {
            'min': min,
            'max': max,
            'guess': guess
        }
        return render_template('home.html', ctx=ctx)
    elif request.method == 'POST':
        min = int(request.form['min'])
        max = int(request.form['max'])
        guess = int(request.form['guess'])
        try:
            comment = request.form['comment']
            if comment == 'too big':
                max = guess
            elif comment == 'too small':
                min = guess
            elif comment == 'you guessed!':
                return render_template('win.html')
        except Exception:
            pass
        guess = checking_number(min, max)
        ctx = {
            'min': min,
            'max': max,
            'guess': guess
        }
        return render_template('gra_w_zgadywanie_liczb.html', ctx=ctx)



if __name__ == "__main__":
    app.run(debug=True)
