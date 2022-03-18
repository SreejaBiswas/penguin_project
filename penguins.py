import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
 
st.title("*Palmer's Penguins*") 
st.write('**Use this Streamlit app to make your own scatterplot about penguins!**') 
from PIL import Image
img = Image.open("pic.png")
st.image(img)

st.subheader("*Introduction to palmerpenguins*")
st.write("**The palmerpenguins R package contains two datasets that we believe are a viable alternative to Anderson’s Iris data (see datasets::iris). In this introductory vignette, we’ll highlight some of the properties of these datasets that make them useful for statistics and data science education, as well as software documentation and testing.**")

st.sidebar.write("***A short clip:***")
video_file = open('video.mp4', 'rb')
video_bytes = video_file.read()

st.sidebar.video(video_bytes)

st.sidebar.text("Photos..")
from PIL import Image
img = Image.open("pic2.png")
st.sidebar.image(img)


st.subheader("*Briefly description*")

if st.checkbox("About Palmer Penguins"):
  from PIL import Image
  img = Image.open("pic5.png")
  st.image(img)

st.subheader("*Meet the Palmer penguins*")
if st.checkbox("Show the photos of Palmer penguins!"):
  from PIL import Image
  img = Image.open("pic4.png")
  st.image(img)
st.subheader("*Bill dimensions*")
st.write("**The culmen is the upper ridge of a bird’s bill. In the simplified penguins data, culmen length and depth are renamed as variables bill_length_mm and bill_depth_mm to be more intuitiveFor this penguin data, the culmen (bill) length and depth are measured as shown below (thanks Kristen Gorman for clarifying!**")

if st.button("See it!"):

  from PIL import Image
  img = Image.open("pic7.png")
  st.image(img)
  
st.subheader("*Finally we are ready to show the Scatterplot of Palmer's penguin*")

selected_x_var = st.selectbox('What do want the x variable to be?', 
  ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']) 
selected_y_var = st.selectbox('What about the y?', 
  ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g']) 

 
penguin_file = st.file_uploader('Select Your Local Penguins CSV') 
if penguin_file is not None: 
	penguins_df = pd.read_csv(penguin_file) 
else: 
	st.stop()

sns.set_style('darkgrid')
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
fig, ax = plt.subplots() 
ax = sns.scatterplot(data = penguins_df, x = selected_x_var, 
  y = selected_y_var, hue = 'species', markers = markers,
  style = 'species') 
plt.xlabel(selected_x_var) 
plt.ylabel(selected_y_var) 
plt.title("Scatterplot of Palmer's Penguins") 
st.pyplot(fig) 


st.subheader("*Body parts*")
if st.checkbox("Do you want to see the body structure of penguins?"):
  from PIL import Image
  img = Image.open("pic6.png")
  st.image(img)

st.write("The majority of living penguin species have declining populations. According to the IUCN Red List, their conservation statuses range from Least Concern through to Endangered.")