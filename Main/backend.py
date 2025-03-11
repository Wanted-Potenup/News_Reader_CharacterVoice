from vllm import LLM, SamplingParams
from fastapi import FastAPI, BackgroundTasks
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

# tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-summarization')
# model = BartForConditionalGeneration.from_pretrained('gogamza/kobart-summarization')

model_name = "/home/user/News_Reader_CharacterVoice/llama-hf-format"
llm = LLM(model=model_name, dtype="float16", gpu_memory_utilization=0.95,max_model_len=3072, tokenizer=model_name, tokenizer_mode='auto')

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
    url = "https://openapi.naver.com/v1/search/news?display=10&sort=sim&query=" +encText
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
            text_list.append(text)
            # raw_input_ids = tokenizer.encode(text)
            # input_ids = [tokenizer.bos_token_id] + raw_input_ids + [tokenizer.eos_token_id]
            # summary_ids = model.generate(torch.tensor([input_ids]),  num_beams=6,  min_length=24, max_length=256, bos_token_id=0, eos_token_id=1)
            # text_list.append(tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True))
        driver.quit()
        return text_list
    else:
        return {"text": "에러가 발생했어요 ㅠ^ㅠ", "Error Code": rescode}
    
# @app.get("/summarization/")
# def summarize(text):

    #    prompt = f"""
    #         요약 규칙:
    #         1. {keyword}가 포함된 내용 위주로 요약해주세요.
    #         2. {keyword}가 포함되지 않은 부분은 생략해주세요.
    #         3. 5문장 이하로 요약해주세요.
    #         4. 한 문장당 글자수를 60글자를 넘지 마세요.
    #         5. 중복 문장을 생성하지 마세요.
    #         6. 모르는 부분은 대답하지 마세요.
    #         7. 문장을 생성할 때 구어체로 이어지게 해주세요.
            
    #         다음 문장을 요약해주세요.: 
    #         {article} 

    #         요약:
    #         <|eot_id|>
    #         """
    #     sampling_params = SamplingParams(
    #         temperature=0.4,
    #         top_p=0.7,
    #         max_tokens=384
    #     )

    #     # 텍스트 생성
    #     outputs = llm.generate(prompt, sampling_params=sampling_params)

# @app.get("/voice/")