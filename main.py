"""
This is my Resume website that will use Streamlit and python
Bill Quain 2025
"""

import streamlit as st
import os

st.title("William Quain")
st.header("Who am I?")
st.write("""I am a Computer Scientist who graduated with a bachelors degree in computer science with a minor
            in cyber security from Western Illinois University. """)
st.image(os.path.join(os.getcwd(), "static", "BillWesternGrad.jpg"))
st.divider()
st.header("Skills")
st.write("""I know how to program in:""")
st.markdown("""
            - Python
            - C/C++
            - Java
""")
st.write("Some tools I am familiar with:")
st.markdown("""
            - Windows
            - Linux
            - Git/Github
            - Tensorflow
            - Pandas
            - Numpy
            - Matplotlib
            - PyGame
            - Streamlit
            - FreeCAD
            - Markdown
            - Microsoft Office 
            - GCC
            - Visual Studio
            - SQL databases 
            
""")
st.divider()
st.header("Experience")
st.write("""    In college I was Lead software engineer on our senior year software engineering capstone project. We made a 
            2D pixel art shooter called Tactical Chicken. You played as a chicken and shot turkeys and turned them into 
            turkey dinners. The most impressive part of the project was that we had to finish the project ahead of the 
            deadline of the other students in the class because my teammate had to leave for police academy, So I learned
            alot about time management.
                \nAt the same time I was also on two other development teams for senior year projects. One of those teams
            I was helping the lead developer in my computer networking class develop and test a chat application that 
            utilized network protocols to send text to other users. I provided knowledge of the Python language and Standards.
                \nThe third team I was on I helped design a SQL database for a databases course to demonstrate that we understood
            how to use Java and JDBC to communicate to an ORACLE database the school had setup.
                \nWorking on these teams simultaneously taught me that I really enjoy working with people on software projects.
            I also believe that my positive personality helped with team cohesion and made the experience for the other 
            students more enjoyable and fulfilling for everyone.  
            """)
st.write("""After college I decided to take a gap year to study other areas of computer science, mathematics, and electronics
            in order to fill the gaps that I wanted to fill. I spent most of 2023 studying Artificial Intelligence, Machine
            Learning, Deep learning, Calculus, and linear algebra. I spent 2024 taking courses and learning a vast array of different subjects
            like C and C++, computer organization and architecture, Python development, and many other skills that I wanted to have.""")

st.divider()
st.header("Screenshots of Tactical Chicken")
st.image(os.path.join(os.getcwd(), "static", "menu.png"))
st.image(os.path.join(os.getcwd(), "static", "gameplay.png"))