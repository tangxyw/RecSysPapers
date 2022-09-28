"""将元信息的`excel`数据转为`json`数据
"""
import json
import pandas as pd
import json

def render_list(s):
    str_list = s.strip("[]").split(",")
    return [ss.strip("' ") for ss in str_list]

if __name__ == "__main__":
    df = pd.read_excel('data.xlsx')
    json_list = df.to_dict(orient="records")
    res = [{
        **paper,
        **{
            "tag": render_list(paper['tag']),
            "authors": [] if pd.isna(paper['authors']) else render_list(paper['authors']),
            "company": "" if pd.isna(paper['company']) else paper['company']
        }} 
        for paper in json_list]
    json.dump(res, open('data.json', "w", encoding="utf-8"))
