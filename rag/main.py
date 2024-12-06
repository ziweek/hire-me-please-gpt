from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from streamlit_dimensions import st_dimensions

from utils.model import run_llm
from utils.utils import load_yaml_file

import pprint
import requests
import json




st.set_page_config(initial_sidebar_state="expanded")

user_data = load_yaml_file("rag/config.yaml")
user_name = user_data['name']
user_email = user_data["email"]
user_github = user_data["github"]
user_linkedin = user_data["linkedin"]


# st.subheader(f"{user_name}")
# st.text("A machine learning engineer specializing in multilingual NLP solutions, with expertise in developing scalable applications and enhancing global user experiences.")


st.title("HireMePleaseGPT")
st.text("The ultimate job-hunting sidekick that knows your resume better than you do. Ready to charm recruiters with wit, facts, and just the right sprinkle of overachiever vibes!")
st.caption("* Powered by the Gemini API free plan (thanks to the applicant's budget-friendly lifestyle), HireMePleaseGPT might occasionally stay quiet clearly because someone else who ***used up all the tokens*** is already busy discovering how amazing I am!")
tab1, tab2 = st.tabs(["Prompt", "My Resume"])
with tab1:
    prompt = st.text_area("Please Ask me a Question! :)", placeholder="Enter your prompt")
    if prompt:
        with st.spinner("Generating reponse..."):
            
            generated_response = run_llm(query=prompt)
            # pprint.pprint(generated_response)
            
            documents_metadata_source = list([document.metadata["source"].replace("rag/src/", "") for document in generated_response["context"]])
            documents_metadata_page = list([document.metadata["page"] for document in generated_response["context"]])
            documents_page_contents = list([document.page_content for document in generated_response["context"]])
            sources_string = "\n\n\n".join([f"{documents_metadata_source} Page {documents_metadata_page}\n{documents_page_contents}" for documents_metadata_source, documents_metadata_page, documents_page_contents in zip(documents_metadata_source, documents_metadata_page, documents_page_contents)])
        
            st.markdown(generated_response['answer'])
            with st.expander("See Sources"):
                st.text(sources_string)
with tab2:
    container_dim = st_dimensions(key="main")
    pdf_viewer(
        input=user_data['resume_file_path'],
        width=int(container_dim['width']) if container_dim else 400,
        render_text=True
        )
    


css = '''
<style>
    [data-testid="stSidebar"]{
        min-width: 350px;
        max-width: 350px;
    }
</style>
'''
st.markdown(css, unsafe_allow_html=True)
with st.sidebar:
    st.header("User Profile")
    with st.expander("Visit Analytics", expanded=False):
        col1, col2, col3 = st.columns(3)
        col1.metric(label="a", value=1, delta="1")
        col2.metric(label="a", value=1, delta="1")
        col3.metric(label="a", value=1, delta="1")

    try:
        github_user_api_url = f"https://api.github.com/users/ziweek"
        github_user_api_response = requests.get(github_user_api_url)
        github_user_api_result = json.loads(github_user_api_response.content)
        img = github_user_api_result["avatar_url"]
    except:
        google_drive_url = "https://drive.google.com/uc?export=view&id=1459-NPm4sC50nrQRdjTpmpz_eKunIi04"
        img = google_drive_url
    st.image(img, width=300)
    st.markdown(
        body="""   
<div align="center"> 
    <a href='https://github.com/ziweek' target="_blank">
    <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Github-262731?style=flat-square&logo=github&logoColor=white">
    <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Github-F0F2F6?style=flat-square&logo=github&logoColor=black">
    <img alt="IMAGE" src="http://LIGHT_IMAGE_URL.png">
    </picture>
    </a>
    <a href='https://www.linkedin.com/in/ziweek' target="_blank">
    <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/LinkedIn-262731?style=flat-square&logo=linkedin&logoColor=0A66C2">
    <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/LinkedIn-F0F2F6?style=flat-square&logo=linkedin&logoColor=0A66C2">
    <img alt="IMAGE" src="http://LIGHT_IMAGE_URL.png">
    </picture>
    </a>
    <a href='mailto:alex.jiuk.kim@gmail.com' target="_blank">
    <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/Gmail-262731?style=flat-square&logo=gmail&logoColor=EA4335">
    <source media="(prefers-color-scheme: light)" srcset="https://img.shields.io/badge/Gmail-F0F2F6?style=flat-square&logo=gmail&logoColor=EA4335">
    <img alt="IMAGE" src="http://LIGHT_IMAGE_URL.png">
    </picture>
    </a>
</div>
<br/>

<p align="center">
    <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white"/>
    <img src="https://img.shields.io/badge/LangSmith-1C3C3C?style=flat-square&logo=langchain&logoColor=white"/>
    <img src="https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=Ollama&logoColor=white"/>
    <br/>
    <img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white"/>
    <img src="https://img.shields.io/badge/Spring-6DB33F?style=flat-square&logo=spring&logoColor=white"/>
    <img src="https://img.shields.io/badge/NestJS-E0234E?style=flat-square&logo=nestjs&logoColor=white"/>
    <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"/>
    <br/>
    <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white"/>
    <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white"/>
    <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white"/>
    <br/>
    <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white"/>
    <img src="https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white"/>
    <br/>
    <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white"/>
</p>
        """,
        unsafe_allow_html=True
    )


# Add a footer
st.caption("---")
st.caption("Powered by LangChain, Gemini API, and Streamlit")


if __name__ == "__main__":
    print("HireMePleaseGPT is running...")
