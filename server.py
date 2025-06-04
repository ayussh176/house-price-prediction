from flask import Flask, request, render_template
import util

app = Flask(__name__)

@app.route('/')
def home():
    util.load_saved_artifacts()
    return render_template('index.html', locations=util.get_location_names())

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    prediction = util.get_estimated_price(location, total_sqft, bhk, bath)

    return render_template('index.html',
                           locations=util.get_location_names(),
                           prediction=prediction)

if __name__ == "__main__":
    print("Starting Flask Server...")
    app.run(debug=True)
