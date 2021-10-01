import boto3
from pprintpp import pprint as pp

client = boto3.client('translate')

def translate_text():# declare the function using def, name, braces for parameters and a colon 
    response = client.translate_text(
        Text = 'I love AWS and coding', # Assigning the value of the string to the variable Text
        SourceLanguageCode = 'en',# We are using a two letter language code from the documentation (en = English)
        TargetLanguageCode= 'fr' )# We are using a two letter language code from the documentation (hi = hindi)
    pp(response)
 
def main():   
    translate_text()

if __name__=='__main__':
    main()