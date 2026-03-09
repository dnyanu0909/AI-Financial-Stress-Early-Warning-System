import pandas as pd
import os
from transformers import pipeline

# paraphrasing model
paraphraser = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")

data = []

# Base sentences
base_sentences = {
    
"No_Stress": [
("I track my expenses every month","financial_control"),
("I save a portion of my salary regularly","savings_habit"),
("I maintain an emergency fund for unexpected costs","emergency_fund"),
("I follow a monthly budget plan","financial_planning"),
("My income comfortably covers my expenses","income_stability"),
("I avoid unnecessary purchases","spending_control"),
("I invest part of my earnings for the future","investment"),
("I review my bank statements regularly","financial_awareness"),
("I pay my credit card bill in full every month","debt_management"),
("I plan big purchases in advance","financial_planning"),
("I always keep some money aside for emergencies","emergency_fund"),
("I rarely make impulsive purchases","spending_control"),
("I know exactly where my money goes each month","financial_awareness"),
("I regularly update my financial budget","financial_planning"),
("I keep my spending within limits","spending_control"),
("I save money automatically from my salary","savings_habit"),
("I plan my financial goals yearly","financial_planning"),
("I maintain a good balance between spending and saving","financial_balance"),
("I review my financial goals frequently","financial_planning"),
("I maintain healthy savings habits","savings_habit"),
("I always pay my bills on time","financial_discipline"),
("I track investments regularly","investment"),
("I avoid unnecessary debt","debt_management"),
("I build my savings every month","savings_habit"),
("I manage my money responsibly","financial_control")
],

"Mild_Stress": [
("My salary barely lasts until the end of the month","income_pressure"),
("I sometimes spend more than I planned","overspending"),
("I occasionally rely on my credit card for expenses","credit_usage"),
("I struggle to save money consistently","low_savings"),
("I buy things online even when not necessary","impulse_buying"),
("My monthly expenses are slowly increasing","expense_growth"),
("I find it difficult to stick to my budget","budget_control"),
("I wonder where my money goes every month","spending_tracking"),
("I delay saving because of daily expenses","savings_delay"),
("I feel slightly worried about my finances","financial_anxiety"),
("I occasionally exceed my monthly budget","overspending"),
("I sometimes regret unnecessary purchases","regret_spending"),
("I find saving money difficult these days","low_savings"),
("Unexpected expenses affect my budget","expense_growth"),
("My savings progress is very slow","low_savings"),
("My spending habits are hard to control","spending_control"),
("I occasionally depend on credit cards","credit_usage"),
("I spend impulsively during sales","impulse_buying"),
("I sometimes struggle with financial planning","financial_planning"),
("I worry about future expenses","financial_anxiety"),
("I often delay financial decisions","financial_planning"),
("I struggle to keep expenses under control","budget_control"),
("My income barely covers my spending","income_pressure"),
("I sometimes feel uncertain about my finances","financial_anxiety"),
("I find it hard to increase my savings","low_savings")
],

"High_Stress":[
("I cannot pay my credit card bill this month","debt"),
("My loan EMI payments are difficult to manage","loan_pressure"),
("I have almost no savings left","zero_savings"),
("I am constantly worried about money","financial_anxiety"),
("Most of my income goes into paying debts","debt_cycle"),
("I missed my loan payment this month","missed_payment"),
("My bank balance is almost zero","cash_shortage"),
("I rely on credit cards to survive","credit_dependency"),
("I feel overwhelmed by my debts","debt_stress"),
("I don't know how I will pay my bills","bill_pressure"),
("My debt keeps increasing every month","debt_cycle"),
("I struggle to manage loan repayments","loan_pressure"),
("My financial situation feels out of control","financial_anxiety"),
("I cannot save any money at all","zero_savings"),
("I am falling behind on my payments","missed_payment"),
("I constantly borrow money to manage expenses","credit_dependency"),
("My financial stress is overwhelming","financial_anxiety"),
("My expenses are greater than my income","cash_shortage"),
("My debt burden keeps growing","debt_cycle"),
("I cannot manage my financial obligations","bill_pressure"),
("I worry about defaulting on my loan","loan_pressure"),
("I feel trapped in debt","debt_stress"),
("My credit card balance is unmanageable","debt"),
("I am struggling to survive financially","cash_shortage"),
("My finances are in serious trouble","financial_crisis")
]
}

for label in base_sentences:
    
    for text,signal in base_sentences[label]:

        prompt = f"paraphrase: {text} </s>"
        outputs = paraphraser(prompt,max_length=60,num_return_sequences=5,do_sample=True,temperature=0.8)
        data.append([text,label,signal])

        for o in outputs:
            sentence = o["generated_text"].strip()
            data.append([sentence,label,signal])

# create dataframe
df = pd.DataFrame(data, columns=["text","label","signal"])

# remove duplicate sentences
df = df.drop_duplicates(subset="text")

# save dataset
df.to_csv("financial_stress_dataset.csv", index=False)

print("Dataset size:", len(df))
print("Dataset generated successfully!")
print("Saved at:", os.getcwd())