import os
import openai
from openai import OpenAI

client = OpenAI()

# 環境変数からAPIキーを読み込む
api_key = os.getenv("OPENAI_API_KEY")

# question.txtファイルから内容を読み込む
with open("question.txt", "r", encoding="utf-8") as file:
    question_content = file.read()

# xmls内のxmlsum.txtファイルから内容を読み込む
with open("xmls/xmlsum.txt", "r", encoding="utf-8") as file:
    xmlsum = file.read()

# Call the GPT-4 API to get the response
response = client.chat.completions.create(
  model = "gpt-4-1106-preview",
  temperature = 0,
  messages = [
    {"role": "system", "content": """
Please respond to the following medical or medical case or clinical question (QUESTION) using the markdown in the format provided, with reference to the article information (ARTICLES). The output should also be in Japanese.
The format is as follows.

---Format---
# Appropriate title
## Summary of QUESTION
Write a summary of the question here.
## Answer to the QUESTION
State your answer to the question, referring to the information in the article. To clarify the scientific facts and evidence, indicate the cited part with numbered brackets so that it is clear from which literature you have brought the information. Later, indicate which literature the information is from in the references. Provide detailed and accurate step-by-step explanations as much as possible. Knowledge should be based on the paper information (ARTICLES).
## References
Indicate the titles of the references used above. Indicate the title only. The list of references should be numbered and correspond to the answers to the questions.
---Format---     
"""},
    {"role": "user", "content": "QUESTIONは以下\n" + question_content + "\n\n" + "論文情報（ARTICLES）は以下\n" + xmlsum},
  ]    
)

# 返ってきたresponseを表示
print("以下は回答のマークダウンです。\n\n" + str(response.choices[0].message.content))

# answer.mdに書き込む
with open("answer.md", "w", encoding="utf-8") as file:
  file.write(str(response.choices[0].message.content))

