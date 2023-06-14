import streamlit as st
import requests
from bs4 import BeautifulSoup


def extract_xpath_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.select_one(".path-to-node").get("xpath")


def replace_coordinates_with_url(coordinates, url):
    lat, lon = coordinates.split(",")
    new_url = url.replace("-34.381413,21.421967", f"{lat},{lon}")
    return new_url


def main():
    st.title("Coordinate XPath Extractor")
    coordinates = st.text_input("Enter coordinates (e.g., -34.381413,21.421967)")
    enter_button = st.button("Enter")

    if enter_button and coordinates:
        original_url = "https://globalsolaratlas.info/detail?c=-34.381413,21.421967,11"
        new_url = replace_coordinates_with_url(coordinates, original_url)
        xpath = extract_xpath_from_url(new_url)
        st.table({"XPath": [xpath]})


if __name__ == "__main__":
    main()
