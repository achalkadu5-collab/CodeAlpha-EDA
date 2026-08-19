# 📊 Task 3 – Sentiment Analysis Dashboard

## 📌 Project Overview

This project is developed as part of my **CodeAlpha Data Analytics Internship – Task 3**.

The project focuses on analyzing customer reviews using **Sentiment Analysis**. It classifies reviews into three categories:

* 😊 Positive
* 😐 Neutral
* 😞 Negative

The sentiment analysis is performed using **TextBlob**, and an interactive dashboard is created using **Streamlit** to visualize and explore the results.

---

## 🎯 Objective

The main objective of this project is to analyze customer reviews and identify the sentiment expressed in each review.

The project aims to:

* Analyze customer review data
* Calculate sentiment polarity
* Classify reviews into Positive, Negative, and Neutral
* Visualize sentiment distribution
* Provide an interactive dashboard
* Generate useful insights from customer feedback

---

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data loading and data analysis
* **TextBlob** – Sentiment analysis
* **Streamlit** – Interactive dashboard
* **Jupyter Notebook** – Data analysis and experimentation

---

## 📂 Dataset

The dataset used in this project is:

**`CodeAlpha_Sentiment_Reviews.csv`**

The dataset contains customer review information that is analyzed to determine the sentiment of each review.

Dataset location:

```text
data/CodeAlpha_Sentiment_Reviews.csv
```

---

## 🔄 Methodology

The project follows these steps:

```text
Customer Reviews Dataset
          ↓
      Data Loading
          ↓
     Data Processing
          ↓
     TextBlob Analysis
          ↓
   Polarity Calculation
          ↓
 Sentiment Classification
          ↓
 Streamlit Dashboard
          ↓
 Visualization & Insights
```

---

## ⭐ Sentiment Analysis

TextBlob is used to calculate the **polarity** of each review.

The polarity score ranges from **-1 to +1**.

| Polarity       | Sentiment   |
| -------------- | ----------- |
| Greater than 0 | 😊 Positive |
| Equal to 0     | 😐 Neutral  |
| Less than 0    | 😞 Negative |

### Example

```text
Review:
"This product is excellent and very useful."

Sentiment:
Positive
```

---

## 🚀 Features

### 1. Sentiment Classification

The system automatically classifies customer reviews into:

* Positive
* Negative
* Neutral

### 2. Polarity Analysis

TextBlob calculates the polarity score of each review.

### 3. Sentiment Distribution

The dashboard displays the distribution of different sentiment categories.

### 4. Interactive Dashboard

The Streamlit dashboard provides an interactive interface to explore the sentiment analysis results.

### 5. Reviews Table

The dashboard displays the analyzed reviews along with their sentiment information.

### 6. Data Visualization

Charts and visual elements are used to make the sentiment results easier to understand.

---

## 📈 Results

After processing the dataset, each review is assigned:

* A polarity score
* A sentiment category

The dashboard provides an overview of the overall sentiment of the customer reviews.

This makes it easier to understand customer opinions and identify whether the feedback is mostly positive, negative, or neutral.

---

## 🖥️ Streamlit Dashboard

The interactive dashboard is developed using **Streamlit**.

The dashboard allows users to:

* View sentiment statistics
* Explore sentiment distribution
* View analyzed customer reviews
* Understand overall customer feedback

### Run the Dashboard

Open the terminal inside the `Task_3_Sentiment_Analysis` folder and run:

```bash
streamlit run sentiment_dashboard.py
```

Streamlit will start the application and provide a local URL in the terminal.

Open that URL in your browser to view the dashboard.

---

## ⚙️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/achalkadu5-collab/CodeAlpha-EDA
```

### Step 2: Navigate to Task 3 Folder

```bash
cd Task_3_Sentiment_Analysis
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Dashboard

```bash
streamlit run sentiment_dashboard.py
```

### Step 5: Open the Dashboard

Open the local Streamlit URL shown in the terminal.

---

## 📁 Project Structure

```text
Task_3_Sentiment_Analysis/
│
├── data/
│   └── CodeAlpha_Sentiment_Reviews.csv
│
├── sentiment_analysis.ipynb
├── sentiment_dashboard.py
├── README.md
└── requirements.txt
```

---

## 📦 Requirements

The main Python libraries used in this project are:

```text
pandas
textblob
streamlit
```

The required dependencies are listed in:

```text
requirements.txt
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 💡 Applications

Sentiment Analysis can be used in various real-world applications, such as:

* Customer feedback analysis
* Product review analysis
* Customer satisfaction analysis
* Social media sentiment analysis
* Brand reputation monitoring
* Market research

---

## 🌟 Advantages

* Automates review analysis
* Saves manual analysis time
* Easy sentiment classification
* Interactive dashboard
* Simple and user-friendly interface
* Helps understand customer opinions quickly

---

## 📝 Conclusion

The **Sentiment Analysis Dashboard** demonstrates how Python and Natural Language Processing techniques can be used to analyze customer reviews.

Using **Pandas, TextBlob, and Streamlit**, the project processes review data, calculates sentiment polarity, classifies reviews, and presents the results through an interactive dashboard.

This project provided practical experience in **Data Analytics, Natural Language Processing, Sentiment Analysis, Data Visualization, and Streamlit Dashboard Development** as part of the **CodeAlpha Data Analytics Internship**.

---

## 👨‍💻 Author

**Achal Kadu**

BCA Graduate | Aspiring Python Developer | Data Analytics & AI/ML Enthusiast

---

## 🏢 Internship

**CodeAlpha – Data Analytics Internship**

**Task 3: Sentiment Analysis**

