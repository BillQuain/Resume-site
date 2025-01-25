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
            a lot about time management.
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

st.header("Tactical Chicken development story")
st.write("""
        Tactical Chicken was a capstone project for my CS491 and CS492 software engineering course. My team consisted of me
        and my good friend Tim Worthem. We were given total freedom by our professor to make any project we wanted as long as it
        was in a language he knew and we followed software engineering practices.
        \n I knew I wanted to make a game and I had heard of a simple game library called Pygame so I convinced Tim to work on a game with me for the project. 
        Challenges immediately sprung up as Tim didn't know Python ,so I had to teach him that, and neither of us had developed any kind of video game before. 
        However I was resourceful and found a heap of content online related to making all kinds of games with Python and Pygame.
        \nInitially the idea for Tactical Chicken was for it to be a side scroller like Mario or the old Duke Nukem games. However neither of us had 
        no idea how we would implement all of the things like projectiles, enemy AI, or map design. We eventually found tools so we could make our assets 
        like characters and the map. I had the idea of making the enemies turkeys and that when the 
        player shot the turkeys that their sprite would turn into a turkey dinner. I thought it was funny and it also made the game 
        more light hearted. 
        \nWe had some ambitious ideas for Tactical Chicken, but since I was also swamped with other classes and projects and 
        Tim was double majoring in law enforcement time forced us to make the decision of what got cut from the final game. More challenges arose at the 
        tail end of the project as I was sick and since Tim had to leave for Police academy we had to finish the project two weeks early! On the night we 
        finished the project I had a migraine so bad I thought I was going to throw up. However I powered through it and we compiled the final version of Tactical 
        Chicken and submitted it to our professor. When it came time to present I had to call in Tim over google meets so that he could also be part of the
        presentation. Our professor was very impressed with the simple enemy AI and my resourcefulness in using google meets to have Tim present as well. 
        I would argue we had the best project in the class in terms of technical achievements and challenges we faced 
        \n Looking back Tactical Chicken may not be the best game made with Pygame, but I learned so much during this project. 
        With having to finish the project early to having to learn entirely new technologies and 
        presenting my work to others. The experience I gained from doing this project was an important step in my journey as a computer scientist.
""")

st.header("Screenshots of Tactical Chicken")
st.image(os.path.join(os.getcwd(), "static", "menu.png"))
st.image(os.path.join(os.getcwd(), "static", "gameplay.png"))
