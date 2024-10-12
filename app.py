import streamlit as st
import boto3
from boto3.dynamodb.conditions import Attr

AWS_REGION = "us-east-1"
dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table("Spara")

def data_saving(innehåll,titel,vecka_num,dag,tid_stampel):
    table.put_item(
        Item={
            'innehåll': innehåll,
            'titel': titel,
            'vecka_num': vecka_num,
            'dag': dag,
            'tid_stampel': tid_stampel
        }
    )

st.title("Min Dagbok.")
titel = st.text_input("",placeholder="Lägg in en titel")
innehåll = st.text_area("",placeholder="Dokumentera i dagboksinlägget här")
spara = st.button("Spara inlägg.")

st.title("Välj vecka, dag och tid.")
vecka_num = st.selectbox('Vecka',['41','42','43','44','45','46','47','48'])
dag = st.selectbox('Dag',['måndag','tisdag','onsdag','torsdag','fredag'])
tid_stampel = st.selectbox('Tid',['9:00-11:00','11:00-14:00'])

if spara:
    if not titel and innehåll:
        st.error("Lägg in en titel och skriv något")
    else:
        data_saving(innehåll,titel,vecka_num,dag,tid_stampel)
        st.success("Ditt inlägg har nu sparats.")

if not items:
   st.info(f"No saved documents found for this week.") # will show if it exists in the data or not for the specific week

else: # Then here is what it would show when we save
   with st.container(border=True,height=200):
    for item in items:
        st.write(f"**titel:** {item['titel']}")
        st.write("------------------------------")
        st.write(f"**innehåll:** {item['innehåll']}")
        st.write("------------------------------")
        st.write(f"**vecka_num:** {item['vecka_num']}")
        st.write("------------------------------")
        st.write(f"**dag:** {item['dag']}")
        st.write("------------------------------")
        st.write(f"**tid_stampel:** {item['tid_stampel']}")
        st.write("------------------------------")
