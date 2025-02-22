# app.py

import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Set page configuration
st.set_page_config(page_title="Data Collection Form", layout="centered")

# Add a title and description
st.title("Data Collection Form")
st.write("Please fill out the form below to submit your information.")

# Create form
with st.form("data_collection_form"):
    # Personal Information
    st.subheader("Personal Information")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    email = st.text_input("Email")
    
    # Additional Details
    st.subheader("Additional Details")
    age = st.number_input("Age", min_value=0, max_value=120)
    department = st.selectbox(
        "Department",
        ["Sales", "Marketing", "Engineering", "HR", "Other"]
    )
    experience = st.slider("Years of Experience", 0, 50, 5)
    
    # Comments
    comments = st.text_area("Additional Comments")
    
    # Submit button
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        # Create a dictionary with form data
        form_data = {
            "First Name": first_name,
            "Last Name": last_name,
            "Email": email,
            "Age": age,
            "Department": department,
            "Experience": experience,
            "Comments": comments,
            "Submission Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Convert to DataFrame
        df = pd.DataFrame([form_data])
        
        # Save to CSV
        if not os.path.exists("submissions.csv"):
            df.to_csv("submissions.csv", index=False)
        else:
            df.to_csv("submissions.csv", mode='a', header=False, index=False)
        
        st.success("Thank you! Your response has been recorded.")
        
# Display existing submissions
if os.path.exists("submissions.csv"):
    st.subheader("Previous Submissions")
    data = pd.read_csv("submissions.csv")
    st.dataframe(data)