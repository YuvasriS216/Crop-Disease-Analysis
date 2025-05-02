import streamlit as st
import numpy as np
from PIL import Image
import io
import matplotlib.pyplot as plt
from model import load_model, predict_deficiency
from utils import preprocess_image
from deficiency_info import get_deficiency_info

# Set page configuration
st.set_page_config(
    page_title="Wheat Leaf Nutrient Deficiency Predictor",
    page_icon="🌾",
    layout="wide"
)

# App title and description
st.title("Wheat Leaf Nutrient Deficiency Predictor")
st.markdown("""
This application helps identify nutrient deficiencies in wheat leaves from uploaded images.
Simply upload a clear photo of a wheat leaf, and the system will analyze it for potential deficiencies.
""")

# Create two columns for layout
col1, col2 = st.columns([1, 1])

# Initialize session state for storing results if not already initialized
if 'prediction_result' not in st.session_state:
    st.session_state.prediction_result = None
if 'confidence_scores' not in st.session_state:
    st.session_state.confidence_scores = None
if 'processed_image' not in st.session_state:
    st.session_state.processed_image = None
if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None

with col1:
    st.subheader("Upload Wheat Leaf Image")
    
    # File uploader for wheat leaf images
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Read and display the uploaded image
        image = Image.open(uploaded_file)
        st.session_state.uploaded_image = image
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Process button
        if st.button("Analyze Leaf"):
            # Show spinner during processing
            with st.spinner("Processing image and running analysis..."):
                try:
                    # Load the model
                    model = load_model()
                    
                    # Preprocess the image for the model
                    processed_img = preprocess_image(image)
                    st.session_state.processed_image = processed_img
                    
                    # Make prediction
                    prediction, confidence_scores = predict_deficiency(model, processed_img)
                    
                    # Store results in session state
                    st.session_state.prediction_result = prediction
                    st.session_state.confidence_scores = confidence_scores
                    
                    # Trigger a rerun to display results
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"An error occurred during analysis: {str(e)}")
    
    # Instructions
    with st.expander("How to use this tool"):
        st.markdown("""
        1. **Upload a clear image** of a wheat leaf showing symptoms
        2. Click the "Analyze Leaf" button
        3. Review the prediction results and information about the detected deficiency
        4. For best results, ensure:
           - The image is well-lit
           - The leaf is clearly visible
           - The image focuses on the affected area
        """)

with col2:
    st.subheader("Analysis Results")
    
    # Display results if available
    if st.session_state.prediction_result is not None:
        st.success(f"Predicted Deficiency: **{st.session_state.prediction_result}**")
        
        # Display confidence scores
        st.subheader("Confidence Scores")
        if st.session_state.confidence_scores:
            # Plot confidence scores
            fig, ax = plt.subplots(figsize=(10, 5))
            deficiencies = list(st.session_state.confidence_scores.keys())
            scores = list(st.session_state.confidence_scores.values())
            
            # Create horizontal bar chart
            ax.barh(deficiencies, scores, color='green')
            ax.set_xlim(0, 1.0)
            ax.set_xlabel('Confidence Score')
            ax.set_title('Prediction Confidence by Deficiency Type')
            
            # Display the plot
            st.pyplot(fig)
        
        # Display information about the detected deficiency
        st.subheader("Deficiency Information")
        deficiency_info = get_deficiency_info(st.session_state.prediction_result)
        
        # Display the information in an expandable container
        with st.expander("Symptoms and Treatment", expanded=True):
            st.markdown(f"### {deficiency_info['name']}")
            
            st.markdown("#### Symptoms")
            st.markdown(deficiency_info['symptoms'])
            
            st.markdown("#### Causes")
            st.markdown(deficiency_info['causes'])
            
            st.markdown("#### Treatment")
            st.markdown(deficiency_info['treatment'])
            
            if 'additional_info' in deficiency_info:
                st.markdown("#### Additional Information")
                st.markdown(deficiency_info['additional_info'])
    else:
        st.info("Upload an image and click 'Analyze Leaf' to see results here.")

# Add bottom section for app information
st.markdown("---")
st.markdown("""
### About This Tool
This application uses a machine learning model trained to identify common nutrient deficiencies in wheat leaves based on visual symptoms. 
The model analyzes patterns in leaf coloration, spots, and other visual indicators to identify potential deficiencies.

**Disclaimer**: While this tool provides guidance, it should be used as a supplementary diagnostic aid. For definitive diagnosis, 
consider soil and tissue testing by agricultural professionals.
""")
