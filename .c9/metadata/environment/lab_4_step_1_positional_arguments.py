{"filter":false,"title":"lab_4_step_1_positional_arguments.py","tooltip":"/lab_4_step_1_positional_arguments.py","undoManager":{"mark":2,"position":2,"stack":[[{"start":{"row":0,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["import boto3","","def translate_text(text, source_language_code, target_language_code): # we define the positional arguments in the ()","    client = boto3.client('translate')","    response = client.translate_text(","        Text=text, # we remove the hard coded value","        SourceLanguageCode=source_language_code, # we used the positional argument instead","        TargetLanguageCode=target_language_code","    )","    print(response) ","","def main():","    translate_text('I am learning to code in AWS','en','fr') # we provide the value for the arguments when we call the function in the correct positional order.","","if __name__==\"__main__\":","    main()",""],"id":1}],[{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"insert","lines":["g"],"id":2},{"start":{"row":16,"column":1},"end":{"row":16,"column":2},"action":"insert","lines":["i"]},{"start":{"row":16,"column":2},"end":{"row":16,"column":3},"action":"insert","lines":["t"]}],[{"start":{"row":16,"column":2},"end":{"row":16,"column":3},"action":"remove","lines":["t"],"id":3},{"start":{"row":16,"column":1},"end":{"row":16,"column":2},"action":"remove","lines":["i"]},{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"remove","lines":["g"]},{"start":{"row":15,"column":10},"end":{"row":16,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":36,"scrollleft":0,"selection":{"start":{"row":15,"column":10},"end":{"row":15,"column":10},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":0,"state":"start","mode":"ace/mode/python"}},"timestamp":1633066109279,"hash":"3d2fc3b184af10413e396b91eea854d4d346bb41"}