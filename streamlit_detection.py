import base64
import streamlit as st
from transformers import pipeline

st.title ("Приложение для определения эмоциональной окраски введенного текста")

# Инициализация модели
classifier = pipeline("sentiment-analysis", "cointegrated/rubert-tiny2-cedr-emotion-detection")

# Поле для ввода текста
text = st.text_input("Введите текст для анализа")

if st.button("Анализировать текст"):
   result = classifier(text)[0]
   label = result['label']
   score = result['score']
   
   if label == 'POSITIVE':
       st.success(f'{label} sentiment (score: {score})')
   else:
       st.error(f'{label} sentiment (score: {score})')


# Устанавливаем фон 

