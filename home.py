# S5.1: Configure the home as directed above.
import streamlit as st

def app():
	st.header("Car Price Prediction App")
	st.text("""
            This web app allows a user to predict the prices of a car based on their
            engine size, horse power, dimensions and the drive wheel type parameters.
        	""")
	


# S6.1: Design the View Data page of the multipage app.
# Import necessary modules
import numpy as np
import pandas as pd
import streamlit as st

# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
    st.header("View Data")
    # Add an expander and display the dataset as a static table within the expander.
    with st.beta_expander("View Dataset"):
        st.table(car_df)