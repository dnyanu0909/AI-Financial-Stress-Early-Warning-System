import pickle

model = pickle.load(open("../models/stress_model.pkl", "rb"))
vectorizer = pickle.load(open("../models/vectorizer.pkl", "rb"))


def predict_stress(text):
    text_lower = text.lower()
    if "no debt" in text_lower or "no loans" in text_lower:
        return "No_Stress"

    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]

    return prediction


def financial_advice(level):

    if level == "High_Stress":
        return """
⚠ High Financial Stress Detected

Possible issue: Debt or cash shortage.

Suggestions:
• Reduce non-essential spending
• Prioritize debt payments
• Create an emergency fund
"""

    elif level == "Mild_Stress":
        return """
⚠ Mild Financial Stress Detected

Suggestions:
• Review monthly budget
• Track spending
• Increase savings gradually
"""

    else:
        return """
✓ Financial Situation Stable

Suggestions:
• Continue saving
• Invest regularly
• Maintain financial discipline
"""

def detect_signal(text):

    text = text.lower()

    signal_keywords = {

        "overspending": ["spend", "shopping", "buy", "purchase", "expenses"],
        "low_savings": ["save little","no savings","low savings","almost zero savings","savings are almost zero","very little savings"],
        "income_pressure": ["salary ends", "income not enough", "manage my expenses"],
        "loan_pressure": ["loan", "emi"],
        "debt": ["debt", "credit card"],
        "cash_shortage": ["no money", "run out of money", "no cash"],
        "investment": ["invest", "portfolio"],
        "financial_control": ["budget", "track expenses"]
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
        "No_Stress": 20,
        "Mild_Stress": 50,
        "High_Stress": 80
    }

    signal_adjustment = {
        "overspending": 5,
        "low_savings": 10,
        "income_pressure": 10,
        "loan_pressure": 15,
        "debt": 15,
        "cash_shortage": 20,
        "investment": -10,
        "financial_control": -10
    }

    score = base_scores.get(level, 50)

    for signal in signals:
        score += signal_adjustment.get(signal, 0)

    score = max(0, min(score, 100))

    return score


def financial_advice(level, signals):

    score = calculate_risk_score(level, signals)

    advice_map = {

        "overspending": "Reduce discretionary spending and track purchases weekly.",
        "low_savings": "Start building an emergency fund by saving at least 10% of your income.",
        "income_pressure": "Review monthly expenses and identify areas where you can reduce costs.",
        "loan_pressure": "Prioritize loan repayment and avoid taking new debt.",
        "debt": "Reduce credit card usage and create a structured debt repayment plan.",
        "cash_shortage": "Create a strict monthly budget and maintain a cash buffer.",
        "investment": "Continue investing regularly and diversify your portfolio.",
        "financial_control": "Good financial discipline. Continue budgeting and tracking expenses."
    }

    advice_list = []

    for signal in signals:
        advice_list.append(advice_map.get(signal, "Review your financial habits."))

    advice_text = "\n".join(advice_list)

    signals_text = ", ".join(signals)

    return f"""
Financial Risk Score: {score}/100

Risk Level: {level}
quit
Detected Issues: {signals_text}

Advice:
{advice_text}
"""


print("AI Financial Stress Assistant")
print("Type 'quit' to exit\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    level = predict_stress(user_input)

    signal = detect_signal(user_input)

    print(financial_advice(level, signal))