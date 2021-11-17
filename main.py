from flask import Flask, render_template, request
from flask_cors import CORS,cross_origin
import pickle


app = Flask(__name__)

@app.route('/' , methods =['GET'])
@cross_origin()
def homepage():
    return render_template('index.html'  )

@app.route('/predict', methods =['POST' , 'GET'])
@cross_origin()
def Prediction():
    if request.method == 'POST':
        try:
            Pclass = float(request.form['Pclass'])
            Sex = request.form['Sex']
            Age = float(request.form['Age'])
            SibSp = request.form['SibSp']
            Parch = request.form['Parch']
            Fare = float(request.form['Fare'])

            filename = 'decision_tree.pickle'
            load_model = pickle.load(open(filename, 'rb'))
            predictionans = load_model.predict([[Pclass, Sex, Age, SibSp, Parch, Fare]])
            if predictionans == 1:
                prediction = 'Survived'
                image = 'http://www.takaishiigallery.com/en/wp-content/uploads/TIG_1905_Image_Press_72dpi_1200px.jpg'
            else :
                prediction = 'deceased'
                image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTWsCXEPuye-Tzd3eZ9rT8TuBvTAPIXHwfDQ&usqp=CAU'
            return render_template('results.html' , prediction = prediction , image = image)

        except Exception as e:
            print('the exception msg is : ', e)
            return 'Something went wrong'
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)
