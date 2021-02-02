from flask import Flask, render_template, request, redirect, url_for
from currencyconverter import currency_list, create_csv

app = Flask(__name__)

@app.route('/currency_converter/', methods=['POST', 'GET'])
def index():
    create_csv()
    if request.method == 'POST':
        currency = request.form['currency']
        amount = request.form['amount']

        for dic in currency_list:
            if dic["currency"] == currency:
                value = dic["ask"]
                value = format((value*int(amount)), "7.2f")
                score = str(value)

        else:
            print("calculation completed")
            return render_template('completed.html', score=score, currency=currency, amount=amount)

    else:
        return render_template('currencyconverter.html')


if __name__=="__main__":    
     app.run(debug=True)