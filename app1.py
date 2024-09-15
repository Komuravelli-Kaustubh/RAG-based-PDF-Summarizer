# import streamlit as st
# import time
# from langchain_community.document_loaders import PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_chroma import Chroma
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains import create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain_core.prompts import ChatPromptTemplate
# import os



# from dotenv import load_dotenv
# load_dotenv()


# st.title("RAG Application built on Gemini Model")
# # Define a list of file paths manually
# pdf_files = [
#     "yolov9_paper.pdf",
#     "FEWD Unit-3.pdf",
#     # "path/to/third_pdf_file.pdf"
#     # Add more file paths as needed
# ]

# # Load and concatenate text from all PDFs
# all_docs = []
# for pdf_file in pdf_files:
#     if os.path.exists(pdf_file):
#         loader = PyPDFLoader(pdf_file)
#         data = loader.load()
#         all_docs.extend(data)
#     else:
#         st.warning(f"File not found: {pdf_file}")

# # Split documents into chunks
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
# docs = text_splitter.split_documents(all_docs)


# vectorstore = Chroma.from_documents(documents=docs, embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))

# retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 10})

# llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",temperature=0,max_tokens=None,timeout=None)


# query = st.text_input("Say something: ") 
# prompt = query

# system_prompt = (
#     "You are an assistant for question-answering tasks. "
#     "Use the following pieces of retrieved context to answer "
#     "the question. If you don't know the answer, say that you "
#     "don't know."
#     # "Use three sentences maximum and keep the "
#     # "answer concise."
#     "No max limit, give the answer as detailly and vividly as possible"
#     "\n\n"
#     "{context}"
# )

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", system_prompt),
#         ("human", "{input}"),
#     ]
# )

# if query:
#     question_answer_chain = create_stuff_documents_chain(llm, prompt)
#     rag_chain = create_retrieval_chain(retriever, question_answer_chain)

#     response = rag_chain.invoke({"input": query})
#     #print(response["answer"])

#     st.write(response["answer"])



# ----------------------------------------------------------------------------------------



# import streamlit as st
# import time
# from langchain_community.document_loaders import PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_chroma import Chroma
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains import create_retrieval_chain
# from langchain.chains.combine_documents import create_stuff_documents_chain
# from langchain_core.prompts import ChatPromptTemplate
# import os
# from dotenv import load_dotenv

# load_dotenv()

# st.title("RAG Application built on Gemini Model")

# # Upload multiple files via Streamlit interface
# uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

# if uploaded_files:
#     all_docs = []
#     for uploaded_file in uploaded_files:
#         # Save uploaded file to disk
#         with open(uploaded_file.name, "wb") as f:
#             f.write(uploaded_file.read())
        
#         # Load and concatenate text from all PDFs
#         loader = PyPDFLoader(uploaded_file.name)
#         data = loader.load()
#         all_docs.extend(data)
    
#     # Split documents into chunks
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
#     docs = text_splitter.split_documents(all_docs)
    
#     vectorstore = Chroma.from_documents(documents=docs, embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))
#     retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 10})
    
#     llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0, max_tokens=None, timeout=None)
    
#     # Automatic Summarization
#     system_prompt_summary = (
#         "You are a smart assistant helping students summarize their educational content effectively. "
#         "Provide a very detailed summary, ensuring that no points are missed. Explain concepts clearly, "
#         "with examples if necessary. There is no maximum limit; provide as much detail as possible."
#         "\n\n"
#         "{context}"
#     )
    
#     summary_prompt = ChatPromptTemplate.from_messages(
#         [
#             ("system", system_prompt_summary),
#             ("human", "{input}"),
#         ]
#     )
    
#     # Generate summary
#     question_answer_chain_summary = create_stuff_documents_chain(llm, summary_prompt, document_variable_name="context")
#     rag_chain_summary = create_retrieval_chain(retriever, question_answer_chain_summary)
    
#     response_summary = rag_chain_summary.invoke({"input": "Summarize the content"})
#     st.write("**Summary:**")
#     st.write(response_summary["answer"])
    
