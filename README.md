# 🎓 Acadivanta

### Student Analytics & Intelligence
**Student Academic Outcome & Dropout Prediction**

**Predict. Understand. Improve.**

Choose your language / भाषा चुनें :

[🇬🇧 English](#english) | [🇮🇳 हिंदी](#हिंदी) 

---

## English

Acadivanta is a machine-learning project that analyses historical student data to estimate academic outcomes, identify students who may need additional support, and estimate second-semester grades.

This is an educational decision-support project. Predictions are estimates, not definitive judgments about any student's future.

### Project objectives

- Predict one of three academic outcomes: **Dropout, Enrolled, or Graduate**.
- Estimate the probability of the **Dropout** class.
- Estimate second-semester grades from admission and first-semester information.
- Demonstrate an end-to-end machine-learning workflow, from data exploration to a Streamlit application.

### Main features

1. **Multiclass Classification:** Predicts `Dropout`, `Enrolled`, or `Graduate`.
2. **Binary Classification:** Estimates the probability that a record belongs to the `Dropout` class.
3. **Regression:** Estimates the second-semester grade using admission and first-semester features.
4. **Streamlit Application:** Includes a dashboard, student prediction form, and project information page.

### Dataset

**Dataset:** [Predict Students' Dropout and Academic Success](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

- Records: **4,424**
- Original columns: **37**
- Model input features: **30**
- Multiclass target: `Target`

Classification models use admission and first-semester information. Second-semester features are excluded from model inputs to reduce target leakage.

The regression model is trained only on records with a positive recorded second-semester grade (**3,554 records**). Its estimates therefore apply conditionally to this subset, not to records with a zero second-semester grade.

### Machine-learning models

| Task | Selected model |
|---|---|
| Multiclass classification | Logistic Regression |
| Binary classification | Logistic Regression |
| Regression | Random Forest Regressor |

### Model performance

Results are from the project's held-out test split.

| Task | Metric | Result |
|---|---|---:|
| Multiclass classification | Accuracy | 74.92% |
| Binary classification | Accuracy | 86.55% |
| Binary classification | Precision (Dropout class) | 85.4% |
| Binary classification | Recall (Dropout class) | 70.1% |
| Regression | MAE | 0.713 |
| Regression | RMSE | 0.929 |
| Regression | R² | 0.534 |

These metrics describe performance on test data and do not guarantee the same performance on new students.

### Technologies

- Python
- Pandas and NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

### Project structure

```text
Acadivanta/
├── README.md
├── app.py
├── FirstAI.ipynb
├── data.csv
├── multiclass_model.pkl
├── binary_model.pkl
└── regression_model.pkl
```

### Setup and run

Run these commands from the project directory:

```bash
pip install pandas numpy matplotlib scikit-learn streamlit joblib
python -m streamlit run app.py
```

Keep `app.py`, `data.csv`, and all three `.pkl` model files in the project directory. Ideally, use the same Scikit-learn version for running the app as the version used to train and save the models.

### Application pages

- **Dashboard:** Project overview and model performance.
- **Student Prediction:** Enter student information and view model estimates.
- **About Project:** Project objectives, features, and technologies.

### Limitations and responsible use

- Models learn patterns from historical data and may not generalize to every student or institution.
- The three models perform different tasks, so their outputs may not always agree.
- A predicted outcome or probability is not a certainty.
- Use results only as one input for supportive academic guidance, with human review.

### Author

**Shashank Parmar**

[LinkedIn Profile](https://www.linkedin.com/in/shashankmeaw/)

[⬆ Back to language selection](#-acadivanta)

---

## हिंदी

Acadivanta एक मशीन लर्निंग प्रोजेक्ट है, जो पुराने विद्यार्थी डेटा का विश्लेषण करके संभावित शैक्षणिक परिणामों का अनुमान लगाता है। इसका उद्देश्य उन विद्यार्थियों की पहचान में सहायता करना है जिन्हें अतिरिक्त शैक्षणिक सहयोग की आवश्यकता हो सकती है। यह दूसरे सेमेस्टर के ग्रेड का अनुमान भी लगाता है।

यह प्रोजेक्ट शैक्षणिक सहायता और सीखने के उद्देश्य से बनाया गया है। इसके अनुमान निश्चित फैसले नहीं हैं और इन्हें किसी विद्यार्थी के भविष्य का अंतिम निर्णय नहीं मानना चाहिए।

### प्रोजेक्ट के उद्देश्य

- तीन संभावित परिणामों का अनुमान लगाना: **Dropout, Enrolled या Graduate**।
- विद्यार्थी के **Dropout** श्रेणी में आने की संभावना का अनुमान लगाना।
- एडमिशन और पहले सेमेस्टर की जानकारी से दूसरे सेमेस्टर के ग्रेड का अनुमान लगाना।
- डेटा विश्लेषण से लेकर Streamlit ऐप तक मशीन लर्निंग की पूरी प्रक्रिया दिखाना।

### मुख्य सुविधाएँ

1. **Multiclass Classification:** विद्यार्थी के परिणाम को `Dropout`, `Enrolled` या `Graduate` में वर्गीकृत करता है।
2. **Binary Classification:** `Dropout` श्रेणी में आने की अनुमानित संभावना बताता है।
3. **Regression:** एडमिशन और पहले सेमेस्टर की जानकारी के आधार पर दूसरे सेमेस्टर के ग्रेड का अनुमान लगाता है।
4. **Streamlit ऐप:** इसमें Dashboard, Student Prediction फॉर्म और About Project पेज शामिल हैं।

### डेटासेट

**डेटासेट:** [Predict Students' Dropout and Academic Success](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

- कुल रिकॉर्ड: **4,424**
- मूल कॉलम: **37**
- मॉडल के इनपुट फीचर: **30**
- Multiclass target: `Target`

Classification मॉडल में एडमिशन और पहले सेमेस्टर की जानकारी का उपयोग किया गया है। Target leakage कम करने के लिए दूसरे सेमेस्टर के फीचर इनपुट से बाहर रखे गए हैं।

Regression मॉडल केवल उन रिकॉर्ड पर ट्रेन किया गया है जिनमें दूसरे सेमेस्टर का दर्ज ग्रेड शून्य से अधिक है (**3,554 रिकॉर्ड**)। इसलिए इसका अनुमान इसी समूह पर लागू होता है, शून्य ग्रेड वाले रिकॉर्ड पर नहीं।

### उपयोग किए गए मशीन लर्निंग मॉडल

| कार्य | चुना गया मॉडल |
|---|---|
| Multiclass classification | Logistic Regression |
| Binary classification | Logistic Regression |
| Regression | Random Forest Regressor |

### मॉडल का प्रदर्शन

नीचे दिए गए परिणाम test split पर आधारित हैं।

| कार्य | मापदंड | परिणाम |
|---|---|---:|
| Multiclass classification | Accuracy | 74.92% |
| Binary classification | Accuracy | 86.55% |
| Binary classification | Precision (Dropout class) | 85.4% |
| Binary classification | Recall (Dropout class) | 70.1% |
| Regression | MAE | 0.713 |
| Regression | RMSE | 0.929 |
| Regression | R² | 0.534 |

ये मापदंड test data पर मॉडल के प्रदर्शन को दर्शाते हैं। नए विद्यार्थियों के लिए समान प्रदर्शन की गारंटी नहीं है।

### उपयोग की गई तकनीकें

- Python
- Pandas और NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

### प्रोजेक्ट की फाइलें

```text
Acadivanta/
├── README.md
├── app.py
├── FirstAI.ipynb
├── data.csv
├── multiclass_model.pkl
├── binary_model.pkl
└── regression_model.pkl
```

### इंस्टॉलेशन और चलाने का तरीका

प्रोजेक्ट फोल्डर में टर्मिनल खोलकर ये कमांड चलाएँ:

```bash
pip install pandas numpy matplotlib scikit-learn streamlit joblib
python -m streamlit run app.py
```

`app.py`, `data.csv` और तीनों `.pkl` मॉडल फाइलें एक ही प्रोजेक्ट फोल्डर में रखें। बेहतर होगा कि ऐप चलाते समय Scikit-learn का वही version इस्तेमाल करें जिससे मॉडल ट्रेन और सेव किए गए थे।

### ऐप के पेज

- **Dashboard:** प्रोजेक्ट का परिचय और मॉडल का प्रदर्शन।
- **Student Prediction:** विद्यार्थी की जानकारी दर्ज करके अनुमान देखना।
- **About Project:** प्रोजेक्ट के उद्देश्य, सुविधाएँ और तकनीकें।

### सीमाएँ और जिम्मेदार उपयोग

- मॉडल पुराने डेटा के पैटर्न सीखते हैं; हर विद्यार्थी या संस्थान के लिए परिणाम समान हों, यह जरूरी नहीं है।
- तीनों मॉडल अलग-अलग काम करते हैं, इसलिए उनके परिणाम हमेशा एक-दूसरे से मेल नहीं खा सकते।
- अनुमान को निश्चित सत्य नहीं मानना चाहिए।
- परिणामों का उपयोग केवल शैक्षणिक सहयोग के एक संकेत के रूप में, मानवीय समीक्षा के साथ करें।

### लेखक

**Shashank Parmar**

[LinkedIn Profile](https://www.linkedin.com/in/shashankmeaw/)

[⬆ भाषा चयन पर वापस जाएँ](#-acadivanta)

---

