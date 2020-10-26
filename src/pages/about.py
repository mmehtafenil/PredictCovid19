import streamlit as st
import base64
from PIL import Image
import streamlit.components.v1 as components



def main():

    st.sidebar.title("About")
    # render_md("resources/README.md")
    st.sidebar.info("Please let us know what do you think about it!")



    st.markdown('![GitHub top language](https://img.shields.io/github/languages/top/tuminzee/PredictCovid?style=for-the-badge)  [![Github Repo](https://img.shields.io/badge/GitHub-Repo-green?style=for-the-badge&logo=appveyor)](https://github.com/tuminzee/PredictCovid) ![GitHub contributors](https://img.shields.io/github/contributors/tuminzee/PredictCovid?style=for-the-badge) ![GitHub forks](https://img.shields.io/github/forks/tuminzee/PredictCovid?label=Fork&style=for-the-badge)')
    
    
    st.subheader("Meet Our Team")
    nav = st.radio("🚀🚀🚀",["Fenil Mehta","Krunal Vasoya","Tumin Sheth"])
    if nav == "Fenil Mehta":
        st.subheader("Fenil Mehta")
        st.markdown('[**LinkedIn**](https://www.linkedin.com/in/fenilmehta/), [GitHub](https://github.com/mmehtafenil) ')


        image = Image.open('profile/fenil.jpg')
        st.image(image, width=400, use_column_width=True)
        CSS = """
        h1 {
            color: red;
        }
        """
        st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


    if nav == "Krunal Vasoya":
        st.subheader("Krunal Vasoya")    
        st.markdown('[**LinkedIn**](https://www.linkedin.com/in/krunal-vasoya-29a3691b5), [Github](https://github.com/krunal310) ')
        image = Image.open('profile/kunal.jpg')
        st.image(image, width=400, use_column_width=True)
        CSS = """
        h1 {
            color: orange;
        }
        """
        st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

    if nav == "Tumin Sheth":
        st.subheader("Tumin Sheth")
        st.markdown('[**LinkedIn**](https://www.linkedin.com/in/tumin-sheth/), [Github](upload://7FxfXwDqJIZdYJ2QYADywvNRjB.png) ')
        image = Image.open('profile/tumin.jpg')
        st.image(image, width=400, use_column_width=True)


if __name__ == "__main__":
    main()
