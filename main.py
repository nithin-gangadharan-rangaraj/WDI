import streamlit as st

st.set_page_config(page_title="Internship")
st.subheader("Web Developer Intern", divider = 'red')

def display_job():
  st.write('''
  **Location:** Remote  
  **Type:** Project-based Internship
  
  **About Me:**
  I'm an AI graduate actively engaged in multiple innovative projects. I believe in the power of ideas 
  and their potential to create immense value. As I embark on this exciting journey to bring my new idea to life, 
  I am eager to provide students with the opportunity to gain hands-on experience and contribute 
  meaningfully to a real-world project.
  
  **Role Overview:**
  I am seeking a motivated and enthusiastic intern to assist in developing a comprehensive website. 
  This role is perfect for students looking to expand their skills in web development and gain valuable 
  experience working on a unique project. You will be responsible for creating a user-friendly website, 
  and integrating databases, and payment systems. Additionally, you should possess a professional mindset and 
  the capacity to work independently.
  
  **Key Responsibilities:**
  1. Develop and design a functional and aesthetically pleasing website.
  2. Ensure the website is responsive and accessible on various devices.
  3. Integrate database solutions to manage and store data efficiently.
  4. Set up and integrate secure payment systems.
  5. Collaborate with me to ensure the website aligns with the project's goals and vision.
  
  **Requirements:**
  1. Basic to intermediate experience in website development.
  2. Familiarity with database management and integration.
  3. Knowledge of payment gateway integration.
  4. Ability to work independently and manage your time effectively.
  5. Strong problem-solving skills and attention to detail.
  6. A professional attitude and capacity to think creatively.
  
  **Preferred Qualifications:**
  Students with high curiosity and someone who is willing to do this project wholeheartedly is preferred. 
  I believe that interests can elevate one's qualifications. Of course, basic knowledge on achieving the goal 
  is ideal, however, the intern's interest towards the project matters the most.
  
  **How to Apply:**
  If you are passionate about web development and eager to gain hands-on experience, please send your resume, 
  a brief cover letter, and any relevant work samples or portfolio.
  
  I'm excited to work with someone who is as enthusiastic about this project as I am. Let's create something amazing together!
  ''')

  st.subheader('Intructions on how to apply:', divider = 'red')
  st.write('''
    Please send all your details and relevant attachments to **teamcandidate.ai@gmail.com**. <br>
    You MUST have this, "**GR_Web_developer_intern**" as your E-mail Subject. Please quote it exactly.
  ''')

if __name__ == "__main__":
  display_job()
