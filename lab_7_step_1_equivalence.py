import json
json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr"
        }
    ]
}
"""
json_input = json.loads(json_string)

SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

if SourceLanguageCode == TargetLanguageCode:
    print('SourceLanguageCode is same as TargetLanguage Code --Stopping')
else:
    print('Source Language Code and Target Language code are different - proceeding')
