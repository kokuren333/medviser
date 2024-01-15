# medviser 知りたい医学情報をソース付きで取得
## 使い方
question.txtに知りたい医学・医療の内容を書き込んで、querymake.py、xmlget.py、xml2txt.py、medsum.pyの順に実行してください。  
必要なライブラリは1.00以上のopenaiとrequests、OpenAIのapikeyはosの環境変数から読み取るようになっています。  
## 結果の例
## question.txt
癌を予防する食事や、リスクを高める食生活などについて知りたい。どんな食材や食生活がどんな影響を及ぼすのかを知りたい。
## answer.md
# 癌予防と食事
## QUESTIONの要約
癌を予防する食事や、リスクを高める食生活についての影響を知りたい。

## QUESTIONへの回答
癌の予防には、健康的な食生活が重要です。特に、植物性食品（豆類、全粒穀物、野菜、果物）を豊富に含む食事が推奨されています[1]。アルコールや加工肉の摂取は癌のリスクを高める可能性がありますが、食物繊維は大腸癌の予防に有効です[1]。フラボノイドを含む食品の摂取は、癌を含む慢性疾患のリスクを減少させるとされています[3]。また、地中海食は代謝症候群、癌、長寿に対する保護効果があるとされています[5]。

口腔癌に関しては、果物や野菜、クルクミン、緑茶がリスクを減少させる一方で、赤肉や揚げ物などのプロ炎症性食品はリスクを高めるとされています[6]。肝癌のリスクに関しては、アフラトキシンの暴露、過度のアルコール摂取、および一部の乳製品（ヨーグルトを除く）がリスクを増加させる可能性があり、コーヒー、魚、お茶、適度なアルコール摂取、およびいくつかの健康的な食生活パターンがリスクを減少させる可能性があります[7]。

地中海食に対する高い遵守度は、全体的な癌死亡リスクを低下させると関連しています[8]。乳癌に関しては、未精製穀物、野菜、果物、ナッツ、オリーブオイルを多く含み、飽和脂肪酸や赤肉の摂取を控えた健康的な食生活パターンが、診断後の全体的な生存率を改善する可能性があります[9]。

断食やカロリー制限は、癌の予防と治療において有益な効果を示す可能性がありますが、慢性的なカロリー制限は利点と欠点があり、実践する上での課題もあります[10]。プロステート癌に関しては、脂肪、タンパク質、炭水化物、ビタミン（A、D、E）、ポリフェノールなどの栄養素が、炎症、抗酸化作用、性ホルモンの作用を通じてPCaの発症と進行に影響を与える可能性があります[14]。

大腸癌においては、食物繊維、カルシウム、ビタミンD、セレンなどの特定の栄養素が保護効果を持つとされています[15][20]。また、食事による腸内細菌叢の変化は、癌の発症に影響を与える可能性があります[20]。

## 参考文献
1. Nutrition and cancer: prevention and survival.
2. The World Cancer Research Fund/American Institute for Cancer Research Third Expert Report on Diet, Nutrition, Physical Activity, and Cancer: Impact and Future Directions.
3. Flavonoids--food sources and health benefits.
4. Dietary Natural Products for Prevention and Treatment of Liver Cancer.
5. Impact of Mediterranean diet on metabolic syndrome, cancer and longevity.
6. Association between Oral Cancer and Diet: An Update.
7. Diet and liver cancer risk: a narrative review of epidemiological evidence.
8. Adherence to Mediterranean Diet and Risk of Cancer: An Updated Systematic Review and Meta-Analysis.
9. Nutrition and Breast Cancer: A Literature Review on Prevention, Treatment and Recurrence.
10. Fasting and Caloric Restriction in Cancer Prevention and Treatment.
11. [Nutrition and cancer].
12. Dietary patterns and cancer risk.
13. Diet-microbiome interactions in cancer treatment: Opportunities and challenges for precision nutrition in cancer.
14. Influence of Diet and Nutrition on Prostate Cancer.
15. Nutrients, foods, and colorectal cancer prevention.
16. Breast Cancer Primary Prevention and Diet: An Umbrella Review.
17. Diet and carcinogenesis of gastric cancer.
18. Diet, menopause and the risk of ovarian, endometrial and breast cancer.
19. The Role of Diet and Nutrition in Cancer: Prevention, Treatment, and Survival.
20. Dietary Factors Modulating Colorectal Carcinogenesis.
