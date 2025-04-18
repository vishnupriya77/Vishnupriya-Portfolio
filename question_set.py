from predefined_answers import predefined_response, all_projects, all_certifications, all_qualifications, all_experience # type: ignore

var = {}

# Project questions
project_questions = [
    "Can you list her Projects?",
    "list her Projects?",
    "her Projects?",
    "Projects?",
    "Her Projects?",
    "Can you list Vishnupriya's Projects?",
    "Vishnupriya's Projects?",
    "What projects has she worked on?",
    "She worked on which projects?",
    "Which projects has she worked on?",
    "Tell me about Vishnupriya's projects",
    "Tell me about her projects",
    "What are some of her past projects?",
    "List all projects she has worked on",
    "Can you provide details on her projects?",
    "Give me an overview of her projects",
    "What kind of projects has she worked on?",
    "Can you summarize her project experience?",
    "What are her key projects?",
    "Has she worked on any notable projects?",
    "Show me her project portfolio.",
    "What projects are in her portfolio?",
    "Provide a list of her completed projects",
    "tell me about your projects",
    "tell me about projects",
    "projects you have worked in",
    "give me a list of projects you have worked on",
    "can you tell me about any projects you have worked on?",
    "can you tell me about any Vishnupriya's project?",
    "can you tell me about her projects?",
    "what are some of your projects?",
]

# Certification questions
certification_questions = [
    "Can you list her certifications?",
    "List her certifications?",
    "Her certifications?",
    "Certifications?",
    "Can you list Vishnupriya's certifications?",
    "Vishnupriya's certifications?",
    "What certifications does she have?",
    "She holds which certifications?",
    "Which certifications has she earned?",
    "Tell me about her certifications",
    "What are some of her professional certifications?",
    "List all certifications she has obtained",
    "Can you provide details on her certifications?",
    "Give me an overview of her certifications",
    "What type of certifications does she hold?",
    "Can you summarize her certification history?",
    "What are her key certifications?",
    "Has she earned any notable certifications?",
    "Show me her certification portfolio",
    "What certifications are in her credentials?",
    "Provide a list of her professional certifications",
    "List of her completed certifications",
    "Tell me about professional certifications",
    "Certifications you have earned",
    "Give me a list of certifications you have obtained",
    "Can you tell me about any certifications you've earned?",
    "Can you tell me about her certification achievements?",
    "What are some of your certifications?",
    "certificstions?", "certificstions list?", "her certificstions?", "wat r her certs?", "certs list?"
]

# Qualification questions
qualification_questions = [
    "Can you list her qualifications?",
    "List her qualifications?",
    "Her qualifications?",
    "Qualifications?",
    "Can you list Vishnupriya's qualifications?",
    "Vishnupriya's qualifications?",
    "What qualifications does she have?",
    "She holds which qualifications?",
    "Which qualifications has she obtained?",
    "Tell me about her educational background",
    "What are her professional credentials?",
    "List all degrees she has earned",
    "Can you provide details on her professional training?",
    "Give me an overview of her academic history",
    "What kind of professional training has she completed?",
    "Can you summarize her academic achievements?",
    "Has she earned any advanced degrees?",
    "Show me her educational certificates",
    "Provide a list of her completed trainings",
    "Tell me about your educational background",
    "Degrees you have earned",
    "Give me a list of credentials you possess",
    "Can you tell me about her technical certifications?",
    "what skools did she go to?",
    "any degrees?", "she got phd?", "her collage details?"
]

# Experience questions
experience_questions = [
    "What is her Work Experience?",
    "Experience?",
    "Work Experience?",
    "Can you list her Work Experience?",
    "Describe her Work Experience",
    "How much Work Experience does she have?",
    "Detail her Work Experience",
    "Tell me about her Work Experience",
    "What are the highlights of her Work Experience?",
    "How long has she been working?",
    "Could you outline her Professional Experience?",
    "Summarize her Professional Experience",
    "What roles has she held in her Professional Experience?",
    "Explain her Professional Background",
    "Which industries has she worked in?",
    "What sectors does she have experience in?",
    "Describe her Industry Background",
    "What companies has she worked for?",
    "Where has she worked before?",
    "What is her Employment History?",
    "What responsibilities has she handled?",
    "What skills has she gained from her experience?",
    "What are her key career achievements?",
    "How many years of experience does she have?",
    "What is her career progression?",
    "Tell me about her work background",
    "What does she do professionally?",
]

# Populate the dictionary
for q in project_questions:
    var[q] = all_projects
for q in certification_questions:
    var[q] = all_certifications
for q in qualification_questions:
    var[q] = all_qualifications
for q in experience_questions:
    var[q] = all_experience
