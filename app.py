from flask import Flask,render_template,request

import requests

api_key = "your-api-key"
url = "http://data.fixer.io/api/latest?access_key=" + api_key

app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def index():

    if request.method =="POST":
        firstCurrency = request.form.get("firstCurrency")
        secondCurrency = request.form.get("secondCurrency")
        amount = request.form.get("amount")

        response = requests.get(url)

        jsonData = response.json()

        firstValue = jsonData["rates"][firstCurrency]
        secondValue = jsonData["rates"][secondCurrency]

        result = (secondValue/firstValue) * float(amount)

        currencyDict = dict()

        currencyDict["firstCurrency"] = firstCurrency
        currencyDict["secondCurrency"] = secondCurrency
        currencyDict["amount"] = amount
        currencyDict["result"] = result

        return render_template("index.html",data= currencyDict)

    else:

        return render_template("index.html")


if __name__ =="__main__":
    app.run(debug=True)