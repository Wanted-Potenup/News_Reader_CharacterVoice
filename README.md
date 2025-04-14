# 📰 News_Reader_CharacterVoice

"✨나의 최애가 오늘 뉴스를 읽어준다면?"  
AI 캐릭터 음성을 통해, 내가 원하는 주제의 뉴스를 요약해서 들려주는 **맞춤형 뉴스 리더 서비스**입니다.

<img src="https://github.com/user-attachments/assets/2f3cc8b2-3943-45f2-9968-fd209bfd3abe" width='300' height='200'/>
<img src="https://github.com/user-attachments/assets/abdfb70a-c029-44ab-8ccf-559b63f4f3d7" width='300' height='200'/>

---

## 📌 프로젝트 개요

 
**사용자 지정 뉴스 요약 + 캐릭터 음성 TTS**를 결합한 사이드 프로젝트입니다.  

### Duration
2025.02.20~2025.03.05

### Participants & Contact

Shaerrr(HyungHu, Kim)
- 🔗 **Github**: [Shaerrr](https://github.com/Shaerrr)
- LLM - fine tunning, Prompt_engineering, news_data_collect
- FastAPI 

Jiye-han(Jiye, Han)
- 🔗 **Github**: [Jiye-han](https://github.com/Jiye-han)
- voice cloning - fine tunning, coqui
- Streamlit

---

## 🔧 구성 요소

### 🧠 1. 뉴스 요약 LLM
- **모델**: `llama 3.2` 기반 LLM을 뉴스 요약 태스크에 맞춰 `LoRA`로 파인튜닝
- **환경**: `Ubuntu + vLLM` 환경에서 모델 학습 및 추론
- **뉴스 데이터**:  
  - `네이버 뉴스 OpenAPI`를 활용해 최신 기사 수집  
  - `Selenium`으로 뉴스 본문 크롤링하여 원문 확보

### 🗣 2. 캐릭터 음성 합성 (TTS)
- **TTS 엔진**: [`Coqui`](https://coqui.ai/)
- **사용 음성**:
  - 명탐정 코난의 **코난**
  - 최애의 아이 **호시노 아이**
- **방식**: 학습된 캐릭터 음성으로 뉴스 요약 결과를 음성으로 출력

---
## 👩‍💻 기술 스택

| Task | Tech |
|------|------|
| LLM | `Llama 3.1`, `LoRA`, `vLLM` |
| TTS | `Coqui`, 캐릭터 음성 클로닝 |
| 크롤링 | `Naver API`, `Selenium` |
| 운영 환경 | `Ubuntu(Linux)`, `Python` |
| 예정 기능 | `Schedule`, `Keyword-based Filtering`, `DB 캐싱` |

---

## 🗓️ 추후 발전 방안
- **⏰ 스케줄링 기능**:
  - 매일 지정된 시간에 뉴스 자동 크롤링
  - 요약에 최적화된 기사 추출 및 사전 요약 처리
  - 빠른 응답 속도를 위한 DB 캐싱 구조 도입

---

## 🎤 데모 or 스크린샷

![image](https://github.com/user-attachments/assets/b647ba7e-c536-4204-a4f8-260a02008734)
![image](https://github.com/user-attachments/assets/abdfb70a-c029-44ab-8ccf-559b63f4f3d7)


## BaseModel
- [llama-3.2-Korean-Bllossom-3B]  https://huggingface.co/Bllossom/llama-3.2-Korean-Bllossom-3B

-----
## data
- Naver API를 활용한 뉴스수집

-  파인튜닝용 요약 데이터

[daekeun-ml
naver-news-summarization-ko] https://huggingface.co/datasets/daekeun-ml/naver-news-summarization-ko 
  
-----
## Requirement 

python 3.11 ~ 

Linux Ubuntu

torch 2.5.1 , cuda 12.4 

cmake 

vllm 

trl

transformers 

peft

fastapi
