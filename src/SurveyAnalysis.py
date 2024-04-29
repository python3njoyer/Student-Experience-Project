import csv
import re
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


response = []
# Open csv and add survey responses to list
with open('Remote Learning 2020 Student Survey.csv', 'r', encoding='utf-8') as readfile:
    surveyData = csv.reader(readfile)
    next(surveyData)
    for row in surveyData:
        response.append(row[10])


# Merge responses into one long string
response = ' '.join(response)
response = ' ' + response + ' '


punctuation = string.punctuation
punctuation = re.sub(('\''), '', punctuation)
commonWords = ['like', 'in-person', 'miss', 'could', 'class', 'able']

# Make lowercase, remove stopwords and meaningless words, remove punctuation
def clean_text(text):
    text = text.lower()
    for word in stopwords.words('english'):
        text = re.sub(' ' + word + ' ', ' ', text)
    for word in commonWords:
        text = re.sub(' ' + word + ' ', ' ', text)
    for char in punctuation:
        text = re.sub(re.escape(char), ' ', text)
    return text

response = clean_text(response)


# Tokenize responses
response = response.split()


# Change all verbs into root form
def lemmatize(text):
    output = []
    for verb in text:
        verb = WordNetLemmatizer().lemmatize(verb, pos='v')
        output.append(verb)
    return output

response = lemmatize(response)


# Write to text file for visualization
with open(r'C:\Users\eliza\PycharmProjects\ODL\cleaned.txt', 'w') as file:
    for word in response:
        file.write(word + ' ')
