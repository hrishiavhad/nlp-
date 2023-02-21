from flask import Flask,render_template,request
import jsonify
import pickle

app=Flask(__name__)

model=pickle.load(open('count2.pkl','rb'))
model1=pickle.load(open('model2.pkl','rb'))

@app.route('/')
def hellow():
    result= ''
    return render_template('index.html', **locals())

@app.route('/predict',methods=['POST',"GET"])
def predict():
    Headline=str(request.form['Headline'])
    arr=model.transform([Headline])
    result=(str(list(model1.predict(arr))[0]))

    if result=='0':
        return 'Sport'

    elif result=='1':
        return 'Business'

    elif result=='2':
        return 'Politics'

    elif result=='3':
        return 'Entertainment'

    else :
        return 'Tech'

if __name__== "__main__":
    app.run(host='0.0.0.0',port=2100)