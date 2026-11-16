
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Fire Detection App", page_icon="🔥", layout="centered")

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("mobilenet_fire_model.h5")
    return model

with st.spinner("Loading model... Please wait! ⏳"):
    model = load_model()

st.title("🔥 Fire Detection System")
st.write("Upload an image below to check whether there is **Fire** or **Non_Fire**.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    st.write("Analyzing image...")
    
    img_resized = image.resize((224, 224))
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Prediction value (0 se 1 ke beech mein)
    prediction = model.predict(img_array)[0][0]
    
    st.markdown("---")
    
    # Logic for Clean Percentage Output
    if prediction > 0.5:
        confidence = prediction * 100
        st.error(f"⚠️ **FIRE Detected!** \n\n **Confidence:** {confidence:.1f}%")
    else:
        # No Fire ki confidence percentage nikalna
        confidence = (1 - prediction) * 100
        st.success(f"🟢 **NO FIRE Detected (Safe)** \n\n **Confidence:** {confidence:.1f}%")