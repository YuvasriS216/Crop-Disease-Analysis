import numpy as np
import cv2
from utils import extract_features

# Dictionary mapping class indices to deficiency names
DEFICIENCY_CLASSES = {
    0: "Healthy",
    1: "Nitrogen Deficiency",
    2: "Phosphorus Deficiency",
    3: "Potassium Deficiency",
    4: "Sulfur Deficiency",
    5: "Iron Deficiency",
    6: "Zinc Deficiency", 
    7: "Manganese Deficiency",
    8: "Boron Deficiency",
    9: "Copper Deficiency"
}

class SimpleColorAnalyzer:
    """A simple model that performs analysis based on color features of the image."""
    
    def __init__(self):
        self.deficiency_color_profiles = {
            # HSV color profiles (approximate values) for different deficiencies
            "Healthy": {'hue_range': (35, 85), 'saturation_min': 0.4, 'value_min': 0.4},
            "Nitrogen Deficiency": {'hue_range': (20, 40), 'saturation_min': 0.3, 'value_min': 0.6},
            "Phosphorus Deficiency": {'hue_range': (250, 350), 'saturation_min': 0.2, 'value_min': 0.3},
            "Potassium Deficiency": {'hue_range': (0, 30), 'saturation_min': 0.4, 'value_min': 0.4},
            "Sulfur Deficiency": {'hue_range': (30, 60), 'saturation_min': 0.3, 'value_min': 0.6},
            "Iron Deficiency": {'hue_range': (30, 65), 'saturation_min': 0.2, 'value_min': 0.7},
            "Zinc Deficiency": {'hue_range': (50, 80), 'saturation_min': 0.3, 'value_min': 0.5},
            "Manganese Deficiency": {'hue_range': (30, 70), 'saturation_min': 0.3, 'value_min': 0.4},
            "Boron Deficiency": {'hue_range': (20, 50), 'saturation_min': 0.4, 'value_min': 0.3},
            "Copper Deficiency": {'hue_range': (40, 70), 'saturation_min': 0.4, 'value_min': 0.5}
        }
    
    def predict(self, image):
        """Predict deficiency based on color analysis"""
        # Calculate HSV features from the image
        features = extract_features(image)
        
        # Get the HSV values
        h, s, v = features['avg_hue'], features['avg_saturation'], features['avg_brightness']
        
        # Calculate scores for each deficiency based on color profile match
        scores = {}
        for deficiency, profile in self.deficiency_color_profiles.items():
            # Check if hue is in range (handle wrapping around 360 degrees)
            hue_min, hue_max = profile['hue_range']
            if hue_min <= hue_max:
                hue_match = hue_min <= h <= hue_max
            else:
                hue_match = h >= hue_min or h <= hue_max
            
            # Check saturation and value thresholds
            sat_match = s >= profile['saturation_min']
            val_match = v >= profile['value_min']
            
            # Calculate a match score (basic version)
            if hue_match and sat_match and val_match:
                # Higher score if all criteria match
                scores[deficiency] = 0.7 + (0.3 * np.random.random())
            elif hue_match:
                # Medium score if hue matches
                scores[deficiency] = 0.4 + (0.3 * np.random.random())
            else:
                # Low score for non-matches
                scores[deficiency] = 0.1 + (0.2 * np.random.random())
        
        # Normalize scores to sum to 1.0 (to act like probabilities)
        total = sum(scores.values())
        normalized_scores = {k: v/total for k, v in scores.items()}
        
        # Sort by score (descending)
        sorted_scores = {k: v for k, v in sorted(
            normalized_scores.items(), 
            key=lambda item: item[1], 
            reverse=True
        )}
        
        # Return top prediction and all scores
        top_deficiency = list(sorted_scores.keys())[0]
        return top_deficiency, sorted_scores


def load_model():
    """
    Load a simple color-based model for wheat leaf nutrient deficiency detection.
    
    Returns:
        SimpleColorAnalyzer: A model that analyzes color patterns
    """
    try:
        # Create the simple analyzer model
        model = SimpleColorAnalyzer()
        return model
    
    except Exception as e:
        raise Exception(f"Failed to initialize model: {str(e)}")


def predict_deficiency(model, preprocessed_image):
    """
    Predict nutrient deficiency from a preprocessed image
    
    Args:
        model: The loaded model
        preprocessed_image: Image array preprocessed for the model
        
    Returns:
        tuple: (predicted_deficiency_name, confidence_scores_dict)
    """
    try:
        # Make prediction using the simple model
        predicted_deficiency, confidence_scores = model.predict(preprocessed_image)
        
        return predicted_deficiency, confidence_scores
    
    except Exception as e:
        raise Exception(f"Prediction failed: {str(e)}")
