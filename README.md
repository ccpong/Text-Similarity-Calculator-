# Text-Similarity-Calculator-
It is a simple calculator for calculating the similarity of two text input.

# Function
The calculator support English text and Chinese text in generally.

First, type the first text to the blank of ‘輸入Text1’ in the top of gui.

Next, type the other text to the blank of ‘輸入Text2’ in the middle of gui.

After that, pick the option in the ‘選項’.
Normally, you could pick 預設英文 for english text or 預設中文 for chinese text.

去除空格：If you picked 去除空格, all blankspace in the texts will be removed.
去除大小寫：If you picked 去除大小寫, all letter in the texts will become lowercase.
去除分行：If you picked 去除分行, the texts will become written in one line.
去除標點：If you picked 去除標點, all punctuation in the texts will be removed.

# Intuition
To calculate the similarity of two text input, we can first calculate the disimilarity of two text input.

In this calculator, I use edit-distance to measure the disimilarity of texts.

https://en.wikipedia.org/wiki/Edit_distance

The higher the edit-distance, the lower the similarity.
