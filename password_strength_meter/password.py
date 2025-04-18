import re
import streamlit as st

#page styling
st.set_page_config(page_title="password strength checker By Nabeera Shahid ", page_icon="🔑", layout="centered")
#custom css
st.markdown("""
<style>   
    .main {text-align: center}
    .stTextInput {width:60% !important; margin: auto; }
    .stButton button {width:50%; background-color: blue; color: white; font-size: 18px; }
    stButton button:hover {background-color: red; color: white;}
    </style>"""
    , unsafe_allow_html=True)

#page title and description
st.title("🔒 Password Strength Generator")
st.write("Enter your password below to check its security level. 🔍")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ password should be  **at least 8 character long**.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):   
        score += 1
    else:
        feedback.append("❌ password should be  **both uppercase(A-Z) and lowercase(a-z) letter **.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ password should be  **atleast one number (0-9**.")

#special characters
    if re.search(r"[!@#$%^&*]", password):   
        score += 1
    else:
        feedback.append("❌ Include ** atleast one special character(!@#$%^&*)**. ")

#display password strength result
    if score == 4:
        st.success("**STRONG PASSWORD** - your password is secure.")
    elif score == 3:
        st.info("**Moderate PASSWORD** - Consider improving security by adding more feature.")
    else:
        st.error("**Weak PASSWORD** - Follow the suggestion below to strength it.")
    
#feedback
    if feedback:
        with st.expander("🔍 ** Improve Your password** "):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password: ",type= "password", help="Ensure your password is strong 🔐. ")

#Button working 
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password first!") # show warning if password empty

