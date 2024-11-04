---
title: 使用 Python 向现有 PDF 添加文本
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2021-06-05"
keywords: add text pdf python, write text pdf python
description: 代码示例展示如何使用 PDF 库在 Pdf 文档中添加或写入文本。
---

## 使用 Python 在 PDF 中写入或添加文本

要在 Pdf 文档中添加文本字符串，使用 **Aspose.PDF Java for Python**，只需调用 **AddText** 模块。

```python
doc=self.Document()
doc=self.dataDir + 'input1.pdf'

pdf_page=self.Document()
pdf_page.getPages().get_Item(1)

text_fragment=self.TextFragment("main text")
position=self.Position()
text_fragment.setPosition(position(100,600))

font_repository=self.FontRepository()
color=self.Color()

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))
text_fragment.getTextState().setFontSize(14)

text_builder=self.TextBuilder(pdf_page)
text_builder.appendText(text_fragment)

# 保存 PDF 文件
doc.save(self.dataDir + "Text_Added.pdf")
print "文本添加成功"
```


**下载运行代码**

从以下任何一个社交编码网站下载**添加文本 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)