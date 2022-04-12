import boto3

#DateCreated: 12/4/2022

#THIS PROGRAM MAKES USE OF AWS TRANSLATE SERVICE TO TRANSLATE TEXT FROM ENGLISH TO FRENCH LANGUAGE.
client = boto3.client('translate')

#### Add the new text below this line ####

def translate_text(text, targetlang, sourcelang='en'): # declare the function using def, name, braces for parameters and a colon  
    response = client.translate_text(
        Text=text, # Assigning the value of the string to the variable Text
        SourceLanguageCode=sourcelang, # We are using a two letter language code from the documentation (en = English)
        TargetLanguageCode=targetlang # We use a second two letter language code from the documentation (fr = French)
    )
    print(response) # this code is inside the function and will print the contents of the variable 'response' 



if __name__ == "__main__":
    text = str(input("Enter the Text you wish to Translate: "))
    targetlang = str(input("Enter your Target Language: "))
    translate_text(text, targetlang) # This line will call our function. Without it, python will not do anything.