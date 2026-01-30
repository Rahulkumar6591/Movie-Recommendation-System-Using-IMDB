# 🎬 Movie Recommendation System using IMDB Dataset  

This repository contains a **Movie Recommendation System** built using the **IMDB dataset**. The system leverages **Content-Based Filtering** and **Collaborative Filtering** techniques to provide personalized movie recommendations based on user preferences. It processes movie metadata such as genres, ratings, and user reviews to generate meaningful suggestions.  

## 📌 Features  

### 🔹 Data Processing  
- Loads and cleans the **IMDB dataset**, removing missing values and irrelevant data.  
- Extracts and preprocesses important features like **title, genre, director, cast, and ratings**.  
- Uses **Natural Language Processing (NLP)** techniques to analyze movie descriptions and reviews.  

### 🔹 Recommendation Algorithms  
#### ✅ **Content-Based Filtering:**  
- Utilizes **TF-IDF (Term Frequency-Inverse Document Frequency)** and **cosine similarity** to recommend movies based on textual descriptions and metadata.  
- Suggests movies similar to a given movie based on **plot summaries, genres, and keywords**.  

#### ✅ **Collaborative Filtering:**  
- Implements **User-Based and Item-Based Collaborative Filtering** using the **K-Nearest Neighbors (KNN) algorithm**.  
- Recommends movies based on user viewing history and preferences.  
- Uses **Matrix Factorization techniques** (such as **Singular Value Decomposition (SVD)**) for better accuracy.  

### 🔹 User Interaction  
- Allows users to input a **favorite movie title** and get a list of similar movies.  
- Provides recommendations based on **user ratings and viewing history**.  
- Can be extended to support **user authentication and profile-based suggestions**.  

### 🔹 Visualization & Insights  
- Generates **interactive visualizations** to explore trends in popular genres, ratings, and user preferences.  
- Uses **Matplotlib and Seaborn** to create **genre distributions, rating trends, and correlation matrices**.  

### 🔹 API Deployment  
- Implements a **Flask-based API** to serve recommendations in real-time.  
- Supports integration with **web applications and mobile apps** via REST API.  

---

## 🚀 Technologies Used  
| Technology | Purpose |  
|------------|---------|  
| **Python** | Core programming language |  
| **Pandas, NumPy** | Data cleaning and processing |  
| **Scikit-Learn** | Machine learning models (TF-IDF, Cosine Similarity, KNN) |  
| **NLTK, TF-IDF Vectorizer** | Natural Language Processing |  
| **Flask** | Web API development |  
| **Matplotlib, Seaborn** | Data visualization |  
| **Jupyter Notebook** | Interactive development and testing |  

---

## 📂 Dataset  
The project uses the **IMDB dataset**, which includes:  
- **Movie Titles**  
- **Genres**  
- **Directors and Cast**  
- **User Ratings**  
- **Plot Summaries**  

The dataset is either obtained from **IMDB's official sources** or publicly available datasets such as **Kaggle’s IMDB dataset**.  

---

## 🛠️ Setup & Installation  

1️⃣ **Clone the Repository:**  
```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

2️⃣ **Create a Virtual Environment & Install Dependencies:**  
```bash
pip install -r requirements.txt
```

3️⃣ **Run the Jupyter Notebook for Data Exploration:**  
```bash
jupyter notebook
```

4️⃣ **Start the Flask API for Recommendations:**  
```bash
python app.py
```

---

## 🎯 How to Use?  
- **Option 1: Jupyter Notebook** – Run the scripts to generate recommendations.  
- **Option 2: Flask API** – Send a request to the API with a movie title, and it returns a list of similar movies.  

Example API request:  
```bash
curl -X GET "http://127.0.0.1:5000/recommend?title=Inception"
```

---

## 📌 Future Enhancements  
- ✅ **Deep Learning-based Recommendations** using Neural Networks.  
- ✅ **Hybrid Filtering Approach** combining Content-Based & Collaborative Filtering.  
- ✅ **User Authentication & Personalized Profiles** for better recommendations.  
- ✅ **Dockerization & Cloud Deployment** for scalable usage.  

---

## 🤝 Contributions  
Contributions are welcome! If you'd like to improve this project, please:  
1. **Fork the repository**  
2. **Create a new branch**  
3. **Commit your changes**  
4. **Submit a Pull Request (PR)**  

---

## 📜 License  
This project is licensed under the **MIT License** – feel free to use and modify it.  

---
