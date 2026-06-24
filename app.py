import streamlit as st
import numpy as np
import joblib

# Load saved objects
scaler = joblib.load("scaler.pkl")
pca = joblib.load("pca.pkl")        # Remove this line if PCA was not used
model = joblib.load("kmeans_model.pkl")

st.set_page_config(page_title="SmartCart Customer Segmentation", layout="wide")

st.title("🛒 SmartCart Customer Segmentation")
st.write("Analyze customers and identify their cluster.")

# Input fields
Income = st.number_input("Income per month")
Recency = st.number_input("Recency", min_value=0)
NumDealsPurchases = st.number_input("NumDealsPurchases", min_value=0)
NumWebPurchases = st.number_input("NumWebPurchases", min_value=0)
NumCatalogPurchases = st.number_input("NumCatalogPurchases", min_value=0)
NumStorePurchases = st.number_input("NumStorePurchases", min_value=0)
NumWebVisitsMonth = st.number_input("NumWebVisitsMonth", min_value=0)
Complain = st.selectbox("Complain", [0,1])
Response = st.selectbox("Response", [0,1])
Age = st.number_input("Age", min_value=18)
Customer_Tenure_Days = st.number_input("Customer_Tenure_Days", min_value=0)
Total_Spending = st.number_input("Total_Spending", min_value=0.0)
Total_Children = st.number_input("Total_Children", min_value=0)

Education_Graduate = st.selectbox("Education_Graduate", [0,1])
Education_Postgraduate = st.selectbox("Education_Postgraduate", [0,1])
Education_Undergraduate = st.selectbox("Education_Undergraduate", [0,1])

Living_With_Alone = st.selectbox("Living_With_Alone", [0,1])
Living_With_Partner = st.selectbox("Living_With_Partner", [0,1])

if st.button("Find Customer Segment"):

    data = np.array([[Income,
                      Recency,
                      NumDealsPurchases,
                      NumWebPurchases,
                      NumCatalogPurchases,
                      NumStorePurchases,
                      NumWebVisitsMonth,
                      Complain,
                      Response,
                      Age,
                      Customer_Tenure_Days,
                      Total_Spending,
                      Total_Children,
                      Education_Graduate,
                      Education_Postgraduate,
                      Education_Undergraduate,
                      Living_With_Alone,
                      Living_With_Partner]])

    # Scale
    data_scaled = scaler.transform(data)

    # PCA transformation
    data_pca = pca.transform(data_scaled)

    # Cluster prediction
    cluster = model.predict(data_pca)[0]

    st.success(f"Customer belongs to Cluster {cluster}")

    if cluster == 0:
        st.info("Cluster 0: High-value customers")
    elif cluster == 1:
        st.info("Cluster 1: Average customers")
    elif cluster == 2:
        st.info("Cluster 2: Frequent deal seekers")
    else:
        st.info("Cluster 3: Low engagement customers")