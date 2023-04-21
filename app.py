from flask import Flask,render_template,request
import requests

app =Flask(__name__)
key ="63ff97f2ee48d573bf57a5bf"

@app.route('/',methods=["POST","GET"])
def index():
    if request.method=="POST":
        firstcurrency=request.form.get("firstCurrency")
        secondcurrency=request.form.get("secondCurrency")
        amount =request.form.get("amount")


        url = f'https://v6.exchangerate-api.com/v6/{key}/latest/{firstcurrency}'
        response =requests.get(url)

        

        current =response.json()

        firstValue =current["conversion_rates"][firstcurrency]
        secondValue =current["conversion_rates"][secondcurrency]
        last_update =current["time_last_update_utc"]

        result =(secondValue/firstValue)*float(amount)

        result =round(result,2)

        currencyInfo ={"firstCurrency":firstcurrency,"secondCurrency":secondcurrency,"amount":amount,"result":result, "last_update":last_update}  

          
             
        return render_template("index.html",info=currencyInfo)

    
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=5000, debug=True)