# Retrieval-augmented-generation for Large Language Model
## 1.Introduce
Retrieval augmented generation là một kĩ thuật kết hợp giữa khả năng tạo sinh của mô hình ngôn ngữ lớn(LLM) và khả năng truy xuất của hệ thống vector database để giải quyết bài toán trả lời câu hỏi, cải thiện độ chính xác.
## 2.Workflow
![image](https://github.com/minhduc2672002/Retrieval-augmented-generation/assets/133132824/87bee34b-db54-4c51-8ae7-eab36288cfd8)
* Description:
  - Dữ liệu sẽ dạng văn bản, text sẽ được chia nhỏ ra thành những đoạn có độ dài 256.
  - Các đoạn text sẽ được đưa vào model embedding để nhúng thành những vector có độ dài 384 chiều.
  - Dữ liệu sau khi nhúng sẽ được lưu vào cơ sở dữ liệu vector(ở đây chúng tôi dùng Pinecone) dùng cho mục đích truy xuất.
  - Sử dụng thư viện Langchain để xấy dựng pipeline kết hợp giữa khả năng truy xuất của vector database và mô hình ngôn ngữ lớn (ở đây chúng tôi sử dụng Llama 2) để tạo ra câu trả lời phù hợp dựa trên dữ liệu đã được đưa vào.
# Chi tiết vui lòng xem ở file .ipynb
