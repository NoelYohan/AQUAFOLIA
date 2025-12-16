from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
import csv
from plant_recommender import PlantRecommender

app = Flask(__name__, static_folder='.')
CORS(app)  # Enable CORS for frontend communication

# Initialize the plant recommender
recommender = PlantRecommender()

@app.route('/')
def index():
    """Serve the main dashboard HTML file."""
    return send_from_directory('.', 'index.html')

@app.route('/api/recommend-plants', methods=['POST'])
def recommend_plants():
    """
    Get plant recommendations based on water quality parameters.
    
    Expected JSON body:
    {
        "pH": float,
        "temperature": float,
        "dissolvedOxygen": float,
        "ammonia": float (optional),
        "nitrate": float (optional)
    }
    """
    try:
        data = request.get_json()
        
        # Validate input data
        required_fields = ['pH', 'temperature', 'dissolvedOxygen']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "error": f"Missing required field: {field}"
                }), 400
        
        # Extract parameters
        ph = float(data['pH'])
        temperature = float(data['temperature'])
        dissolved_oxygen = float(data['dissolvedOxygen'])
        ammonia = float(data.get('ammonia', 0.0))
        nitrate = float(data.get('nitrate', 0.0))
        
        # Validate ranges
        if ph < 0 or ph > 14:
            return jsonify({"error": "pH must be between 0 and 14"}), 400
        if temperature < -10 or temperature > 50:
            return jsonify({"error": "Temperature must be between -10 and 50°C"}), 400
        if dissolved_oxygen < 0 or dissolved_oxygen > 50:
            return jsonify({"error": "Dissolved oxygen must be between 0 and 50 mg/L"}), 400
        if nitrate < 0 or nitrate > 5000:
            return jsonify({"error": "Nitrate must be between 0 and 5000 mg/L"}), 400
        
        # Get recommendations
        recommendations = recommender.recommend_plants(
            ph=ph,
            temperature=temperature,
            dissolved_oxygen=dissolved_oxygen,
            ammonia=ammonia,
            nitrate=nitrate
        )
        
        return jsonify(recommendations)
        
    except ValueError as e:
        return jsonify({"error": f"Invalid input: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

@app.route('/api/plants', methods=['GET'])
def get_all_plants():
    """Get all available plants in the database."""
    try:
        plants = recommender.get_all_plants()
        return jsonify(plants)
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "Aquafolia API"
    })

@app.route('/api/test-data', methods=['GET'])
def get_test_data():
    """
    Get a specific row of data from the CSV file for testing.
    Query parameter: row_index (0-based, defaults to 0 for first data row)
    Returns the specified data row (excluding header) from Iot_data_set.csv
    """
    try:
        csv_file = 'Iot_data_set.csv'
        if not os.path.exists(csv_file):
            return jsonify({"error": "CSV file not found"}), 404
        
        # Get row index from query parameter (default to 0)
        row_index = request.args.get('row_index', default=0, type=int)
        
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            
            if not rows:
                return jsonify({"error": "CSV file is empty"}), 404
            
            # Handle row index (loop back to beginning if exceeds)
            total_rows = len(rows)
            actual_index = row_index % total_rows
            
            selected_row = rows[actual_index]
            
            # Convert to proper format matching our API
            test_data = {
                "temperature": float(selected_row['Temperature(C)']),
                "dissolvedOxygen": float(selected_row['Dissolved Oxygen(g/ml)']),
                "pH": float(selected_row['PH']),
                "ammonia": float(selected_row['Ammonia(g/ml)']),
                "nitrate": float(selected_row['Nitrate(g/ml)']),
                "fishWeight": float(selected_row.get('Fish_Weight(g)', 0)),
                "rowIndex": actual_index,
                "totalRows": total_rows
            }
            
            return jsonify(test_data)
            
    except FileNotFoundError:
        return jsonify({"error": "CSV file not found"}), 404
    except KeyError as e:
        return jsonify({"error": f"Missing column in CSV: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": f"Invalid data format: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    print("🌿 Starting Aquafolia API Server...")
    print("📊 Plant Recommendation System Ready")
    print("🔗 Dashboard: http://localhost:5000")
    print("🔗 API: http://localhost:5000/api/recommend-plants")
    print("")
    app.run(debug=True, host='0.0.0.0', port=5000)
