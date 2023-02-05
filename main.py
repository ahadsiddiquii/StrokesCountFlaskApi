from cjklib.characterlookup import CharacterLookup
from flask import Flask, jsonify, request
import re

app = Flask(__name__)


@app.route('/get_strokes_count', methods=['POST'])
def getStrokesCountFromJson():
    try:
        stroke_count_dict = {}
        char_lookup = CharacterLookup('C')
        print(request)
        requestData = request.json
        print(requestData)
        dictionaryUnsorted = requestData['ListToSort']

        if(len(dictionaryUnsorted) > 0):
            for listItem in dictionaryUnsorted:
                try:
                    # print(listItem)
                    strokeSum = 0
                    if(len(listItem) == 1):
                        strokeSum = char_lookup.getStrokeCount(listItem)
                    else:
                        newWord = listItem
                        res = re.findall(
                            u'([\u4e00-\u9fff0-9a-zA-Z]|(?<=[0-9])[^\u4e00-\u9fff0-9a-zA-Z]+(?=[0-9]))', newWord)
                        # print("Getting substituted word")
                        # print(res)
                        
                        wordBreaking = list(res)
                        if(len(wordBreaking) != 0):
                            print(wordBreaking)
                            for wordBreakItem in wordBreaking:
                                stroke_count = char_lookup.getStrokeCount(
                                    wordBreakItem)
                                strokeSum = stroke_count + strokeSum
                    stroke_count_dict[listItem] = strokeSum
                except Exception as e:
                    print("Loop exception: ")
                    print(e)
                    pass

            print(stroke_count_dict)

        return jsonify({'Error': 0, 'Message': 'Successfully Counted The Strokes',
                        'StrokesMap': stroke_count_dict
                        })

    except Exception as e:
        print(e)
        return jsonify({'Error': 1, 'Message': 'Some Error Occured'})


@app.route('/index')
def index():
    return '<h3>Heroku Deployed</h3>'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
