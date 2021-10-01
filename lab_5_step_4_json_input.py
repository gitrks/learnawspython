import json
# this uses json string as input
json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr",
        "Required": true
        }
    ]
}
"""


def main():
    json_input = json.loads(json_string)
    indented_output = json.dumps(json_input, indent=2)
    print(indented_output)


if __name__ == '__main__':
    main()
