import os
import streamlit as st
import pickle

# Get the absolute path to the directory where app.py lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build absolute paths to the models folder (which is one level up from 'src')
model_path = os.path.join(BASE_DIR, "..", "models", "stress_model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "..", "models", "vectorizer.pkl")

# Load files
model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))

# title
st.title("AI Financial Stress Early Warning System")

st.write("Enter a financial message to evaluate risk.")

# user input
user_input = st.text_input("Your financial message")

def predict_stress(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    return prediction

# simple signal detector
def detect_signal(text):

    text = text.lower()

    signal_keywords = {
        "overspending": ["spend","shopping","buy","purchase","expenses"],
        "low_savings": ["no savings","low savings","almost zero savings"],
        "income_pressure": ["salary ends","income not enough","manage expenses"],
        "loan_pressure": ["loan","emi"],
        "debt": ["debt","credit card"],
        "cash_shortage": ["no money","run out of money"],
        "investment": ["invest","portfolio"],
        "financial_control": ["budget","track expenses"]
    }

    detected = []

    for signal, words in signal_keywords.items():
        for word in words:
            if word in text:
                detected.append(signal)
                break

    if not detected:
        return ["general"]

    return detected


def calculate_risk_score(level, signals):

    base_scores = {
        "No_Stress":20,
        "Mild_Stress":50,
        "High_Stress":80
    }

    signal_adjustment = {
        "overspending":5,
        "low_savings":10,
        "income_pressure":10,
        "loan_pressure":15,
        "debt":15,
        "cash_shortage":20,
        "investment":-10,
        "financial_control":-10
    }

    score = base_scores.get(level,50)

    for signal in signals:
        score += signal_adjustment.get(signal,0)

    score = max(0,min(score,100))

    return score

def generate_advice(signals):

    advice_map = {

        "overspending": "Reduce discretionary spending and track purchases weekly.",
        "low_savings": "Start building an emergency fund by saving at least 10% of your income.",
        "income_pressure": "Review monthly expenses and identify areas where you can reduce spending.",
        "loan_pressure": "Prioritize loan repayment and avoid taking new debt.",
        "debt": "Reduce credit card usage and create a structured debt repayment plan.",
        "cash_shortage": "Create a strict monthly budget and maintain a cash buffer.",
        "investment": "Continue investing regularly and diversify your portfolio.",
        "financial_control": "Good financial discipline. Continue budgeting and tracking expenses."
    }

    advice_list = []

    for signal in signals:
        advice_list.append(advice_map.get(signal, "Review your financial habits."))

    return advice_list

if user_input:

    level = predict_stress(user_input)

    signals = detect_signal(user_input)

    score = calculate_risk_score(level, signals)

    advice = generate_advice(signals)

    st.subheader("Financial Risk Score")
    st.write(score,"/100")

    st.subheader("Risk Level")
    st.write(level)

    st.subheader("Detected Issues")
    st.write(", ".join(signals)) 
    
    st.subheader("Advice")

    for a in advice:
        st.write("-", a)