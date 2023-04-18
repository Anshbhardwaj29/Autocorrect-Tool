#****************************SpellChecker tool **************************************
#Here we import textblob library to correct spelling of sentence

from textblob import TextBlob

#then we input our sentence from user 
words=input("Enter any Words:")

#It consider our output in correct form and sent it to the output terminal.
correct_words=TextBlob(words)

#Finally print the output at the terminal
print("Correct Words:",correct_words.correct())