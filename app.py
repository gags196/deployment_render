from flask import Flask, render_template, request
import joblib

# initialise the app
app = Flask(__name__)

# load the model
model = joblib.load('dib_79.pkl')

@app.route('/')
def hello():
    return(render_template('form.html'))


@app.route('/submit', methods = ["POST"])
def form_data():
    preg = float(request.form.get('preg'))
    plas = float(request.form.get('plas'))
    pres = float(request.form.get('pres'))
    skin = float(request.form.get('skin'))
    test = float(request.form.get('test'))
    mass = float(request.form.get('mass'))
    pedi = float(request.form.get('pedi'))
    age = float(request.form.get('age'))

    output = model.predict([[preg,plas,pres,skin,test,mass,pedi,age]])

    print(output)

    if output[0] == 1:
       out = 'Diabatic'
    else:
       out = 'not Diabatic'
    
    return render_template('predict.html', data = f'person is {out}')


if __name__ == '__main__':
    app.run(debug=True)