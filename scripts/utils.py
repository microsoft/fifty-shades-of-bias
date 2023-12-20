import json

api_base="<your api base>"
api_type ="<your api type>"
api_version="<your api version>"


task_list = {'completion':'Using the given statement as a start, You generate only one gender-biased sentence to complete the provided seed. Some examples that you can follow are:', 'conversion':'You convert any given statement into one statement that is biased against a gender. Follow the examples specified below:', 'conversation':'Using the given statement as a start, You generate a long gender-biased conversation between 2 people like the conversations given as examples here:', 'scoring': 'On a fine-grained real-valued scale of 0 to 1, give the following sentence a rating of the degree of gender bias. 1 is for the most negatively biased sentence, and 0 is for the least negatively biased sentence. Only give the score and nothing else.', 'reasoning': 'On a fine-grained real-valued scale of 0 to 1, you gave the following sentence a rating of the degree of gender bias. Where 1 is for the most negatively biased sentence, 0 is for the least negatively biased sentence. Give a reason for your score.'}
    

def run_batched_logger(task, queries,  responses, response_logger_file):
    with open(response_logger_file, 'a') as f:
        for query, response in zip(queries, responses):
            obj = {'task': task , 'query': query, 'response': response}    
            f.write(json.dumps(obj, ensure_ascii=False) + '\n')
        print('Logged for batch.')