import streamlit as st
from utils import columns, log_reg_model as model

import numpy as np
import pandas as pd

#Setting a title for the project and the user's input features
st.title('Discover Your Ideal Mobile Phone Price Class!')
battery_power = st.slider("Battery Power (mAh)", 500, 2000, step=1)
clock_speed = st.slider("Clock Speed (GHz)", 0.5, 3.0, step=0.1)
fc = st.slider("Front Camera (MP)", 0, 20, step=1)
int_memory = st.slider("Internal Memory (GB)", 2, 64, step=1)
m_depth = st.slider("Memory Depth (GB)", 0.1, 1.0, step=0.1)
mobile_wt = st.slider("Mobile Weight (g)", 80, 200, step=1)
n_cores = st.slider("Number of Cores", 1, 8, step=1)
pc = st.slider("Primary Camera (MP)", 1, 20, step=1)
px_height = st.slider("Pixel Resolution Height", 50, 2000, step=1)
px_width = st.slider("Pixel Resolution Width", 500, 2000, step=1)
ram = st.slider("RAM (MB)", 263, 3989, step=10)
sc_h = st.slider("Screen Height (cm)", 5, 19, step=1)
sc_w = st.slider("Screen Width (cm)", 1, 18, step=1)
talk_time = st.slider("Talk Time (hours)", 2, 20, step=1)

def get_message(predicted_class: int) -> str:
    """
    Returns a message to display for the user, input of the function is the model's price class prediction
    """
    messages = {
        0: "Lucky day, This phone is budget-friendly! 🌟",
        1: "Solid price for a solid choice! 👍",
        2: "Premium features at a competitive price! 🚀",
        3: "Top-tier flagship device!💲"
    }
    return messages[predicted_class]

def predict() -> None: 
    """
    Uses the user's input features to predict the phone's price class
    """
    row = np.array([battery_power, clock_speed, fc, int_memory, m_depth, mobile_wt,
                    n_cores, pc, px_height, px_width, ram, sc_h, sc_w, talk_time]) 
    X = pd.DataFrame([row], columns=columns)
    print(X)
    prediction = model.predict(X)[0]
    return prediction

trigger = st.button('Predict', on_click=predict)

if trigger:
    prediction_result = predict()
    st.success(get_message(prediction_result))