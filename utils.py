import numpy as np
from PIL import Image
import cv2
import io

def preprocess_image(image, target_size=(224, 224)):
    """
    Preprocess the uploaded image to prepare it for the model.
    
    Args:
        image (PIL.Image): The uploaded image
        target_size (tuple): The target size for the model input
        
    Returns:
        numpy.ndarray: Preprocessed image array
    """
    try:
        # Convert PIL Image to numpy array
        if isinstance(image, Image.Image):
            img_array = np.array(image)
        else:
            # If image is already a numpy array
            img_array = image
            
        # Convert to RGB if it's in RGBA format
        if img_array.shape[-1] == 4:
            img_array = cv2.cvtColor(img_array, cv2.COLOR_RGBA2RGB)
        
        # Resize the image to the target size
        img_resized = cv2.resize(img_array, target_size)
        
        # Normalize pixel values to [0, 1]
        img_normalized = img_resized / 255.0
        
        return img_normalized
    
    except Exception as e:
        raise Exception(f"Image preprocessing failed: {str(e)}")

def extract_features(preprocessed_image):
    """
    Extract relevant features from the preprocessed image that might be useful
    for further analysis or display
    
    Args:
        preprocessed_image (numpy.ndarray): The preprocessed image
        
    Returns:
        dict: Dictionary of extracted features
    """
    try:
        # Convert to HSV for color analysis
        hsv_img = cv2.cvtColor((preprocessed_image * 255).astype(np.uint8), cv2.COLOR_RGB2HSV)
        
        # Calculate average hue, saturation, value
        avg_hue = np.mean(hsv_img[:, :, 0])
        avg_saturation = np.mean(hsv_img[:, :, 1])
        avg_value = np.mean(hsv_img[:, :, 2])
        
        # Calculate image features
        features = {
            'avg_hue': float(avg_hue),
            'avg_saturation': float(avg_saturation),
            'avg_brightness': float(avg_value),
            'dominant_color': get_dominant_color(preprocessed_image)
        }
        
        return features
    
    except Exception as e:
        raise Exception(f"Feature extraction failed: {str(e)}")

def get_dominant_color(image, k=3):
    """
    Extract dominant colors from the image using K-means clustering
    
    Args:
        image (numpy.ndarray): The preprocessed image
        k (int): Number of clusters (colors) to extract
        
    Returns:
        list: RGB values of dominant colors
    """
    # Reshape image to be a list of pixels
    pixels = (image * 255).astype(np.uint8)
    pixels = pixels.reshape(-1, 3)
    
    # Use a small sample for efficiency
    pixel_sample = pixels[np.random.choice(pixels.shape[0], size=1000, replace=False)]
    
    # Perform K-means clustering
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(
        pixel_sample.astype(np.float32), 
        k, 
        None, 
        criteria, 
        10, 
        cv2.KMEANS_RANDOM_CENTERS
    )
    
    # Convert back to uint8
    centers = centers.astype(np.uint8)
    
    # Count occurrences of each label
    counts = np.bincount(labels.flatten())
    
    # Get the most frequent color
    dominant_color = centers[np.argmax(counts)]
    
    # Convert to regular Python list
    return dominant_color.tolist()
