# 自訂函式
import os
import openai
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

openai.api_type = "azure"
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")

def aoai(q):
  msg = ""

  response_az = openai.Completion.create(
  engine="text-davinci-003",
  prompt=q,
  temperature=1,
  max_tokens=300,
  top_p=0.5,
  frequency_penalty=0,
  presence_penalty=0,
  best_of=1,
  stop=None)
  
  msg += (response_az['choices'][0]['text'].strip())


  return msg

q = input('請輸入您想問的事情：')
print(aoai(q))
