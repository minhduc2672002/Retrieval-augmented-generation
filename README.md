# Retrieval-augmented-generation for Large Language Model
Link Demo: https://www.youtube.com/watch?v=HJTrIfLI8Ow
## 1.Introduce
Retrieval augmented generation là một kĩ thuật kết hợp giữa khả năng tạo sinh của mô hình ngôn ngữ lớn(LLM) và khả năng truy xuất của hệ thống vector database để giải quyết bài toán trả lời câu hỏi, cải thiện độ chính xác.
## 2.Architecture
![image](https://github.com/user-attachments/assets/a24441c9-ed95-46a1-951b-27f6352ce21d)
## 3.Flow
![image](https://github.com/user-attachments/assets/19ba9d7c-903d-49d5-bde9-703162f04c79)

* Description:
  - Dữ liệu sẽ dạng văn bản, text sẽ được chia nhỏ ra thành những đoạn có độ dài 512.
  - Các đoạn text sẽ được đưa vào model embedding để nhúng thành những vector có độ dài 768 chiều.
  - Dữ liệu sau khi nhúng sẽ được lưu vào cơ sở dữ liệu vector(ở đây chúng tôi dùng Chroma) và BM25 dùng cho mục đích truy xuất.
  - Sử dụng thư viện Langchain để xấy dựng pipeline kết hợp giữa khả năng truy xuất của vector database và mô hình ngôn ngữ lớn (ở đây chúng tôi sử dụng Llama 3) để tạo ra câu trả lời phù hợp dựa trên dữ liệu đã được đưa vào.
## 4.UI
![Screenshot 2024-06-21 135543](https://github.com/user-attachments/assets/5cdeebd3-049a-4980-bf94-7edf916835ed)

![Screenshot 2024-06-21 135910](https://github.com/user-attachments/assets/a6d330b5-86c9-4b71-8b7a-0e23ec09dc80)
