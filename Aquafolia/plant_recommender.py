import json
import os
from typing import List, Dict
import numpy as np

class PlantRecommender:
    """
    AI-powered plant recommendation system based on water quality parameters.
    Uses a scoring algorithm to match plants with current water conditions.
    """
    
    def __init__(self, plants_file='plants_database.json'):
        """Initialize the recommender with plant database."""
        self.plants_file = plants_file
        self.plants = self._load_plants()
    
    def _load_plants(self) -> List[Dict]:
        """Load plants from JSON database."""
        if os.path.exists(self.plants_file):
            with open(self.plants_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # Return default plants if file doesn't exist
            return self._get_default_plants()
    
    def _get_default_plants(self) -> List[Dict]:
        """Default plant database with water quality requirements."""
        return [
            {
                "name": "Lettuce",
                "type": "Leafy Green",
                "ph_min": 6.0,
                "ph_max": 7.0,
                "temp_min": 15,
                "temp_max": 20,
                "do_min": 5.0,
                "do_max": 8.0,
                "ammonia_max": 0.5,
                "nitrate_min": 50,
                "nitrate_max": 400,
                "description": "Fast-growing leafy green, perfect for aquaponics. High yield and nutrient-rich."
            },
            {
                "name": "Basil",
                "type": "Herb",
                "ph_min": 5.5,
                "ph_max": 6.5,
                "temp_min": 18,
                "temp_max": 25,
                "do_min": 4.0,
                "do_max": 7.0,
                "ammonia_max": 0.5,
                "nitrate_min": 50,
                "nitrate_max": 400,
                "description": "Aromatic herb that thrives in warm conditions. Great for culinary use."
            },
            {
                "name": "Tomato",
                "type": "Fruit Vegetable",
                "ph_min": 5.5,
                "ph_max": 6.5,
                "temp_min": 18,
                "temp_max": 24,
                "do_min": 6.0,
                "do_max": 8.0,
                "ammonia_max": 0.5,
                "nitrate_min": 100,
                "nitrate_max": 300,
                "description": "Popular aquaponic crop. Requires good oxygen levels and stable pH."
            },
            {
                "name": "Cucumber",
                "type": "Fruit Vegetable",
                "ph_min": 5.5,
                "ph_max": 6.5,
                "temp_min": 20,
                "temp_max": 25,
                "do_min": 5.0,
                "do_max": 7.0,
                "ammonia_max": 0.5,
                "nitrate_min": 100,
                "nitrate_max": 300,
                "description": "Fast-growing vine crop. Needs warm temperatures and good water quality."
            },
            {
                "name": "Spinach",
                "type": "Leafy Green",
                "ph_min": 6.0,
                "ph_max": 7.5,
                "temp_min": 10,
                "temp_max": 20,
                "do_min": 4.0,
                "do_max": 6.0,
                "ammonia_max": 0.5,
                "nitrate_min": 50,
                "nitrate_max": 400,
                "description": "Cold-tolerant leafy green. Rich in iron and vitamins."
            },
            {
                "name": "Kale",
                "type": "Leafy Green",
                "ph_min": 6.0,
                "ph_max": 7.5,
                "temp_min": 8,
                "temp_max": 22,
                "do_min": 4.0,
                "do_max": 7.0,
                "ammonia_max": 0.5,
                "nitrate_min": 50,
                "nitrate_max": 400,
                "description": "Superfood green. Very cold-tolerant and nutrient-dense."
            },
            {
                "name": "Pepper",
                "type": "Fruit Vegetable",
                "ph_min": 5.5,
                "ph_max": 6.5,
                "temp_min": 20,
                "temp_max": 26,
                "do_min": 5.0,
                "do_max": 8.0,
                "ammonia_max": 0.5,
                "nitrate_min": 100,
                "nitrate_max": 300,
                "description": "Warm-season crop. Requires consistent warm temperatures."
            },
            {
                "name": "Mint",
                "type": "Herb",
                "ph_min": 6.0,
                "ph_max": 7.0,
                "temp_min": 15,
                "temp_max": 22,
                "do_min": 4.0,
                "do_max": 6.0,
                "ammonia_max": 0.5,
                "nitrate_min": 50,
                "nitrate_max": 400,
                "description": "Hardy herb that grows well in aquaponics. Spreads quickly."
            },
            {
                "name": "Swiss Chard",
                "type": "Leafy Green",
                "ph_min": 6.0,
                "ph_max": 7.0,
                "temp_min": 10,
                "temp_max": 24,
                "do_min": 4.0,
                "do_max": 7.0,
                "ammonia_max": 0.5,
                "nitrate_min": 50,
                "nitrate_max": 400,
                "description": "Colorful and nutritious. Tolerates a wide temperature range."
            },
            {
                "name": "Cilantro",
                "type": "Herb",
                "ph_min": 6.0,
                "ph_max": 7.0,
                "temp_min": 10,
                "temp_max": 20,
                "do_min": 4.0,
                "do_max": 6.0,
                "ammonia_max": 0.5,
                "nitrate_min": 50,
                "nitrate_max": 400,
                "description": "Cool-season herb. Best grown in cooler temperatures."
            },
            {
                "name": "Arugula",
                "type": "Leafy Green",
                "ph_min": 6.0,
                "ph_max": 7.0,
                "temp_min": 10,
                "temp_max": 20,
                "do_min": 4.0,
                "do_max": 6.0,
                "ammonia_max": 0.5,
                "nitrate_min": 50,
                "nitrate_max": 400,
                "description": "Peppery leafy green. Fast-growing and cold-tolerant."
            },
            {
                "name": "Strawberry",
                "type": "Fruit",
                "ph_min": 5.5,
                "ph_max": 6.5,
                "temp_min": 15,
                "temp_max": 22,
                "do_min": 5.0,
                "do_max": 7.0,
                "ammonia_max": 0.5,
                "nitrate_min": 100,
                "nitrate_max": 300,
                "description": "Sweet fruit crop. Requires careful pH and temperature management."
            },
            {
                "name": "Watercress",
                "type": "Aquatic Plant",
                "ph_min": 6.0,
                "ph_max": 7.5,
                "temp_min": 10,
                "temp_max": 18,
                "do_min": 6.0,
                "do_max": 8.0,
                "ammonia_max": 0.5,
                "nitrate_min": 50,
                "nitrate_max": 400,
                "description": "Aquatic plant that loves high oxygen. Very nutritious."
            },
            {
                "name": "Pak Choi",
                "type": "Leafy Green",
                "ph_min": 6.0,
                "ph_max": 7.0,
                "temp_min": 12,
                "temp_max": 22,
                "do_min": 4.0,
                "do_max": 7.0,
                "ammonia_max": 0.5,
                "nitrate_min": 50,
                "nitrate_max": 400,
                "description": "Asian leafy green. Fast-growing and versatile in cooking."
            },
            {
                "name": "Beans",
                "type": "Legume",
                "ph_min": 6.0,
                "ph_max": 7.0,
                "temp_min": 18,
                "temp_max": 24,
                "do_min": 5.0,
                "do_max": 7.0,
                "ammonia_max": 0.5,
                "nitrate_min": 50,
                "nitrate_max": 400,
                "description": "Nitrogen-fixing legume. Good for aquaponic systems."
            }
        ]
    
    def _calculate_match_score(self, plant: Dict, ph: float, temp: float, 
                              do: float, ammonia: float = 0.0, nitrate: float = 0.0) -> float:
        """
        Calculate compatibility score (0-100) for a plant based on water quality.
        Uses weighted scoring algorithm.
        """
        score = 0.0
        weights = {'ph': 0.25, 'temp': 0.25, 'do': 0.20, 'ammonia': 0.10, 'nitrate': 0.20}
        
        # pH scoring (0-35 points)
        ph_score = 0
        if plant['ph_min'] <= ph <= plant['ph_max']:
            ph_score = weights['ph'] * 100  # Perfect match
        else:
            ph_range = plant['ph_max'] - plant['ph_min']
            ph_center = (plant['ph_min'] + plant['ph_max']) / 2
            distance = abs(ph - ph_center)
            if distance <= ph_range:
                ph_score = weights['ph'] * 100 * (1 - distance / ph_range)
            else:
                ph_score = max(0, weights['ph'] * 100 * (1 - distance / ph_range * 2))
        
        # Temperature scoring (0-30 points)
        temp_score = 0
        if plant['temp_min'] <= temp <= plant['temp_max']:
            temp_score = weights['temp'] * 100  # Perfect match
        else:
            temp_range = plant['temp_max'] - plant['temp_min']
            temp_center = (plant['temp_min'] + plant['temp_max']) / 2
            distance = abs(temp - temp_center)
            if distance <= temp_range:
                temp_score = weights['temp'] * 100 * (1 - distance / temp_range)
            else:
                temp_score = max(0, weights['temp'] * 100 * (1 - distance / temp_range * 2))
        
        # Dissolved Oxygen scoring (0-25 points)
        do_score = 0
        if plant['do_min'] <= do <= plant['do_max']:
            do_score = weights['do'] * 100  # Perfect match
        else:
            do_range = plant['do_max'] - plant['do_min']
            do_center = (plant['do_min'] + plant['do_max']) / 2
            distance = abs(do - do_center)
            if distance <= do_range:
                do_score = weights['do'] * 100 * (1 - distance / do_range)
            else:
                do_score = max(0, weights['do'] * 100 * (1 - distance / do_range * 2))
        
        # Ammonia scoring (0-10 points) - lower is better
        ammonia_score = 0
        if ammonia <= plant.get('ammonia_max', 0.5):
            ammonia_score = weights['ammonia'] * 100
        else:
            # Penalize high ammonia
            excess = ammonia - plant.get('ammonia_max', 0.5)
            ammonia_score = max(0, weights['ammonia'] * 100 * (1 - excess * 2))
        
        # Nitrate scoring (0-20 points)
        nitrate_score = 0
        nitrate_min = plant.get('nitrate_min', 50)
        nitrate_max = plant.get('nitrate_max', 400)
        if nitrate_min <= nitrate <= nitrate_max:
            nitrate_score = weights['nitrate'] * 100  # Perfect match
        else:
            nitrate_range = nitrate_max - nitrate_min
            nitrate_center = (nitrate_min + nitrate_max) / 2
            distance = abs(nitrate - nitrate_center)
            if distance <= nitrate_range:
                nitrate_score = weights['nitrate'] * 100 * (1 - distance / nitrate_range)
            else:
                nitrate_score = max(0, weights['nitrate'] * 100 * (1 - distance / nitrate_range * 2))
        
        total_score = ph_score + temp_score + do_score + ammonia_score + nitrate_score
        
        # Bonus for plants that match all parameters perfectly
        if (plant['ph_min'] <= ph <= plant['ph_max'] and
            plant['temp_min'] <= temp <= plant['temp_max'] and
            plant['do_min'] <= do <= plant['do_max'] and
            ammonia <= plant.get('ammonia_max', 0.5) and
            nitrate_min <= nitrate <= nitrate_max):
            total_score = min(100, total_score + 5)  # Small bonus
        
        return round(total_score, 2)
    
    def recommend_plants(self, ph: float, temperature: float, 
                         dissolved_oxygen: float, ammonia: float = 0.0,
                         nitrate: float = 0.0, top_n: int = 10) -> List[Dict]:
        """
        Get plant recommendations based on water quality parameters.
        
        Args:
            ph: pH level (0-14)
            temperature: Temperature in Celsius
            dissolved_oxygen: Dissolved oxygen in mg/L
            ammonia: Ammonia level in mg/L (optional)
            nitrate: Nitrate level in mg/L (optional)
            top_n: Number of top recommendations to return
        
        Returns:
            List of recommended plants with match scores
        """
        recommendations = []
        
        for plant in self.plants:
            match_score = self._calculate_match_score(
                plant, ph, temperature, dissolved_oxygen, ammonia, nitrate
            )
            
            # Only include plants with score > 0
            if match_score > 0:
                recommendation = plant.copy()
                recommendation['match_score'] = match_score
                recommendations.append(recommendation)
        
        # Sort by match score (descending)
        recommendations.sort(key=lambda x: x['match_score'], reverse=True)
        
        # Return top N recommendations
        return recommendations[:top_n]
    
    def get_all_plants(self) -> List[Dict]:
        """Get all plants in the database."""
        return self.plants
