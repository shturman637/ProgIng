from transformers import pipeline

classifier  = pipeline("sentiment-analysis", "cointegrated/rubert-tiny2-cedr-emotion-detection")

classifier("Праздник к нам приходит")
