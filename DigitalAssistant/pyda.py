import wolframalpha
import wikipedia

while True:
    input = raw_input("Question: ")

    try:
        #wolframalpha
        app_id = ""
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        answer = next(res.results).text
        print answer
    except:
        #wikipedia
        print wikipedia.summary(input)
