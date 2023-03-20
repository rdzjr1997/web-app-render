from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My webpage", page_icon=":tada:",layout="wide")

# Creating function to acces the json data of the animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200: # if the request is succesfull, it will return "200"
        return None
    return r.json()  # Returning the json data of the lottie animation

# Use local CSS
# Function to add the CSS changes
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


# --- LOAD ASSETS ---
lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_wnceyokk.json")
img_contact_form = Image.open("images/image.png")

# ---- Header Section ----
with st.container():  # Just to organize the code
    st.subheader("Hi, I am Francisco :wave:")
    st.title("A Mechanical Engineer From Brazil")
    st.write("I like to develop data analysis and write code for numerical analysis")
    st.write("[Learn More >](http://engfrancisco.com/)")

# ---- What I Do ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column: # Inserting text
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am a mechanical engineer that works in the area of maintenance including preventive and predictive.

            Also I am doing my master's degreee in the rotordynamics area, including simulation by the method of finite element for transient contact modelling.

            I am very passionate about the data and programming area, so I will work very hard with these things
            """
        )
    with right_column: # Inserting the animation
        st_lottie(lottie_coding, height=300, key="coding")

# --- PROJECTS ---
with st.container():
    st.write("---") # Line of division/Divider
    st.header("My Projects")
    st.write("##") # Space
    image_column, text_column = st.columns((1,2)) # The text column is twice the image column
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Following some tutorials for practice")
        st.write(
            """
            By now I am following some basic tutorials for practicing but I have experience with python and some libraries like numpy, pandas, scikit learn, matplotlib and some machine learning algorithm.
            """
        )
        st.markdown("Just a markdown")

# --- CONTACT
with st.container():
    st.write("---")
    st.header("Get In touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/francisco.mec.eng@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form> 
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

    






