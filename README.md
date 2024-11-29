# HireMePleaseGPT

<table>
  <tr>
    <td style="width:1/2;">
      <img src="./src/banner.png"/>
    </td>
  </tr>
</table>
<br/>

<p align="center">
  <strong>The ultimate job-hunting sidekick that knows your resume better than you! :)</strong>
  <br/>
  <br/>
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white"/>
  <img src="https://img.shields.io/badge/LangSmith-1C3C3C?style=flat-square&logo=langchain&logoColor=white"/>
  <img src="https://img.shields.io/badge/Gemini%20API-8E75B2?style=flat-square&logo=googlegemini&logoColor=white"/>
  <br/>
  <img src="https://img.shields.io/badge/streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=Docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white"/>
</p>
<br/>

<p align="center">  
  <strong>↓ Check out prototypes ↓<strong>
  <br/>
  <br/>
  <a href='https://hire-me-please-gpt.streamlit.app'>
    <img src="https://img.shields.io/badge/Product-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white"/>
  </a>
  <a href='https://colab.research.google.com/drive/13-VZyx3LiYPRS8aw-AcMSBK0Z4--TF2j?usp=sharing'>
    <img src="https://img.shields.io/badge/Tutorial-Google%20Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white"/>
  </a>
</p>
<br/>

# Introduction

HireMePleaseGPT is a chatbot built using Retrieval-Augmented Generation (RAG) architecture, powered by LangChain and Streamlit. It is designed to deliver precise and clear answers by retrieving information from archives of resumes and projects.
<br/>

<details open>
 <summary><b>Why do we need HireMePleaseGPT?</b></summary>
In today’s bustling job market, recruiters often face the daunting challenge of sifting through mountains of resumes and projects with barely enough time to breathe, let alone dive deep. That’s where HireMePleaseGPT comes in—a simple yet genius solution to make life easier. Instead of painstakingly reading every word and deciphering the hidden treasures in a candidate’s resume, recruiters can now just ask HireMePleaseGPT anything they want to know. It’s like having a personal assistant who’s read every line for you and is ready with instant, meaningful insights—minus the coffee breaks!
</details>
<br/>

# Implementation

<table>
  <tr>
    <td style="width:1/2;">
      <img src="./src/diagram.png"/>
    </td>
  </tr>
</table>

<details open>
 <summary><b>Retrieval-Augmented Generation</b></summary>
HireMePleaseGPT is build as a RAG architecture, powered by LangChain, Google Gemini API, and FAISS vector database. Text from resume or cover letter is ingested to the FAISS vector database as soon as Google Gemini API embedded it into words or subwords. LangChain 
</details>
<br/>

<details open>
 <summary><b>Google Gemini API</b></summary>
HireMePleaseGPT utilizes the Google Gemini API to embed text from resumes and generate responses. It employs “model/text-embedding-004” and “Gemini-1.5-flash,” both available under the free plan, offering sufficient computational performance for a RAG architecture tailored to processing single or double-page PDF documents, such as resumes and cover letters.
</details>
<br/>

<details open>
  <summary><b>Powered by Streamlit</b></summary>
HireMePleaseGPT is deployed on the Streamlit.io platform. Steamlit framework provided well-built user-friendly UIUX blocks 
</details>
<br/>

# Contribution

<!--
https://contrib.rocks/preview?repo=angular%2Fangular-ja
-->

<a href="https://github.com/ziweek/two-armies-chat-once/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=ziweek/two-armies-chat-once" />
</a>
