#Text compare algorithm
from head import *
def getText(wordname):
    d = Document(wordname)
    texts = []
    for para in d.paragraphs:
        texts.append(para.text)
    return texts

def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

def msplit(s, seperators=',|\.|\?|，|。|？|！'):
    return re.split(seperators, s)

def readDocx(docfile):
    # print('*' * 80)
    # print('文件', docfile, '加载中……')
    paras = getText(docfile)
    segs = []
    for p in paras:
        temp = []
        for s in msplit(p):
            if len(s) > 2:
                temp.append(s.replace(' ', ""))
        if len(temp) > 0:
            segs.append(temp)
    showInfo(segs, docfile)
    return segs

def showInfo(doc, filename='filename'):
    chars = 0
    segs = 0
    for p in doc:
        for s in p:
            segs = segs + 1
            chars = chars + len(s)
    # print('段落数: {0:>8d} 个。'.format(len(doc)))
    # print('短句数: {0:>8d} 句。'.format(segs))
    # print('字符数: {0:>8d} 个。'.format(chars))

def compareParagraph(doc1, i, doc2, j, min_segment=5):
    """
    功能为比较两个段落的相似度，返回结果为两个段落中相同字符的长度与较短段落长度的比值。
    :param p1: 行
    :param p2: 列
    :param min_segment = 5: 最小段的长度
    """
    p1 = doc1[i]
    p2 = doc2[j]
    len1 = sum([len(s) for s in p1])
    len2 = sum([len(s) for s in p2])
    if len1 < 10 or len2 < 10:
        return ([], 0)
    list = []
    for s1 in p1:
        if len(s1) < min_segment:
            continue
        for s2 in p2:
            if len(s2) < min_segment:
                continue
            if s2 in s1:
                list.append(s2)
            elif s1 in s2:
                list.append(s1)

    # 取两个字符串的最短的一个进行比值计算
    count = sum([len(s) for s in list])
    # ratio = float(count) / min(len1, len2)
    # if count > 10 and ratio > 0.1:
    #     print(' 发现相同内容 '.center(80, '*'))
    #     print('文件1第{0:0>4d}段内容：{1}'.format(i + 1, p1))
    #     print('文件2第{0:0>4d}段内容：{1}'.format(j + 1, p2))
    #     print('相同内容：', list)
    # print('相同字符比：{1:.2f}%\n相同字符数： {0}\n'.format(count, ratio * 100))
    return (list, count)