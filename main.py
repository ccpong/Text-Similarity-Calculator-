import tkinter as tk
import math
import re


class compare:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def minDistance(self, word1=None, word2=None):
        if word1 == None:
            word1 = self.word1
        if word2 == None:
            word2 = self.word2
        dp = []
        n = len(word1)
        m = len(word2)
        for i in range(n + 1):
            dp.append([])
            for j in range(m + 1):
                if i == 0 or j == 0:
                    dp[-1].append(max(i, j))
                elif word1[i - 1] == word2[j - 1]:
                    dp[-1].append(dp[i - 1][j - 1])
                else:
                    case1 = dp[i - 1][j - 1] + 1
                    case2 = dp[i][j - 1] + 1
                    case3 = dp[i - 1][j] + 1
                    dp[-1].append(min(case1, case2, case3))
        return dp[-1][-1]

    def noPunctuation(self, e=0):
        if e == 1:
            for p in ['［', '|', '＾', '＿', '＠', '｛', '﹏', '}', '?', '^', '、', '＼', ';', '＜', '〈', '﹔', '”', '｝', '〃',
                      '【', '„', '！', '＞', '~', '《', ':', '=', '】', '{', '；', '…', '>', '』', '!', '〞', '.', '〿', '？',
                      '｡', '＄', '﹑', '〚', '[', '」', '｢', '，', '(', '-', '｠', '“', '：', '～', ')', '#', '—', '‟', '〖',
                      ':wavy_dash:', '。', '〾', '〝', '<', '〔', '–', '－', '〜', '/', '､', '％', ',', '）', ']', "'", '｟',
                      '＝', '＋', '&', '｀', '*', '］', '%', '$', '／', '＃', '〛', '‘', '\u3000', '＇', '‛', ',', '〕', '｜',
                      '+', '·', '`', '（', '＊', '「', '＆', '"', '@', '｣', '『', '_', '〘', '‧', '》', '〉', '〙', '’', '〟',
                      '〗', '＂']:
                self.word1 = self.word1.replace(p, ' ')
                self.word2 = self.word2.replace(p, ' ')
        else:
            for p in ['［', '|', '＾', '＿', '＠', '｛', '﹏', '}', '?', '^', '、', '＼', ';', '＜', '〈', '﹔', '”', '｝', '〃',
                      '【', '„', '！', '＞', '~', '《', ':', '=', '】', '{', '；', '…', '>', '』', '!', '〞', '.', '〿', '？',
                      '｡', '＄', '﹑', '〚', '[', '」', '｢', '，', '(', '-', '｠', '“', '：', '～', ')', '#', '—', '‟', '〖',
                      ':wavy_dash:', '。', '〾', '〝', '<', '〔', '–', '－', '〜', '/', '､', '％', ',', '）', ']', "'", '｟',
                      '＝', '＋', '&', '｀', '*', '］', '%', '$', '／', '＃', '〛', '‘', '\u3000', '＇', '‛', ',', '〕', '｜',
                      '+', '·', '`', '（', '＊', '「', '＆', '"', '@', '｣', '『', '_', '〘', '‧', '》', '〉', '〙', '’', '〟',
                      '〗', '＂']:
                self.word1 = self.word1.replace(p, '')
                self.word2 = self.word2.replace(p, '')

    def noSpace(self):
        self.word1 = ''.join(self.word1.split(' '))
        self.word2 = ''.join(self.word2.split(' '))

    def oneLine(self):
        self.word1 = ''.join(self.word1.split('\n'))
        self.word2 = ''.join(self.word2.split('\n'))

    def lower(self):
        self.word1 = self.word1.lower()
        self.word2 = self.word2.lower()

    def diff(self, correct_word=0, e=0):
        if e == 1:
            w1 = self.word1.split(' ')
            while '' in w1:
                w1.remove('')
            w2 = self.word2.split(' ')
            while '' in w2:
                w2.remove('')
            dis = self.minDistance(w1, w2)
        else:
            w1 = self.word1
            w2 = self.word2
            dis = self.minDistance(w1, w2)
        if correct_word == 0:
            n = max(len(w1), len(w2))
        elif correct_word == 1:
            n = len(w1)
        else:
            n = len(w2)
        if n==0: return 0
        return 1 - dis / n

def compareChinese(word1, word2):
    cp = compare(word1, word2)
    cp.noPunctuation()
    cp.noSpace()
    cp.oneLine()
    return cp.diff()

