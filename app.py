from flask import Flask, render_template,request

import marks as m
app = Flask(__name__)

@app.route('/', methods = ["POST","GET"])
def marks():
    if request.method == "POST":
        hrs = request.form['hrs']
        m_p = m.predict(hrs)
        print(m_p)
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)