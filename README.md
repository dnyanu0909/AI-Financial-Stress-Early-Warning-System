# AI Financial Stress Early Warning System

## Overview

This project implements an AI-powered chatbot that detects early signs of financial stress from user messages and provides risk analysis with financial advice.

The system uses Natural Language Processing (NLP) and Machine Learning to classify financial stress levels and identify potential financial risks such as debt pressure, overspending, or low savings.

## Problem Statement

Many individuals experience financial stress but fail to recognize early warning signs. This system aims to detect financial stress signals from user conversations and provide proactive financial guidance.

## Features

* Financial stress detection using NLP
* Risk score calculation (0–100 scale)
* Multi-signal financial issue detection
* AI-based chatbot interaction
* Web interface using Streamlit
* Personalized financial advice generation

## Machine Learning Pipeline

Dataset → Text Preprocessing → TF-IDF Vectorization → Logistic Regression Model → Stress Prediction

## System Architecture

User Input
↓
Streamlit Interface
↓
Stress Prediction Model
↓
Signal Detection Engine
↓
Risk Scoring Engine
↓
Financial Advice Generator
↓
User Output

## Dataset

A custom dataset of labeled financial statements was created containing:

* No_Stress
* Mild_Stress
* High_Stress

Each sentence also includes a financial signal label such as:

* overspending
* loan_pressure
* low_savings
* debt
* investment

## Model Used

Logistic Regression with TF-IDF feature extraction.

This approach was chosen because it performs well for small text classification datasets.

## Example Output

Input:
"I cannot pay my credit card bill this month"

Output:

Financial Risk Score: 95
Risk Level: High_Stress
Detected Issues: debt
Advice: Reduce credit card usage and create a debt repayment plan.

## Technologies Used

* Python
* Scikit-learn
* Streamlit
* Pandas
* Natural Language Processing (TF-IDF)

## Project Structure

financial_stress_ai_project
│
├── Dataset
├── models
│   ├── stress_model.pkl
│   └── vectorizer.pkl
│
├── src
│   ├── train_model.py
│   ├── chatbot.py
│   └── app.py

## Future Improvements

* Expand dataset for better model accuracy
* Implement transformer-based NLP models (BERT)
* Add sentiment analysis for emotional financial stress
* Connect with financial budgeting tools

## Author

AI & Machine Learning Project by Dnyaneshwari Gandhre

## Application Interface

![App Screenshot](screenshots/app.png)