def compareEnglish(word1, word2):
    cp = compare(word1, word2)
    cp.noPunctuation(e=1)
    cp.oneLine()
    cp.lower()
    return cp.diff(e=1)

def compare_customize(word1, word2, noPunctuation=False, oneLine=False, lower=False, noSpace=False, cutWord=0):
    cp = compare(word1, word2)
    if lower: cp.lower()
    if noSpace: cp.noSpace()
    if oneLine: cp.oneLine()
    #print(list(cp.word1),list(cp.word2),oneLine)
    if noPunctuation and cutWord == 0: cp.noPunctuation(e=cutWord)
    if noPunctuation and cutWord == 1: cp.noPunctuation(e=1)

    return cp.diff(e=cutWord)

window = tk.Tk()
window.title('文字相似度計算器')
window.geometry('700x600')
window.minsize(700, 600)

def calculate():
    text1 = text1_Text.get(1.0,"end-1c")
    text2 = text2_Text.get(1.0,"end-1c")
    value = compare_customize(text1,text2, noPunctuation=noPunctuation.get(), oneLine=oneLine.get(),\
            lower=lower.get(), noSpace=noSpace.get(), cutWord=cutWord.get())
    result = '文字相似度為：{:.4f}'.format(value*100)+'%'
    result_label.configure(text=result)


header_label = tk.Label(window, text='文字相似度計算器')
header_label.pack()
text1_frame = tk.Frame(window)
text1_frame.pack()
text1_label = tk.Label(text1_frame, text='輸入Text1')
text1_label.pack()
text1_Text = tk.Text(text1_frame, width=75, height=12)
text1_Text.pack()

text2_frame = tk.Frame(window)
text2_frame.pack()
text2_label = tk.Label(text2_frame, text='輸入Text2')
text2_label.pack()
text2_Text = tk.Text(text2_frame, width=75, height=12)
text2_Text.pack()


def preset_Chinese():
    noPunctuation.set(True)
    oneLine.set(True)
    lower.set(True)
    noSpace.set(True)
    cutWord.set(0)

def preset_English():
    noPunctuation.set(True)
    oneLine.set(True)
    lower.set(True)
    noSpace.set(False)
    cutWord.set(1)

labelframe1 = tk.LabelFrame(window, text='選項:',padx = 10,pady = 10)
labelframe1.pack()
row1=tk.Frame(labelframe1)
row1.pack()
tk.Button(row1, text="預設中文",command=preset_Chinese).pack(side=tk.LEFT)
tk.Button(row1, text="預設英文",command=preset_English).pack(side=tk.LEFT)
row2=tk.Frame(labelframe1)
row2.pack()
noPunctuation = tk.BooleanVar()
oneLine = tk.BooleanVar()
lower = tk.BooleanVar()
noSpace = tk.BooleanVar()
cutWord = tk.IntVar()
noPunctuation.set(True)
oneLine.set(True)
lower.set(True)
noSpace.set(True)
cutWord.set(0)
C1 = tk.Checkbutton(row2, text="去除標點", var=noPunctuation, onvalue=True, offvalue=False, height=3, width=10)
C2 = tk.Checkbutton(row2, text="去除分行", var=oneLine, onvalue=True, offvalue=False, height=3, width=10)
C3 = tk.Checkbutton(row2, text="去除大小寫", var=lower, onvalue=True, offvalue=False, height=3, width=10)
C4 = tk.Checkbutton(row2, text="去除空格", var=noSpace, onvalue=True, offvalue=False, height=3, width=10)
C1.pack(side=tk.RIGHT)
C2.pack(side=tk.RIGHT)
C3.pack(side=tk.RIGHT)
C4.pack(side=tk.RIGHT)
row3=tk.Frame(labelframe1)
row3.pack()
r3_label = tk.Label(row3, text='分詞風格：')
r3_label.pack(side=tk.LEFT)
r3b1 = tk.Radiobutton(row3, text="按字元分隔", variable=cutWord, value=0).pack(side=tk.LEFT)
r3b2 = tk.Radiobutton(row3, text="以空格分隔", variable=cutWord, value=1).pack(side=tk.LEFT)




result_label = tk.Label(window,height=2)
result_label.pack()

calculate_btn = tk.Button(window, text='馬上計算', command=calculate)
calculate_btn.pack()

window.mainloop()