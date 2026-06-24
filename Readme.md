# 🛒 SmartCart Customer Segmentation

A Machine Learning-based customer segmentation system for e-commerce businesses using **Unsupervised Learning**. This project analyzes customer demographics, spending behavior, and purchasing patterns to group customers into meaningful segments for targeted marketing and business insights.

---

## 📌 Project Overview

SmartCart Customer Segmentation helps businesses understand their customers by grouping them into clusters based on their purchasing habits, income, engagement, and demographics. The project uses **K-Means Clustering** and **Agglomerative Clustering** along with **Principal Component Analysis (PCA)** for dimensionality reduction and visualization.

---

## 🚀 Features

- 📊 Exploratory Data Analysis (EDA)
- 🛠 Data Cleaning and Preprocessing
- 🔧 Feature Engineering
- 📈 Customer Behavior Analysis
- 📉 Principal Component Analysis (PCA)
- 🤖 K-Means Clustering
- 🌳 Agglomerative Clustering
- 📊 Cluster Visualization
- 🌐 Interactive Streamlit Frontend
- ⚡ Real-Time Customer Segment Prediction

---

## 📂 Dataset Features

### Customer Demographics
- Income
- Age
- Total_Children
- Education_Graduate
- Education_Postgraduate
- Education_Undergraduate
- Living_With_Alone
- Living_With_Partner

### Customer Behavior
- Recency
- NumDealsPurchases
- NumWebPurchases
- NumCatalogPurchases
- NumStorePurchases
- NumWebVisitsMonth
- Total_Spending

### Customer Engagement
- Response
- Complain
- Customer_Tenure_Days

---

## 🧠 Machine Learning Techniques Used

### K-Means Clustering
Used for segmenting customers into 4 clusters.

### Agglomerative Clustering
Used for hierarchical cluster analysis and comparison.

### PCA (Principal Component Analysis)
Used for dimensionality reduction and cluster visualization.

---

## 📊 Cluster Categories

### ⭐ Cluster 0: High-Value Customers
- High income
- High spending
- Frequent purchases
- Loyal customers

### 🛍️ Cluster 1: Average Customers
- Moderate income
- Moderate spending
- Regular buyers

### 💸 Cluster 2: Frequent Deal Seekers
- Price-sensitive customers
- Purchase mainly during discounts
- High number of deal purchases

### 📉 Cluster 3: Low Engagement Customers
- Low spending
- Less active customers
- Infrequent purchases

---

## 🧰 Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- Streamlit

---

## 📁 Project Structure

```text
SmartCart-Customer-Segmentation/
│
├── app.py                  # Streamlit Application
├── smartcart.ipynb         # Jupyter Notebook
├── smartcart_customer.csv  # Dataset
├── scaler.pkl             # Standard Scaler
├── pca.pkl                # PCA Model
├── kmeans_model.pkl       # K-Means Model
├── requirements.txt       # Dependencies
├── README.md              # Documentation
└── images/                # Screenshots (Optional)
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/SmartCart-Customer-Segmentation.git
```

Move to the project directory:

```bash
cd SmartCart-Customer-Segmentation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

🔗 Streamlit App:

```text
Add your Streamlit app URL here
```

---

## 📸 Application Features

- Input customer information
- Analyze customer behavior
- Identify customer segment
- Display cluster insights
- Interactive and user-friendly interface

---

## 🎯 Future Enhancements

- Dashboard Analytics
- Interactive Cluster Visualization
- Customer Recommendation System
- CSV Upload Feature
- Marketing Campaign Suggestions
- Business Intelligence Dashboard

---

## 👨‍💻 Author

**Prajwal Kumbhare**

- B.Tech CSE (Data Science)
- Machine Learning Enthusiast
- Full Stack Developer
- Interested in AI, Data Science, and Software Development

---

## ⭐ If you found this project useful, don't forget to star the repository!
