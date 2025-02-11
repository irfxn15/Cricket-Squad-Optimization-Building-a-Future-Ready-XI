from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Load cleaned dataset
@app.route('/api/players', methods=['GET'])
def get_players():
    # Example: Load your transformed dataset
    data = pd.read_csv('players_data.csv')  # Replace with your dataset path
    return jsonify(data.to_dict(orient='records'))

# Serve frontend
@app.route('/')
def index():
    return render_template('index.html')  # Your HTML frontend

if __name__ == '__main__':
    app.run(debug=True)
