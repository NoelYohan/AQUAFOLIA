# 🌿 AQUAFOLIA - Smart Aquaponics Dashboard with AI Plant Recommendations

A comprehensive water quality monitoring system with AI-powered plant recommendations for aquaponics. This project detects water quality parameters (pH, temperature, dissolved oxygen, ammonia) and uses intelligent analytics to predict which plants are suitable to grow in your aquaponic system.

## ✨ Features

- **Real-time Water Quality Monitoring**: Track pH, temperature, dissolved oxygen, and ammonia levels
- **AI-Powered Plant Recommendations**: Get intelligent suggestions for plants based on current water conditions
- **Interactive Dashboard**: Beautiful, modern UI with real-time charts and data visualization
- **Raspberry Pi Integration**: Designed to work with Raspberry Pi sensors
- **Match Scoring System**: Each plant recommendation includes a compatibility score (0-100%)
- **Comprehensive Plant Database**: 15+ plants with detailed water quality requirements

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Web browser (Chrome, Firefox, Edge, etc.)
- (Optional) Raspberry Pi with sensors for real data collection

### Installation

1. **Clone or download this repository**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the backend server**:
   ```bash
   python app.py
   ```
   The API will run on `http://localhost:5000`

4. **Open the frontend**:
   - Open `index.html` in your web browser
   - Or use a local web server:
     ```bash
     # Python 3
     python -m http.server 8000
     # Then open http://localhost:8000
     ```

## 📊 How It Works

### Water Quality Parameters

The system monitors four key parameters:

1. **pH Level** (0-14): Acidity/alkalinity of water
2. **Temperature** (°C): Water temperature
3. **Dissolved Oxygen** (mg/L): Amount of oxygen in water
4. **Ammonia** (mg/L): Toxic compound level (lower is better)

### AI Recommendation Algorithm

The plant recommendation system uses a weighted scoring algorithm:

- **pH Match** (35% weight): How well the current pH matches plant requirements
- **Temperature Match** (30% weight): Compatibility with plant temperature needs
- **Dissolved Oxygen Match** (25% weight): Sufficiency of oxygen levels
- **Ammonia Safety** (10% weight): Low ammonia levels are critical

Each plant receives a match score (0-100%) indicating how suitable it is for your current water conditions.

### Plant Database

The system includes 15+ plants commonly grown in aquaponics:

- **Leafy Greens**: Lettuce, Spinach, Kale, Swiss Chard, Arugula, Pak Choi
- **Herbs**: Basil, Mint, Cilantro
- **Fruit Vegetables**: Tomato, Cucumber, Pepper
- **Fruits**: Strawberry
- **Legumes**: Beans
- **Aquatic Plants**: Watercress

Each plant has specific requirements for pH, temperature, dissolved oxygen, and maximum ammonia tolerance.

## 🎯 Usage

### Getting Plant Recommendations

1. **Monitor Water Quality**: The dashboard displays real-time sensor data
2. **Click "Get Recommendations"**: The AI analyzes current conditions
3. **View Results**: See plants ranked by compatibility score
   - **High Match** (80-100%): Excellent conditions for this plant
   - **Medium Match** (60-79%): Good conditions, may need minor adjustments
   - **Low Match** (<60%): Conditions not ideal, significant adjustments needed

### API Endpoints

#### Get Plant Recommendations
```http
POST /api/recommend-plants
Content-Type: application/json

{
    "pH": 6.5,
    "temperature": 20,
    "dissolvedOxygen": 6.5,
    "ammonia": 0.3
}
```

Response:
```json
[
    {
        "name": "Lettuce",
        "type": "Leafy Green",
        "match_score": 92.5,
        "ph_min": 6.0,
        "ph_max": 7.0,
        "temp_min": 15,
        "temp_max": 20,
        "do_min": 5.0,
        "do_max": 8.0,
        "description": "..."
    },
    ...
]
```

#### Get All Plants
```http
GET /api/plants
```

## 🔧 Configuration

### Connecting Real Sensors

To connect actual Raspberry Pi sensors:

1. **Modify `index.html`**: Replace the `simulateRealTimeData()` function with actual sensor readings
2. **Create Sensor Interface**: Write Python code to read from your sensors
3. **Update API**: Modify the backend to accept real-time sensor data

Example sensor reading function:
```python
def read_sensors():
    # Your sensor reading code here
    return {
        "pH": read_ph_sensor(),
        "temperature": read_temp_sensor(),
        "dissolvedOxygen": read_do_sensor(),
        "ammonia": read_ammonia_sensor()
    }
```

### Adding Custom Plants

Edit `plants_database.json` to add your own plants:

```json
{
    "name": "Your Plant",
    "type": "Category",
    "ph_min": 6.0,
    "ph_max": 7.0,
    "temp_min": 15,
    "temp_max": 25,
    "do_min": 5.0,
    "do_max": 8.0,
    "ammonia_max": 0.5,
    "description": "Description of your plant"
}
```

## 📁 Project Structure

```
Aquafolia/
├── index.html              # Frontend dashboard
├── app.py                  # Flask backend API
├── plant_recommender.py    # AI recommendation engine
├── plants_database.json    # Plant database
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## 🧪 Testing

### Test the API

```bash
# Test health endpoint
curl http://localhost:5000/api/health

# Test plant recommendations
curl -X POST http://localhost:5000/api/recommend-plants \
  -H "Content-Type: application/json" \
  -d '{"pH": 6.5, "temperature": 20, "dissolvedOxygen": 6.5, "ammonia": 0.3}'
```

## 🎨 Customization

### Styling

The dashboard uses inline CSS. To customize:
- Modify the `<style>` section in `index.html`
- Colors, fonts, and layouts can be easily adjusted

### Algorithm Tuning

Edit `plant_recommender.py` to adjust:
- Weight distribution for scoring
- Match score calculation logic
- Minimum score thresholds

## 🔮 Future Enhancements

- Machine learning model training on historical data
- Integration with weather APIs for climate predictions
- Mobile app version
- Alert system for critical water quality issues
- Historical data analysis and trends
- Multi-zone support for different growing areas

## 📝 License

This project is open source and available for educational and commercial use.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add more plants to the database
- Improve the recommendation algorithm
- Enhance the UI/UX
- Add new features

## 📧 Support

For issues or questions, please open an issue in the repository.

---

**Built with ❤️ for sustainable aquaponics farming**
