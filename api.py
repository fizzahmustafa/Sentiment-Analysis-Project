from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("model (1).pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data['text']

    transformed = vectorizer.transform([text])
    prediction = model.predict(transformed)[0]

    return jsonify({"sentiment": prediction})

if __name__ == '__main__':
    app.run(debug=True)