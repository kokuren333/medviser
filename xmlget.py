import os
import time
import requests
from xml.etree import ElementTree

# NCBIのAPIエンドポイント
NCBI_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

# XMLを保存するディレクトリ名
XML_DIR = "xmls"

# query.txtから検索クエリを読み込む
with open("query.txt", "r", encoding="utf-8") as file:
    search_query = file.read()

# xmlsディレクトリが存在しない場合は作成する
if not os.path.exists(XML_DIR):
    os.makedirs(XML_DIR)
else:
    # ディレクトリが存在する場合は中身を削除する
    for file_name in os.listdir(XML_DIR):
        file_path = os.path.join(XML_DIR, file_name)
        if os.path.isfile(file_path):
            os.unlink(file_path)

# 検索クエリを使ってPubMedで検索し、関連度順に上位20件のPMIDを取得する
search_url = f"{NCBI_API_URL}esearch.fcgi?db=pubmed&term={search_query}&retmax=20&usehistory=y&sort=relevance"
search_response = requests.get(search_url)
search_tree = ElementTree.fromstring(search_response.content)
id_list = [id_tag.text for id_tag in search_tree.findall("IdList/Id")]


# PMIDごとにXMLを取得し、ファイルに保存する
for idx, pmid in enumerate(id_list):
    # 秒間3アクセスを超えないようにするための遅延
    time.sleep(1/3)
    
    # XMLを取得する
    fetch_url = f"{NCBI_API_URL}efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
    fetch_response = requests.get(fetch_url)
    
    # XMLをファイルに保存する
    file_path = os.path.join(XML_DIR, f"article_{idx+1}.xml")
    with open(file_path, 'wb') as file:
        file.write(fetch_response.content)

# 完了メッセージを表示
print("XMLファイルの取得が完了しました。")