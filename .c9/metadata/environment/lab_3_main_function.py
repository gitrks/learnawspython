{"filter":false,"title":"lab_3_main_function.py","tooltip":"/lab_3_main_function.py","undoManager":{"mark":18,"position":18,"stack":[[{"start":{"row":0,"column":0},"end":{"row":12,"column":16},"action":"insert","lines":["import boto3","from pprintpp import pprint as pp","","client = boto3.client('translate')","","def translate_text():# declare the function using def, name, braces for parameters and a colon ","    response = client.translate_text(","        Text = 'I love AWS and coding', # Assigning the value of the string to the variable Text","        SourceLanguageCode = 'en',# We are using a two letter language code from the documentation (en = English)","        TargetLanguageCode= 'fr' )# We are using a two letter language code from the documentation (hi = hindi)","    pp(response)","    ","translate_text()"],"id":1}],[{"start":{"row":11,"column":1},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"insert","lines":[" "]}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"remove","lines":[" "],"id":3}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":11},"action":"insert","lines":["def main():"],"id":4}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"insert","lines":["    "],"id":5}],[{"start":{"row":13,"column":20},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":6},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "],"id":7}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":8},{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":["i"]},{"start":{"row":15,"column":1},"end":{"row":15,"column":2},"action":"insert","lines":["f"]}],[{"start":{"row":15,"column":2},"end":{"row":15,"column":3},"action":"insert","lines":[" "],"id":9},{"start":{"row":15,"column":3},"end":{"row":15,"column":4},"action":"insert","lines":["n"]},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["a"]},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":["m"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"remove","lines":["e"],"id":10},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"remove","lines":["m"]},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"remove","lines":["a"]},{"start":{"row":15,"column":3},"end":{"row":15,"column":4},"action":"remove","lines":["n"]}],[{"start":{"row":15,"column":3},"end":{"row":15,"column":4},"action":"insert","lines":["_"],"id":11},{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["_"]},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":["n"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["a"]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["m"]},{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["e"]}],[{"start":{"row":15,"column":3},"end":{"row":15,"column":9},"action":"remove","lines":["__name"],"id":12},{"start":{"row":15,"column":3},"end":{"row":15,"column":11},"action":"insert","lines":["__name__"]}],[{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["="],"id":13},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":15,"column":13},"end":{"row":15,"column":15},"action":"insert","lines":["''"],"id":14}],[{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["_"],"id":15},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["_"]},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["m"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["a"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["i"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["n"]}],[{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["_"],"id":16},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["_"]}],[{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":[":"],"id":17}],[{"start":{"row":15,"column":24},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":18},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":["m"]},{"start":{"row":16,"column":5},"end":{"row":16,"column":6},"action":"insert","lines":["a"]},{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":["i"]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":7},"action":"remove","lines":["mai"],"id":19},{"start":{"row":16,"column":4},"end":{"row":16,"column":10},"action":"insert","lines":["main()"]}]]},"ace":{"folds":[],"scrolltop":36,"scrollleft":0,"selection":{"start":{"row":16,"column":9},"end":{"row":16,"column":9},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":0,"state":"start","mode":"ace/mode/python"}},"timestamp":1633064658095,"hash":"6be10c72940899108ac3b768524144a6039fb812"}