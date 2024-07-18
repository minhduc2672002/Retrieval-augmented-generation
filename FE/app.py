import streamlit as st
import time
import os
from PyPDF2 import PdfReader
import requests
from docx import Document
import re
from docx2pdf import convert
from io import BytesIO



def convert_docx_to_pdf(docx_bytes):
    # Tạo tệp docx tạm thời
    with open("temp.docx", "wb") as f:
        f.write(docx_bytes.getbuffer())
    # Chuyển đổi tệp docx sang pdf
    convert("temp.docx", "output.pdf")
    # Đọc tệp PDF đã chuyển đổi
    with open("output.pdf", "rb") as f:
        pdf_bytes = f.read()
    # Xóa tệp tạm thời
    os.remove("temp.docx")
    os.remove("output.pdf")
    return pdf_bytes
def read_file(file):
    pdf_reader = PdfReader(file)
    whole_text = ""
    count_each_page = []
    for page in pdf_reader.pages:
        text = page.extract_text()
        whole_text += text
        each_page = len(text)
        count_each_page.append(each_page)
    return {
        'whole_text' : whole_text,
        'page_lengths': count_each_page
    }



def read_svg(file_path):
    with open(file_path, "r") as file:
        return file.read()


def get_answer(url,question):
    try:
        url_answer = url+"/answer"
        params = {
                'question': question,  
            }

        response = requests.get(url_answer,params=params)
        return response.json()['response']['answer']
    except Exception as e:
        return "Response Error!!"

def main():
    st.set_page_config(page_title="Chat with your document", page_icon=":books:")

    # Tạo tiêu đề cho ứng dụng
    st.header("CHAT WITH YOUR DOCUMENTS")

    if "whole_text" not in st.session_state:
        st.session_state.whole_text= ""
    
    if "page_lengths" not in st.session_state:
        st.session_state.page_lengths = []

    if "messages" not in st.session_state:
        st.session_state.messages = []
    with st.sidebar:
        url = st.text_input("URL Server:")
        st.subheader("Your documents")
        uploaded_file = st.file_uploader(
            "Upload your file (.pdf,.docx,.txt) here", accept_multiple_files=False)
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("Process"):
                if  url:
                    with st.spinner("Processing"):
                        if uploaded_file is not None:
                            st.session_state.whole_text=""
                            st.session_state.page_lengths = []
                            file_type = uploaded_file.name.split(".")[-1]
                            if file_type == "txt":
                                st.session_state.whole_text = uploaded_file.read().decode("utf-8")
                            elif file_type == "docx":
                                pdf_file = BytesIO(convert_docx_to_pdf(uploaded_file))
                                results = read_file(pdf_file)
                                st.session_state.whole_text = results['whole_text']
                                st.session_state.page_lengths = results['page_lengths']
                            elif file_type == "pdf":
                                results = read_file(uploaded_file)
                                st.session_state.whole_text = results['whole_text']
                                st.session_state.page_lengths = results['page_lengths']
                            else:
                                raise ValueError("Invalid file format!")
                        
                        try:
                            url_import = url+"/items"
                            payload = {"text": st.session_state.whole_text,
                                    "page_lengths": st.session_state.page_lengths}
                            st.session_state.response = requests.post(url_import, json=payload)
                            print(st.session_state.response.text)
                        except Exception as e:
                            st.sidebar.error("Lỗi khi request!!! Kiểm tra lại URL Server")
                else:
                     st.sidebar.error("Vui lòng nhập URL trước khi Process.")
        with col2:
            if st.button("Clear Chat", key="clear_chat",on_click=lambda: st.session_state.messages.clear()):
                st.session_state.messages = []


    # Chèn CSS tùy chỉnh để định dạng tin nhắn
    css_file_path = "css/styles.css"
    if os.path.exists(css_file_path):
        with open(css_file_path, "r", encoding="utf-8") as f:
            css_content = f.read()
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    else:
        st.error(f"Tệp CSS '{css_file_path}' không tồn tại!")

    # user_icon_path = os.path.join(os.path.dirname(__file__), 'user_icon.svg')
    assistant_icon_path = os.path.join(os.path.dirname(__file__), 'asset/assistant_icon.svg')


    # Hiển thị các tin nhắn
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(
                f'<div class="chat-container user-message">'
                f'<div class="message-content">{message["content"]}</div>'
                # f'<div class="avatar user-avatar">{read_svg(user_icon_path)}</div>'
                f'</div>', 
                unsafe_allow_html=True)
        else:
            st.markdown(
                f'<div class="chat-container assistant-message">'
                f'<div class="avatar">{read_svg(assistant_icon_path)}</div>'
                f'<div class="message-content">{message["content"]}</div>'
                f'</div>', 
                unsafe_allow_html=True)
    


    # Nhập tin nhắn mới
    prompt = st.chat_input("Ask a question about your documents:")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})

        st.markdown(
            f'<div class="chat-container user-message">'
            f'<div class="message-content">{prompt}</div>'
            # f'<div class="avatar user-avatar">{read_svg(user_icon_path)}</div>'
            f'</div>', 
            unsafe_allow_html=True)
    
        # Phản hồi giả lập từ bot
        response = get_answer(url,prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Hiển thị phản hồi từng chút một
        placeholder = st.empty()
        full_response = ""
        for char in response.split(" "):
            full_response += char
            full_response+= " "
            full_response = full_response.replace("\n","<br>")
            placeholder.markdown(
                f'<div class="chat-container assistant-message">'
                f'<div class="avatar">{read_svg(assistant_icon_path)}</div>'
                f'<div class="message-content">{full_response}</div>'
                f'</div>', 
                unsafe_allow_html=True)
            time.sleep(0.05)  # Điều chỉnh tốc độ hiện chữ ở đây
        
        st.markdown(
            """
            <script>
            var elem = document.getElementById('assistant_message');
            elem.scrollIntoView();
            </script>
            """,
            unsafe_allow_html=True
        )



if __name__ == '__main__':
    main()
