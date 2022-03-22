import wolframalpha
import csv
import keys

client = wolframalpha.Client(keys.API_KEY)

question = input('What is your question?\n')


def get_res():

    res = client.query(question)
    result = next(res.results).text
    print(result)
    return result


def store_request():
    header = ['question', 'response']
    info = [question, response]
    
    with open('data.csv', 'w', newline='') as file:
        spamwriter = csv.writer(file)
        spamwriter.writerow(header)
        spamwriter.writerow(info)
        

response = get_res()

store_request()