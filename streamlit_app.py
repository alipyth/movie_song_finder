import streamlit as st
import databutton as db
import requests
from bs4 import BeautifulSoup
import json
st.title("Find Songs from movie Easy Peasy")

with st.form('find song'):
    query = st.text_input('your movie ?')
    submited = submited = st.form_submit_button("find")

    if submited:
        found = requests.get(f'https://www.tunefind.com/search/site?q={query}')
        soup = BeautifulSoup(found.text , 'html.parser')
        for i in soup.select('.tf-search-highlight'):
            high = i.text.replace(' ','-').replace('(','').replace(')','')
            st.title(f'i Found It :) - {high}')
            #movie = st.write(f"https://www.tunefind.com{i['href']}")
            r = requests.get(f'https://www.tunefind.com/api/frontend/movie/{high}?fields=song-events')
            y = json.loads(r.text)
            st.image(y['movie']['image']['src'])
            st.write('____________________')
            st.title(f"{y['movie']['songs_count']} Songs Found")
            st.write('____________________')
            sons_list = y['song_events']
            for music in sons_list:
                st.write(f"Name of Song : {music['song']['name']}")
                st.write(f"Album : {music['song']['album']}")
                st.write(f"Artist : {music['song']['artists'][0]['name']}")
                musics = music['song']['preview_url'] 
                st.audio(music['song']['preview_url'], format="audio/m4a", start_time=0)
                st.write('____________________')


        
        
st.write("By Ali Jahani - satreyek@gmail.com")
