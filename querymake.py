import os
import openai
from openai import OpenAI

client = OpenAI()

# 環境変数からAPIキーを読み込む
api_key = os.getenv("OPENAI_API_KEY")

# question.txtファイルから内容を読み込む
with open("question.txt", "r", encoding="utf-8") as file:
    question_content = file.read()

# question.txtファイルの内容を表示
print("以下について調べます。\n\n" + question_content)

# Call the GPT-4 API to get the response
response = client.chat.completions.create(
  model = "gpt-4-1106-preview",
  temperature = 0,
  messages = [
    {"role": "system", "content": "Output only the search query for pubmed. Below is a medical or medical case or clinical question. I would like to search pubmed for primary information needed to solve or discuss the problem about the above. Please think of the best English search query and output it. Please use AND and OR searches as appropriate. Use a general scientific vocabulary that could be used as a search query in pubmed. To obtain as many search results as possible, minimize AND searches and use OR searches as the main search method. Output only the search query for pubmed."},
    {"role": "user", "content": question_content },
  ]    
)

# queryを表示
print("以下はpubmed向けの検索クエリです。\n\n" + str(response.choices[0].message.content))

# Write the response to query.txt
with open("query.txt", "w", encoding="utf-8") as file:
  file.write(str(response.choices[0].message.content))