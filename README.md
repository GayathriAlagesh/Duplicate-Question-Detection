# Duplicate-Question-Detection
To detect the duplicate question by segregate into bucket by using the cosine similarity of each question and remove that duplicate question from each bucket

# Packages installation 

pip install nltk    # This will install the natural language processing toolkit

import nltk
nltk.download('punkt')
nltk.download('stopwords')   # Download punkt and stopwords from nltk to remove the stopwords

pip install lxml    # To take the questions from the website we want lxml package 

pip install requests   # To get the webpage want to give requests 

Import all the packages we istall 

Run the Duplicate_Detection.py file 

The Tkinter window will be open and tell that you want to find the duplicate question click the start button 

if you click the start button the another Tkinter window will be opened and ask the website link and the container which will have the list of questions

give the details and click Next button 

then,It will give the question based on the accuracy of the duplication bucket by bucket with unique questions 




