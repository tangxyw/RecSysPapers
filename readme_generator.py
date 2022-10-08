"""
    生成README.md
"""

import os
import urllib.request
from datetime import datetime

DIRS = [
    'Rank',
    'Industry',
    'Pre-Rank',
    'Re-Rank',
    'Match',
    'Multi-Task',
    'Multi-Modal',
    'Multi-Scenario',
    'Debias',
    'Calibration',
    'Distillation',
    'Feedback-Delay',
    'ContrastiveLearning',
    'Cold-Start',
    'Learning-to-Rank',
    'Fairness',
    'Look-Alike',
    'CausalInference',
    'Diversity',
    'ABTest',
    'Reinforce',
]
# GITHUB_PATH = "https://github.com/tangxyw/RecSysPapers/blob/main/"
count = 0

readme_file = open("./README.md", 'w')

"""
    论文索引部分
"""


def helper(folder, layer_index):
    """
        深度优先遍历folder中的pdf文件和文件夹，写入Readme.
    Args:
        folder (string): 需要遍历的文件夹路径
        layer_index (int): 文件夹深度索引，决定字体大小

    Returns:
        None
    """
    global count

    file_list = []
    dir_list = []
    for f in os.listdir(folder):
        if os.path.isfile(folder + "/" + f) and f != ".DS_Store":
            file_list.append(f)
        elif os.path.isdir(folder + "/" + f):
            dir_list.append(f)

    # 写入当前文件夹内的pdf
    # 排序, 把已读论文排前面, 剩下的按字母顺序排列
    file_list.sort(key=lambda x: x[1:5] if x[0] == "[" else x[0])
    cur_folder = folder.split("/")[-1]
    readme_file.write("#" * layer_index + " " + cur_folder + "\n")
    for pdf in file_list:
        pdf_url = urllib.request.quote(folder + "/" + pdf)
        pdf = pdf.replace(".pdf", "")
        readme_file.write("-" + " " + "[" + pdf + "]" + "(" + pdf_url + ")" + "\n")
        count += 1

    # 向下递归
    if not dir_list:
        return
    else:
        for dir in dir_list:
            helper(folder + "/" + dir, layer_index + 2)


# 生成目录
# readme_file.write("## 论文目录"+"\n")
for folder in DIRS:
    readme_file.write("-" + " " + "[" + folder + "]" + "(#" + folder + ")" + "\n")

# 生成索引
for folder in DIRS:
    helper(folder, 2)

readme_file.close()

"""
    固定部分 - 中文
"""

today = datetime.now().strftime('%Y-%m-%d')

with open("./README.md", 'r+') as readme_file:
    old_content = readme_file.read()
    desc = """
# 推荐系统相关论文汇总
([English Version is Here]('./README_EN.md'))
## 介绍
1. 截至{}，本仓库收集汇总了推荐系统领域相关论文共**{}**篇，涉及：**召回**，**粗排**，**精排**，**重排**，**多任务**，**多场景**，**多模态**，**冷启动**，**校准**，
**纠偏**，**多样性**，**公平性**，**反馈延迟**，**蒸馏**，**对比学习**，**因果推断**，**Look-Alike**，**Learning-to-Rank**，**强化学习**等领域，本仓库会跟踪业界进展，持续更新。
2. 因文件名特殊字符的限制，故论文title中所有的`:`都改为了`-`，检索时请注意。
3. 文件名前缀中带有`[]`的，表明本人已经通读过，第一个`[]`中为论文年份，第二个`[]`中为发表机构或公司(可选)，第三个`[]`中为论文提出的model或method的简称(可选)。
4. 在某些一级分类下面，还有若干二级分类；一篇论文可能应该涉及多个二级分类(例如用对比学习的方法做召回)，最终我会将论文放在较主要的那一类下；分类也会随时调整优化，欢迎在`issue`中提出宝贵意见。    
5. 若您是文章作者，且不希望您的论文出现在这里，请在`issue`中提出，我核实后会马上下架。
6. 关于排序算法的一些实现，请见我的另一个repo: https://github.com/tangxyw/RecAlgorithm    
7. 本仓库仅供交流学习使用，不做任何商业目的。
    """

    readme_file.seek(0, 0)
    readme_file.write(desc.format(today, count))
    readme_file.write("\n" * 2)
    readme_file.write("## 联系方式")
    readme_file.write("\n")
    readme_file.write("<img src='Wechat.jpeg' alt='pic' width='220' height='220'>")
    readme_file.write("\n" * 2)
    readme_file.write("## 论文目录" + "\n")
    readme_file.write(old_content)

"""
    固定部分 - 英文
"""

with open("./README_EN.md", 'r+') as readme_en_file:
    # old_content = readme_file.read()
    desc = """
# Summary of Papers Related to Recommendation System
## Introduce
1. Up to {}, **{}** papers related to recommendation system have been collected and summarized in this repo, 
including: **Match**, **Pre-Rank**, **Rank**, **Re-Rank**, **Multi-Task**, **Multi-Scenario**, **Multi-Modal**, **Cold-Start**, **Calibration**, 
**Debias**, **Diversity**, **Fairness**, **Feedback-Delay**, **Distillation**, **Contrastive Learning**, **Casual Inference**, 
**Look-Alike**, **Learning-to-Rank**, **ReinForce Learning** and other fields, the repo will track the industry progress and update continuely.
2. Due to the restriction of special characters in the file name, all `:` in the title of the paper are changed to `-`. 
Bring to attention please when searching.
3. If the prefix of the file name contains `[]`, it indicates that I have read it thoroughly. The first `[]` refers to 
the publication year of the paper, the second `[]` refers to the institution or company (optional), and the third `[]` 
refers to the abbreviation of the model or the method proposed in the paper (optional).
4. Below some of the primary categories, there are several secondary categories; 
A paper may involve multiple secondary categories (e.g., Match by Contrastive Learning), and eventually I will put the paper in the main category. 
The classification will be adjusted and optimized at any time, welcome to put forward any opinions in the issue.
5. If you are the author of the article and do not want your paper to exhibit here, please mention it in the issue. 
I will remove it immediately after verification.
6. About some Rank Algorithm implementation, please see another repo of mine: https://github.com/tangxyw/RecAlgorithm.
7. This repo is for exchange and study only, without any commercial purpose.
    """

    readme_en_file.seek(0, 0)
    readme_en_file.write(desc.format(today, count))
    readme_en_file.write("\n" * 2)
    readme_en_file.write("## WeChat")
    readme_en_file.write("\n")
    readme_en_file.write("<img src='Wechat.jpeg' alt='pic' width='220' height='220'>")
    readme_en_file.write("\n" * 2)
    readme_en_file.write("## Catalogue" + "\n")
    readme_en_file.write(old_content)
