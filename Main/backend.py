from fastapi import FastAPI
import requests
import os
import urllib.request
import requests
from dotenv import load_dotenv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from transformers import PreTrainedTokenizerFast, BartModel, BartForConditionalGeneration
import torch

tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-summarization')
model = BartForConditionalGeneration.from_pretrained('gogamza/kobart-summarization')

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/topic/")
def topic_selection(keyword: str):
    load_dotenv()
    client_id = os.getenv("client_id")
    client_secret = os.getenv("client_secret")
    encText = urllib.parse.quote(f"{keyword}")
    url = "https://openapi.naver.com/v1/search/news?"
    response = requests.get(url,headers={"X-Naver-Client-Id":client_id ,"X-Naver-Client-Secret":client_secret})
    rescode = response.status_code
    text_list=[]
    if(rescode==200):
        response_body = response.json()
        link_list = [x['link'] for x in response_body['items'] if 'naver' in x['link']]
        driver =webdriver.Chrome()
        for link in link_list :
            driver.get(link)
            time.sleep(1)
            article = driver.find_elements(By.CLASS_NAME, "_article_content")
            text = [x.text for x in article][0]
            text = text.replace('\n', ' ')
            raw_input_ids = tokenizer.encode(text)
            input_ids = [tokenizer.bos_token_id] + raw_input_ids + [tokenizer.eos_token_id]
            summary_ids = model.generate(torch.tensor([input_ids]),  num_beams=6,  min_length=24, max_length=256, bos_token_id=0, eos_token_id=1)
            text_list.append(tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True))
        driver.quit()
        return text_list
    else:
        return {"text": "에러가 발생했어요 ㅠ^ㅠ", "Error Code": rescode}
    
@app.get("/summarize/")