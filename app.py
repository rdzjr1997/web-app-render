from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="EngFrancisco", page_icon=":coffee:",layout="wide")

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
    st.write("I enjoy to develop code for data and numerical analysis")

# ---- What I Do ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column: # Inserting text
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am a mechanical engineer currently working in the steel industry in the areas of mechanical design and maintenance, but who as a passion by data analysis and programming in general.

            In addition, I am doing a master's degree at UFRJ in the area of rotordynamics including the creation of a numerical code for modeling the transient response during rotor-stator contact by the finite element method.

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
        st.subheader("My Mechanical Engineering Blog")
        st.write(
            """
            I created a blog for write about mechanical engineering during my master degree studies.
            This is something I pretend to continuously update. So, [keep an eye">](http://engfrancisco.com/)
            """
        )

    st.write("##") # Space
    image_column, text_column = st.columns((1,2)) # The text column is twice the image column
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Exploratory Data Analysis (EDA)")
        st.write(
            """
            The Exploraroty Data Analysis is very important to get insights about the data. in this project I made and EDA of the Top 50 Spotify Songs - 2019.

            Enjoy
            """
        )

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

    






