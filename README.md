# Jaipur Website

A **dynamic, multi-page web application** built using **Streamlit**, providing an interactive and informative experience about **Jaipur**. This website covers various aspects such as **tourism, healthcare, history, and law**, and also features an **AI-powered chatbot** for user interaction.

## ⭐ Key Features

### 1️⃣ Home Page
* Provides an overview of Jaipur with a **user-friendly interface**.
* Easy navigation between different sections of the website.

### 2️⃣ Tourism Page
* Showcases **popular tourist destinations** in Jaipur.
* Includes descriptions of **historical landmarks, cultural heritage, and must-visit places**.

### 3️⃣ Healthcare Page
* Contains **dummy data for doctor appointments**.
* Initially planned to integrate a **real-time appointment booking API**, but limited free API access prevented full implementation.

### 4️⃣ History Page
* Provides **detailed historical insights** about Jaipur.
* Engages users with **fascinating facts and cultural significance**.

### 5️⃣ Law Page
* Offers **legal information and guidelines** relevant to Jaipur.
* Helps users understand **local laws and regulations**.

### 6️⃣ Integrated AI Chatbot (Ollama - LLaMA 2 Model)
* **Conversational AI chatbot** built using **Ollama's LLaMA 2**.
* Enhances user experience by providing **quick responses and information**.
* **Note:** To use the chatbot on another machine, users need to **download the Ollama LLaMA 2 model** locally.

## 📌 Installation & Setup
To run this project locally, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/jaipur-website.git
   ```

2. Navigate to the project folder:
   ```
   cd jaipur-website
   ```

3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

5. (Optional: To enable chatbot functionality)
   - Install Ollama on your machine
   - Download the LLaMA 2 model using:
     ```
     ollama pull llama2
     ```
     
## 🚀 Technologies Used
* **Python** (Streamlit for web development)
* **Ollama LLaMA 2** (Chatbot integration)
* **REST API (planned)** for real-time doctor appointment booking

## 💡 Future Enhancements
* Full **real-time doctor appointment booking system** using a paid API.
* Improved **UI/UX with custom CSS and JavaScript**.
* **Enhanced chatbot capabilities** with multimodal inputs.



