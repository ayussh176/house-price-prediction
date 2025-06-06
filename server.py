from flask import Flask, request, render_template, redirect, url_for
import util

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict_page():
    util.load_saved_artifacts()
    # Pass dummy values for prediction to avoid error on initial load
    return render_template('index.html', locations=util.get_location_names(), prediction=None, total_sqft=None, bhk=None, bath=None, location=None)

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    prediction = util.get_estimated_price(location, total_sqft, bhk, bath)

    return render_template('index.html',
                           locations=util.get_location_names(),
                           prediction=prediction,
                           total_sqft=total_sqft,
                           bhk=bhk,
                           bath=bath,
                           location=location) # Pass selected location back to pre-select it

if __name__ == "__main__":
    print("Starting Flask Server...")
    app.run(debug=True)