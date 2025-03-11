# News_Reader_CharacterVoice
-----------
## Overview
 """최애가 읽어주는 오늘의 뉴스! """ 
 
 '출퇴근길 최애가 내가 좋아하는 관심사를 정리해서 들려준다!'
 
 이러한 서비스의 프로토타입 입니다.

-----------
## BaseModel
- [llama-3.2-Korean-Bllossom-3B]  https://huggingface.co/Bllossom/llama-3.2-Korean-Bllossom-3B

-----
## data
- Naver API를 활용한 뉴스수집 
- [daekeun-ml
/
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

-----
## Participants & Contact

Shaerrr(HyungHu, Kim)
- llama : fine tunned
- 
