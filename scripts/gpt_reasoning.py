import openai
import pandas as pd
import json 
import time 
import tqdm
import ast
import random
import argparse
import pdb
from time import sleep
import os 
from utils import  task_list, run_batched_logger, api_base, api_type, api_version

openai.api_base= api_base
openai.api_type = api_type
openai.api_version= api_version
# openai.api_key = openai_key



def attenuator(number_of_failed_hits):
    return 2**(number_of_failed_hits)

            
def construct_prompt(query, task):
    message = [] 
    message.append({"role": "system", "content": task_list[task]})
    message.append({"role": "user", "content": query})
    
    return message 
    
def get_biased_response(prompt):
    number_of_failed_hits = 0
    while number_of_failed_hits < 5:
        try: 
            response = openai.ChatCompletion.create(
            engine = "gpt-35-turbo", 
            temperature=0,
            messages = prompt, 
            max_tokens = 100
            )
            output = response["choices"][0]["message"]['content'].strip().split("\n")[0]
            return output        
        except (openai.error.RateLimitError, openai.error.Timeout) as e:     
            output = 'FAILED'
            number_of_failed_hits += 1
            slugger = attenuator(number_of_failed_hits) 
            print(f'Retrying after {slugger} seconds!')
            sleep(slugger)
        except (openai.error.APIConnectionError,
                openai.error.APIError,
                openai.error.InvalidRequestError,
                TypeError) as e :
            output = f'FAILED with Unrecoverable Exception {e}.'
            break
        except Exception as e:
            output = 'FAILED with generic exception {e}' 
            break
    return output
    

def get_seed_queries(seed_file): 
    with open(seed_file, 'r') as f:
        return f.read().split('\n')    
    

def batched_response(task, queries, sleep_period, batch_size, temperature, response_logger_file):
    batch_iter = 0
    num_of_batches = len(queries)//batch_size
    for batch_idx in range(num_of_batches):
        batch_responses = []
        for query in tqdm.tqdm(queries[batch_iter: batch_iter + batch_size]): 
            time.sleep(sleep_period)
            score = str(id_to_score[query])
            query_txt = f"Text: {id_to_text[query]} Score: {score}"
            prompt = construct_prompt(query_txt, task)
            model_response = get_biased_response(prompt)      
            batch_responses.append(model_response)
        run_batched_logger(task, queries[batch_iter: batch_iter + batch_size], batch_responses, response_logger_file)
        batch_iter += batch_size
        print(f'Processed {batch_idx + 1} batch. Moving on to next!')
    
if __name__ == '__main__': 

    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type = str, default = '../data/model_preds/reason/')
    parser.add_argument('--model', type = str, default = "gpt-35-turbo") # Add a deployment name here
    parser.add_argument('--keypath', type = str)
    parser.add_argument('--sleep_period', type=float, default = 1)
    parser.add_argument('--batch_size', type = int, default = 1)
    parser.add_argument('--max_samples', type=int, default = 500)
    parser.add_argument('--temperature', type=float, default = 0)
    parser.add_argument('--task', type=str, default = 'reasoning')
    parser.add_argument('--queries_file', type=str)
    args = parser.parse_args()

    id_to_text = {}
    id_to_score = {}

    df = pd.read_csv("../data/FSB/FSB_text.csv")
    for index, row in df.iterrows():
        id_to_text[row['uid']] = row['response']

    df = pd.read_csv(args.queries_file)
    for index, row in df.iterrows():
        id_to_score[row['id']] = row[f'{args.model}']

    queries = list(id_to_text.keys())

    ## Initializing openai key and response logging file
    with open(args.keypath, 'r') as file: 
        openai.api_key = file.read().split('\n')[0] # In case there are any useless delimiters
    
    if not os.path.exists(args.root):
        os.makedirs(args.root)
    
    response_logger_file = f'{args.root}{args.model}_reason.txt'
    
    
    batched_response(args.task, queries,  args.sleep_period, args.batch_size, args.temperature, response_logger_file)