#     # Question and Answer
#     query = st.text_input("Ask a question related to the content: ") 
#     if query:
#         system_prompt_qa = (
#             # "You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer "
#             # "the question. If you don't know the answer, say that you don't know. Provide detailed answers and be as "
#             # "specific as possible."
#             # "\n\n"
#             # "{context}"
#             "You are an assistant for question-answering tasks. "
#             "Use the following pieces of retrieved context to answer "
#             "the question. If you don't know the answer, say that you "
#             "don't know."
#             # "Use three sentences maximum and keep the "
#             # "answer concise."
#             "No max limit, give the answer as detailly and vividly as possible"
#             "\n\n"
#             "{context}"
#         )
        
#         qa_prompt = ChatPromptTemplate.from_messages(
#             [
#                 ("system", system_prompt_qa),
#                 ("human", "{input}"),
#             ]
#         )
        
#         question_answer_chain_qa = create_stuff_documents_chain(llm, qa_prompt, document_variable_name="context")
#         rag_chain_qa = create_retrieval_chain(retriever, question_answer_chain_qa)
        
#         response_qa = rag_chain_qa.invoke({"input": query})
        
#         st.write("**Answer:**")
#         st.write(response_qa["answer"])
# else:
#     st.info("Please upload PDF files to proceed.")

# --------------------------------------------------------------------------------------------



import streamlit as st
import time
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.title("RAG Application built on Gemini Model")

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Upload multiple PDF files via Streamlit interface
uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files:
    all_docs = []
    for uploaded_file in uploaded_files:
        # Save uploaded file to disk
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.read())
        
        # Load and concatenate text from all PDFs
        loader = PyPDFLoader(uploaded_file.name)
        data = loader.load()
        all_docs.extend(data)
    
    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
    docs = text_splitter.split_documents(all_docs)
    
    vectorstore = Chroma.from_documents(documents=docs, embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 10})
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0, max_tokens=None, timeout=None)
    
    # Automatic Summarization
    system_prompt_summary = (
        "You are a smart assistant helping students summarize their educational content effectively. "
        "Provide a very detailed summary, ensuring that no points are missed. Explain concepts clearly, "
        "with examples if necessary. There is no maximum limit; provide as much detail as possible."
        "\n\n"
        "{context}"
    )
    
    summary_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt_summary),
            ("human", "{input}"),
        ]
    )
    
    # Generate summary
    question_answer_chain_summary = create_stuff_documents_chain(llm, summary_prompt, document_variable_name="context")
    rag_chain_summary = create_retrieval_chain(retriever, question_answer_chain_summary)
    
    response_summary = rag_chain_summary.invoke({"input": "Summarize the content"})
    st.write("**Summary:**")
    st.write(response_summary["answer"])
    
    # Input for question
    query = st.text_input("Ask a question related to the content: ")
    
    if query:
        system_prompt_qa = (
            "You are an assistant for question-answering tasks. "
            "Use the following pieces of retrieved context to answer "
            "the question. If you don't know the answer, say that you "
            "don't know."
            "No max limit, give the answer as detailed and vividly as possible."
            "\n\n"
            "{context}"
        )
        
        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt_qa),
                ("human", "{input}"),
            ]
        )
        
        question_answer_chain_qa = create_stuff_documents_chain(llm, qa_prompt, document_variable_name="context")
        rag_chain_qa = create_retrieval_chain(retriever, question_answer_chain_qa)
        
        response_qa = rag_chain_qa.invoke({"input": query})
        
        # Add the new Q&A pair to the chat history
        st.session_state['chat_history'].append({"question": query, "answer": response_qa["answer"]})
    
    # Display chat history
    if st.session_state['chat_history']:
        st.write("**Chat History:**")
        for i, qa_pair in enumerate(st.session_state['chat_history']):
            st.write(f"**Q{i+1}:** {qa_pair['question']}")
            st.write(f"**A{i+1}:** {qa_pair['answer']}")
else:
    st.info("Please upload PDF files to proceed.")
