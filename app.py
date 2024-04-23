import streamlit as st
from streamlit_extras.colored_header import colored_header
import json


def load_data():
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def app():
    st.set_page_config(
        page_title="Smaki Globu")
    st.header(body="Smaki Globu", help="Odkryj smaki świata w jednym miejscu!", divider="gray")
    st.markdown("""
        <style>
            button p{
                font-weight: 700 !important;
            }
        </style>
    """, unsafe_allow_html=True)
    with st.container(border=True):
        st.caption("""
                <p style='font-weight: 600'>
                   Smaki Globu są jak magiczne bramy, które przenoszą nas w podróż po kulturach i tradycjach.
                   Odkryj z nami bogactwo kulinarnych doświadczeń, które skrywają się w każdym kęsie!
                </p>
            """, unsafe_allow_html=True)

    with st.container(border=True):
        for c, j in enumerate(load_data().values(), 0):
            with st.container(border=True):
                st.title(j.get("title"))
                tab1, tab2 = st.tabs(["Wstęp", "Więcej"])
                with tab1:
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"<p style='font-weight: 600'>{j.get('description')}</p>", unsafe_allow_html=True)
                    with col2:
                        img = j.get("img")
                        st.image(image=img["path"], caption=img["caption"].upper())
                with tab2:
                    st.write(j.get("info"))
                            
                        
                        
                # if st.button("Czytaj Więcej", type="secondary", key=c, use_container_width=True):
                #     st.switch_page("pages/american_cuisine.py")

if __name__ == "__main__":
    app()