import os
import xml.etree.ElementTree as ET

# XMLファイルが格納されているフォルダのパス
xml_folder_path = 'xmls'
# 出力するテキストファイルのパス
output_file_path = os.path.join(xml_folder_path, 'xmlsum.txt')

# 出力ファイルを開く
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    # フォルダ内のすべてのXMLファイルを処理する
    for i, xml_file in enumerate(os.listdir(xml_folder_path), start=1):
        if xml_file.endswith('.xml'):
            # XMLファイルのフルパスを取得
            xml_file_path = os.path.join(xml_folder_path, xml_file)
            # XMLファイルを解析
            tree = ET.parse(xml_file_path)
            root = tree.getroot()
            
            # 論文のタイトルを取得
            title = root.find('.//ArticleTitle').text
            # 発行年度を取得
            year = root.find('.//PubDate/Year').text if root.find('.//PubDate/Year') is not None else '0000'
            month = root.find('.//PubDate/Month').text if root.find('.//PubDate/Month') is not None else '00'
            day = root.find('.//PubDate/Day').text if root.find('.//PubDate/Day') is not None else '00'
            publishing_year = f'{year}-{month}-{day}'
            # 著者情報を取得
            authors = root.findall('.//AuthorList/Author')
            author_names = ', '.join([f"{author.find('LastName').text}, {author.find('ForeName').text}" if author.find('LastName') is not None and author.find('ForeName') is not None else "Author name not available" for author in authors])
            # アブストラクトを取得
            abstract = root.find('.//AbstractText').text if root.find('.//AbstractText') is not None else 'No abstract available'
            
            # テキストファイルに書き込む
            output_file.write(f'article{i:03d}\n')
            output_file.write(f'{title}\n')
            output_file.write(f'{publishing_year}\n')
            output_file.write(f'{author_names}\n')
            output_file.write(f'{abstract}\n\n')