#!/bin/python
# ---------------------------------------------------------
# load_data_set.py
#
# David Pelkmann <david.pelkmann@fh-bielefeld.de>
#       Department of Engineering Sciences and Mathematics
#       University of Applied Sciences Bielefeld
#
# 10. February 2020 (dp)
# ---------------------------------------------------------
# Info
# ----
# 
# ---

import pandas as pd
pd.set_option('display.max_colwidth', 15)
import article_stack
from urllib import request
import pickle

# load expert and council data set
df_eac = pd.read_csv("./expert_and_council_data_set.csv", sep=',', index_col=0, skipinitialspace=True) 
# print dataframe infos
print(df_eac.info())
# print first five rows
print(df_eac.head())

stack_expert_a = article_stack.ArticleStack()
stack_expert_b = article_stack.ArticleStack()
stack_expert_c = article_stack.ArticleStack()
stack_council = article_stack.ArticleStack()

print("[info] downloading websites...")

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

for stack, name in [(stack_expert_a, 'a'), (stack_expert_b, 'b'), (stack_expert_c, 'c'), (stack_council, 'council')]:
    for index, row in df_eac.iterrows():
        try:
            html_code = request.urlopen(request.Request(url=row['article_link'], headers=hdr)).read()
        except Exception as e:
            if e == "HTTP Error 404: Not Found":
                html_code = "HTTP Error 404: Not Found"
        if ((row['data_set'] == "expert") and (name == "a")):
            stack.appendArticle(
                article_stack.Article(
                    label = row['label_expert_a'],
                    html_code=html_code
                )
            )
        elif ((row['data_set'] == "expert") and (name == "b")):
            stack.appendArticle(
                article_stack.Article(
                    label = row['label_expert_b'],
                    html_code=html_code
                )
            )
        elif ((row['data_set'] == "expert") and (name == "c")):
            stack.appendArticle(
                article_stack.Article(
                    label = row['label_expert_c'],
                    html_code=html_code
                )
            )
        elif ((row['data_set'] == "council") and (name == "council")):
            stack.appendArticle(
                article_stack.Article(
                    label = row['label_council'],
                    html_code=html_code
                )
            )

print("---------------------")
print("Number of Article:")
print("---------------------")
print("Expert A:\t" + str(stack_expert_a.get_cnt_article()))
print("Expert B:\t" + str(stack_expert_b.get_cnt_article()))
print("Expert C:\t" + str(stack_expert_c.get_cnt_article()))
print("Expert Council:\t" + str(stack_council.get_cnt_article()))
print("---------------------")
print("[info] save stacks in pickle files...")
pickle.dump( stack_expert_a.get_stack(), open( "./expert_a.p", "wb" ))
pickle.dump( stack_expert_b.get_stack(), open( "./expert_b.p", "wb" ))
pickle.dump( stack_expert_c.get_stack(), open( "./expert_c.p", "wb" ))
pickle.dump( stack_council.get_stack(), open( "./expert_council.p", "wb" ))
print("[info] done!")