import pandas as pd
import random

data = []

# sentence templates
templates = [
    "I {} my {}",
    "I usually {} my {}",
    "Sometimes I {} my {}",
    "I often {} my {}",
    "I struggle to {} my {}"
]

# financial signals
signals = {

"No_Stress": {
"financial_control": [
("track","expenses"),
("manage","budget"),
("monitor","spending")
],

"savings_habit": [
("save","income"),
("set aside","money"),
("build","savings")
],

"investment": [
("invest","earnings"),
("grow","investments"),
("add to","portfolio")
]
},

"Mild_Stress": {
"overspending": [
("overspend on","shopping"),
("spend too much on","online purchases"),
("buy unnecessary","items")
],

"income_pressure": [
("stretch","salary"),
("manage","monthly income"),
("adjust","budget")
],

"low_savings": [
("struggle to build","savings"),
("delay","saving money"),
("save little from","income")
]
},

"High_Stress": {
"debt": [
("cannot pay","credit card bill"),
("miss","loan payment"),
("struggle with","debt")
],

"loan_pressure": [
("worry about","loan repayment"),
("stress over","EMI payments"),
("panic about","loan balance")
],

"cash_shortage": [
("run out of","money"),
("have almost no","savings"),
("lack","cash reserves")
]
}

}

# generate sentences
for label in signals:
    
    for signal in signals[label]:
        
        for verb,obj in signals[label][signal]:
            
            for template in templates:
                
                sentence = template.format(verb,obj)
                data.append([sentence,label,signal])

# shuffle dataset
random.shuffle(data)

# convert to dataframe
df = pd.DataFrame(data, columns=["text","label","signal"])

# save CSV
df.to_csv("financial_stress_dataset.csv",index=False)

print("Dataset generated!")
print("Total rows:",len(df))