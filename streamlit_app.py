import streamlit
streamlit.title("My Parents New Healthy Dinner")
streamlit.header ('Breakfast Menu')
streamlit.text ('😇Omega 3 & Blueberry Oatmeal')
streamlit.text ('😜Kale,Spinach and Rocket Smoothie')
streamlit.text ('😊Hard Boiled Free range Egg')

streamlit.header ('😰 Build your own smoothie')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamkit.dataframe('my_fruit_list)
