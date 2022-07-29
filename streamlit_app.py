import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT * from fruit_load_list")
# my_data_rows = my_cur.fetchall()
# streamlit.dataframe(my_data_rows)
# streamlit.text(my_data_rows)

def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()
if streamlit.button('Get fruit load list') :
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
  
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
    return "Thanks for adding" + new_fruit
add_my_fruit =  streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list') :                  
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text( back_from_function )          
  
fruit_choice = streamlit.text_input('What fruit would you like to add?','Jackfruit')
#will fetch only first row
#my_data_row = my_cur.fetchone()
#will fetch all rows

streamlit.text("The fruit load list contains")
streamlit.header("The fruit load list contains:")


#streamlit.stop()

streamlit.title('My parents new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
                                                                                         
streamlit.dataframe(fruits_to_show)    


streamlit.header("Fruityvice Fruit Advice!")



#fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

def get_fruityvice_data(this_fruit_choice) :
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information:")
  else :
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + 'kiwi')
#streamlit.text(fruityvice_response.json())



#fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#streamlit.dataframe(fruityvice_normalized)
                                                                                         
#streamlit.dataframe(my_fruit_list)

