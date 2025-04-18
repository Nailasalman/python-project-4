import re
import streamlit as st

# Page styling
st.set_page_config(page_title="Password Strength Meter Prepared by Naila Suleman", layout="centered")

# Custom CSS to style elements
st.markdown("""
    <style>
        .main {text-align: center;}
        .stTextInput {width: 60% !important; margin: auto;}
        .stButton button {width: 50%; background-color: blue; color: white; font-size: 18px;}
        .stButton button:hover {background-color: red; color: white;}
    </style>
""", unsafe_allow_html=True)

# Page title and description
st.title("Password Strength Meter")
st.write("Enter your password below to check its security level")

# Function to check password strength
def check_password_strength(password):
    score = 0 
    feedback = []

    if len(password) >= 8:
        score += 1  # Increase score by 1
    else:
        feedback.append("Password should be **at least 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1 
    else:
        feedback.append("Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should include **at least one number (0-9)**.")

    # Check for special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Password should include **at least one special character (!@#$%^&*)**.")

    # Display password strength result
    if score == 4:
        st.success("**Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("**Moderate Password** - Consider improving security by adding more features.")
    else: 
        st.error("**Weak Password** - Follow the suggestions below to strengthen it.")

        # Feedback to improve the password
        if feedback:
            with st.expander("**Improve Your Password**"):
                for item in feedback:
                    st.write(item)

# Password input
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong")

# Button action
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password first!")





