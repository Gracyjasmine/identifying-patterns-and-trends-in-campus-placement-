from flask(import Flask, render_template, request
app=Flask(__name__)
import pickle
import joblib
model-pickle.load(open("placement123.pkl", 'rb'))
ct-joblib.load('placement')

@app.route('/')
def hello():
    return render_template("index.html")

Capp.route('/guest', methods = ["POST"])
def Guest():
    sen1=request.form["sen1"]
    sen2=request.form["sen2"]
    sen3-request.form["sen3"]
    sen4-request.form["sen4"]
    sen5-request.form["sen5"]
    sen6=request.form["sen6"]
    Sapp.route('/y_predict', methods = ["POST"])
    def y predict():
       x_test = [[(yo) for yo in request.form.values()]]
       prediction model.predict(x_test)
       prediction = prediction[0]
    return render_template("secondpage.html",y=prediction)