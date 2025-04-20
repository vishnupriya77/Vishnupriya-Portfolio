import streamlit as st
from PIL import Image
import base64
import streamlit.components.v1 as components
from question_set import var # type: ignore
from predefined_answers import predefined_response, all_projects, all_certifications, all_qualifications, all_experience  # type: ignore
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def main():
    st.set_page_config(page_title="Vishnupriya's Portfolio", layout="wide")

    # Custom CSS
    custom_css = """
    <style>
    body {
        background-color: #121212;
        color: white;
    }
    .stTabs [data-baseweb="tab-list"] {
        display: flex;
        justify-content: space-evenly;
        border-bottom: 2px solid #4a4a4a;
        padding: 10px 0;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #333;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        margin: 0 5px;
        font-weight: bold;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #444;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff4b4b !important;
    }

    .profile-pic {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 50%;
        width: 200px;
        height: 200px;
        object-fit: cover;
        border: 3px solid #666;
    }
    .center-text {
        text-align: center;
    }
    .role-tag-expanded {
        background-color: #2c2c2c;
        color: #bbb;
        padding: 6px 16px;
        border-radius: 30px;
        font-size: 15px;
        display: block;
        width: 160px;
        text-align: center;
        margin-left: auto;
        margin-right: auto;
        transform: translateX(-8px);  /* move slightly left */
    }



    }
    .info-wrapper {
        margin-top: 30px;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        padding-left: 30px;
    }
    .info-block {
        display: flex;
        align-items: flex-start;
        margin-bottom: 12px;
    }
    .info-icon {
        width: 22px;
        height: 22px;
        margin-right: 12px;
        filter: brightness(0) invert(1);
    }
    .info-text {
        line-height: 1.4;
    }
    .info-label {
        font-size: 13px;
        color: #888;
        font-weight: 600;
    }
    .info-value {
        font-size: 15px;
        color: white;
    }
    .social-icons {
        display: flex;
        justify-content: flex-start;
        gap: 16px;
        margin-top: 20px;
        padding-left: 30px;
    }
    .social-icons img {
        width: 28px;
        filter: brightness(0) invert(1);
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 3], gap="large")

    with col1:
        name_section = f'''
        <div class="center-text">
            <img src="data:image/jpeg;base64,{image_to_base64("profile.jpeg")}" class="profile-pic"/>
            <h2 style="margin-bottom: 0px;">Vishnupriya</h2>
            <div class="role-tag-expanded" style="margin-top: 0px; margin-bottom: 25px;">Computer Science</div>
        </div>
        '''
        st.markdown(name_section, unsafe_allow_html=True)

        contact_html = '''
        <div class="info-wrapper">
            <div class="info-block">
                <img class="info-icon" src="https://cdn-icons-png.flaticon.com/512/542/542638.png"/>
                <div class="info-text">
                    <div class="info-label">EMAIL</div>
                    <div class="info-value">vishnupriyapolamreddy@gmail.com</div>
                </div>
            </div>
            <div class="info-block">
                <img class="info-icon" src="https://cdn-icons-png.flaticon.com/512/597/597177.png"/>
                <div class="info-text">
                    <div class="info-label">PHONE</div>
                    <div class="info-value">+1 (469) 686-0078</div>
                </div>
            </div>
            <div class="info-block">
                <img class="info-icon" src="https://cdn-icons-png.flaticon.com/512/684/684908.png"/>
                <div class="info-text">
                    <div class="info-label">LOCATION</div>
                    <div class="info-value">Dallas, Texas</div>
                </div>
            </div>
        </div>
        <div class="social-icons">
            <a href="https://www.linkedin.com/in/vishnupriya-polamreddy/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png"/>
            </a>
            <a href="https://github.com/vishnupriya77" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/733/733553.png"/>
            </a>
        </div>
        '''
        st.markdown(contact_html, unsafe_allow_html=True)

    with col2:
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["\U0001F464 About Me", "\U0001F6E0 Skills", "\U0001F4BC Experience", "\U0001F4C1 Projects", "\U0001F4C4 Resume"])

        with tab1:
            st.header("Hi, I am Vishnupriya! 👋")
            st.write("Master’s student in Computer Science at The University of Texas at Dallas with prior experience as a Data Analyst Intern at Hudson’s Bay Company. I’ve worked on projects involving machine learning, data visualization, and full-stack development. Currently seeking opportunities to apply my skills in real-world industry settings.")

            st.markdown("""
    <style>
    .chat-container {
        background-color: #1a1a1a;
        border-radius: 14px;
        padding: 20px;
        margin-top: 30px;
        border: 1px solid #333;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }
    .chat-title {
        font-size: 22px;
        font-weight: 600;
        margin-bottom: 18px;
        color: #ffffff;
    }
    .ai-response {
        background-color: #2a2a2a;
        color: white;
        padding: 14px 18px;
        border-radius: 12px;
        font-size: 15px;
        max-width: 90%;
        margin-bottom: 15px;
    }
    .chat-input .stTextInput>div>div>input {
        background-color: #2a2a2a !important;
        color: white !important;
        border-radius: 8px !important;
        font-size: 15px !important;
        border: none !important;
    }
    </style>
    <div class="chat-container" id="vishbot-container">
        <div class="chat-title">Ask VishBot anything about me!</div>
        <div class="ai-response">
            Hi! I'm <strong>VishBot</strong>, Vishnupriya's AI assistant. Ask me anything about her skills, experience, projects, or visa status! 🚀
        </div>
    </div>
""", unsafe_allow_html=True)


            with st.container():
                user_input = st.text_input("", placeholder="Type your question here...", label_visibility="collapsed")
                if user_input:
                    response = generate_response(user_input)
                    st.markdown(response, unsafe_allow_html=True)




        with tab2:
            st.markdown("""
            <style>
            .skills-box {
                background-color: #f0cb7b;
                border-radius: 15px;
                padding: 30px;
                margin-top: 30px;
                color: black;
            }
            .skills-box ul {
                list-style-type: disc;
                padding-left: 25px;
                line-height: 1.8;
            }
            .skills-box li {
                margin-bottom: 10px;
            }
            </style>
            <div class="skills-box">
                <ul>
                    <li><strong>Programming Languages:</strong> Programming Languages: Python, SQL, R, HTML, CSS</li>
                    <li><strong>Data Visualization & BI Tools:</strong> Power BI, Tableau</li>
                    <li><strong>Databases:</strong> MySQL, MongoDB, Microsoft SQL Server, Oracle, MS Access</li>
                    <li><strong>Big Data & Cloud Technologies:</strong> Apache Spark, Hadoop, Databricks, PySpark</li>
                    <li><strong>Libraries & Frameworks:</strong> Pandas, NumPy, Matplotlib, Seaborn, TensorFlow, Keras, PyTorch React, Flask</li>
                    <li><strong>Tools:</strong> PyCharm, Jupyter Notebook, R Studio, MS Office - (Excel, Word, PowerPoint & Outlook), MS Excel, GIT, MATLAB, VS Code, LINUX, UNIX</li>
                    <li><strong>Machine Learning & Analytics:</strong> Predictive Modelling, Sentiment Analysis, NLP, Deep Learning, Reinforcement Learning</li>
                    <li><strong>Certifications:</strong> Front-End Web UI Frameworks and Tools (Coursera), Java for Android (Coursera), Certificate in Oracle (Oracle Academy)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with tab3:
            st.markdown("""
            <style>
            .exp-container {
                display: flex;
                margin-bottom: 20px;
                border-radius: 12px;
                overflow: hidden;
            }
            .exp-left {
                background-color: #e0b861;
                padding: 20px;
                width: 30%;
                text-align: center;
                font-weight: bold;
                color: black;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
            }
            .exp-right {
                background-color: #1e1e1e;
                padding: 20px;
                width: 70%;
                color: white;
                font-size: 15px;
            }
            .exp-right ul {
                padding-left: 20px;
            }
            </style>
            <div class="exp-container">
                <div class="exp-left">
                    Hudson’s Bay Company<br>
                    Data Analyst Intern<br>
                    Feb 2023 – Jun 2023
                </div>
                <div class="exp-right">
                    <ul>
                        <li>Managed and maintained SQL databases, ensuring 99.9% data accuracy through validation and quality checks</li>
                        <li>Conducted exploratory data analysis (EDA) on 100K+ transactions, uncovering trends that improved decision-making for marketing strategies</li>
                        <li>Designed interactive dashboards in Power BI and Excel, enhancing reporting efficiency by 30% and enabling real-time business insights.</li>
                        <li>Automated data cleaning and preprocessing scripts in Python, reducing manual effort by 40% and improving workflow efficiency.</li>
                    </ul>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with tab4:
            projects = [
                ("Travel Advisor", "images/Travel Advisor.png", "https://github.com/vishnupriya77/Travel-Advisor"),
                ("Brain Tumor Detection", "images/Brain Tumor Detection.png", "https://github.com/yourusername/brain-tumor-detection"),
                ("Library Management System", "images/Library Management System.jpg", "https://github.com/vishnupriya77/Library-Management-System/tree/main/Library%20Management%20System"),
                ("Online Hotel Reservation", "images/Online Hotel Registration.webp", "https://github.com/vishnupriya77/ONLINE-HOTELRESERVATION"),
                ("Automated Attendance System", "images/Automated Attendance System.png", "https://github.com/vishnupriya77/Automated-Attendance-System"),
            ]

            html = """
            <style>
            .projects-grid {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 30px;
                margin-top: 40px;
            }
            .project-card {
                width: 45%;
                background-color: transparent;
                border-radius: 12px;
                padding: 10px;
                text-align: center;
                box-shadow: 0 0 6px rgba(255,255,255,0.05);
                transition: transform 0.3s ease;
            }
            .project-card:hover {
                transform: scale(1.03);
            }
            .project-card img {
                width: 75%;
                height: auto;
                border-radius: 10px;
                margin-bottom: 12px;
            }
            .project-title {
                font-size: 16px;
                font-weight: bold;
                color: white;
                margin-bottom: 4px;
            }
            
            </style>
            <div class="projects-grid">
            """

            for title, img_path, link in projects:
                try:
                    img_base64 = image_to_base64(img_path)
                    card = f"""
                    <a href="{link}" target="_blank" class="project-card">
                        <img src="data:image/png;base64,{img_base64}" />
                        <div class="project-title">{title}</div>
                    </a>
                    """
                    html += card
                except FileNotFoundError:
                    continue

            html += "</div>"

            components.html(html, height=1000, scrolling=True)

        with tab5:
            with open("Resume.pdf", "rb") as Resume_file:
                Resume_data = Resume_file.read()
            st.download_button(
                label="Download Resume",
                data=Resume_data,
                file_name="Resume.pdf",
                mime="application/pdf"
            )

def generate_response(query):
    query_lower = query.strip().lower()

    # Keyword-based detection for predefined answers
    if "project" in query_lower:
        return all_projects
    elif "certification" in query_lower or "certificstion" in query_lower or "certs" in query_lower:
        return all_certifications
    elif "qualification" in query_lower or "education" in query_lower or "degree" in query_lower:
        return all_qualifications
    elif "experience" in query_lower or "work" in query_lower or "internship" in query_lower:
        return all_experience

    # Check exact match from var (custom questions)
    for stored_q in var:
        if stored_q.strip().lower() == query_lower:
            return var[stored_q]

    # Check loose keyword-based matches in predefined_response
    for keyword in predefined_response:
        if keyword in query_lower:
            return predefined_response[keyword]

    return "I'm not sure about that, but you can ask Vishnupriya directly!"



if __name__ == "__main__":
    main()
