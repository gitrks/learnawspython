import json
import logging
json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"fr",
        "TargetLanguageCode":"fr"
        }
    ]
}
"""
json_input = json.loads(json_string)

SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']
if SourceLanguageCode == TargetLanguageCode:
    # This will print to the console as the default level is warning
    logging.warning(
        "The SourceLanguageCode is the same as the TargetLanguageCode - stopping")
else:
    # This will not print to the console because it is lower than warning
    logging.info(
        "The Source Language and Target Language codes are different - proceeding")
