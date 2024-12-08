# 🌟 **Customer Support Chatbot Using LangChain and Chroma** 🌟

Welcome to the **Customer Support Chatbot** project! This chatbot uses the **LangChain** framework, **Chroma** vector store, and **OpenAI's GPT** model to create an intelligent customer support assistant. It answers questions based on the documents in your system, offering a seamless and effective interaction.

## 🚀 **Features**

- 🔍 **Document-based Q&A**: The chatbot uses PDF files to retrieve and answer questions related to the content.
- 💬 **Interactive UI**: The Gradio-powered chat interface allows for real-time conversation.
- 🌐 **Scalable**: Easily extendable to work with more documents and improve the chatbot's knowledge base.

---

## 🛠 **Project Structure**
Customer_Support_Chatbot/
├── Data/                  # PDF documents for the chatbot
│   ├── botanical.pdf      # Botanical content
│   ├── astronomical.pdf   # Astronomical content
│   ├── biological.pdf     # Biological content
│   ├── cosmological.pdf   # Cosmological content
│   ├── culinary.pdf       # Culinary content
│   └── pharmaceutical.pdf # Pharmaceutical content
│
├── example.py             # Core logic for chatbot and Chroma integration
├── ui.py                  # User interface with Gradio
├── .env                   # Environment variables (API keys and sensitive info)
├── .gitignore             # Git ignore file to avoid unnecessary uploads
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies


## 🔧 **Prerequisites**

Before you run the project, ensure that you have the following installed:

- Python 3.8 or higher
- Git (for version control)
- Virtualenv (for isolated environments)

---

## 🛠️ **Setting Up the Environment**

Follow these steps to get the project running locally:

### 1. **Clone the repository:**
```bash
git clone https://github.com/your-username/Customer_Support_Chatbot.git
cd Customer_Support_Chatbot
2. Create a virtual environment:
bash
Copy code
python -m venv myenv
3. Activate the virtual environment:
Windows:
bash
Copy code
myenv\Scripts\activate
macOS/Linux:
bash
Copy code
source myenv/bin/activate
4. Install dependencies:
bash
Copy code
pip install -r requirements.txt
5. Set up environment variables:
Create a .env file in the root of the project directory and add your OpenAI API key. Example .env:

makefile
Copy code
OPENAI_API_KEY=your_openai_api_key
🚀 How to Run the Code
1. Run the chatbot server:
Ensure your virtual environment is activated and dependencies are installed, then start the chatbot interface:

bash
Copy code
python ui.py
Visit http://127.0.0.1:7860 in your browser to interact with the chatbot.

📄 How It Works
1. PDF Document Loader:
The chatbot loads PDFs from the Data/ folder using PyPDFLoader. It extracts text from these documents and splits them into smaller chunks.

2. Chroma for Vector Store:
The documents are embedded using OpenAI's embeddings and stored in Chroma for fast similarity search. This allows the chatbot to retrieve relevant information when a question is asked.

3. Question Answering:
The chatbot answers user queries using the GPT model powered by OpenAI. It uses the retrieved context to provide relevant answers.

4. Gradio Interface:
The chatbot is accessible via a web-based interface built with Gradio. Users can chat with the assistant and get answers in real-time.

🧑‍💻 Usage Example
Once the chatbot is running, you can ask questions like:

"What is a hydrogen fuel cell?"
"Tell me about astronomical concepts."
The chatbot will answer based on the content of the documents in the Data/ folder.

📝 Gitignore File
Here's the content for the .gitignore file to prevent unnecessary files from being tracked:

graphql
Copy code
# Ignore virtual environment
myenv/

# Ignore Python cache files
__pycache__/
*.pyc

# Ignore .env file for API keys
.env

# Ignore Chroma database directory
chromadb/

# Ignore IDE and editor-specific files
.vscode/
.idea/
📝 Additional Notes
Make sure to set your OpenAI API Key correctly in the .env file before running the project.
The Chroma database (chromadb/) will be used to store the document embeddings and retrieval info locally.
Feel free to add more documents to the Data/ folder, and the chatbot will automatically update the knowledge base.
📑 Project Improvements
✅ Performance improvements: Optimize the question-answering process for faster results.
🔄 Add more documents: Keep expanding the chatbot's knowledge base by adding more PDFs to the Data/ folder.
🚀 Advanced features: Integrate with more APIs for broader functionality (e.g., database, cloud storage, etc.).
📢 Contact Information
Feel free to reach out if you have any questions or suggestions.

Happy Coding! 👨‍💻🚀

