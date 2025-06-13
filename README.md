# Customer Sentiment Explorer

This project is a user-friendly sentiment analysis web app built using Python and Streamlit. It allows users to enter any text—such as customer reviews, tweets, or comments—and instantly determines if the sentiment is Positive, Negative, or Neutral.

---

## Features

- Easy-to-use web interface powered by Streamlit  
- Real-time sentiment predictions  
- Uses basic natural language processing (NLP) techniques  
- Classifier trained using scikit-learn's Logistic Regression  
- Great for analyzing social media posts or customer feedback  

---

## Files Included

- `sentiment_explorer_app.py` – Main script for the Streamlit application  
- `README.md` – Project description and instructions  

---

## Requirements

Install the following Python libraries:

```bash
pip install streamlit nltk scikit-learn
```

Also, download the necessary NLTK data:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## How to Run

1. Open your terminal or command prompt  
2. Navigate to the folder with the script  
3. Run this command:

```bash
streamlit run sentiment_explorer_app.py
```

The app will open in your browser.

---

## Example

Enter a sentence like:

> This product is amazing, I love it!

You’ll get:

> Predicted Sentiment: Positive ✅

---

## Future Ideas

- Add multi-language support  
- Connect to live Twitter feeds for trend analysis  
- Include data visualizations and charts  

---

## Contributions

Feel free to fork this project, improve the model, or suggest new features. Contributions are always welcome!
