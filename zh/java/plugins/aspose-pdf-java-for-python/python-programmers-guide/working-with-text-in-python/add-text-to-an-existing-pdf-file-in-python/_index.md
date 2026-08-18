---
title: 使用 Python 将文本添加到现有 PDF
linktitle: 使用 Python 将文本添加到现有 PDF
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2026-06-09"
description: 代码示例如何使用 Python 和 PDF 库在 Pdf 文档中添加或写入文本。
---
## 使用 Python 在 PDF 中写入或添加文本

要使用 **Aspose.PDF Java for Python** 在 Pdf 文档中添加文本字符串，只需调用 **AddText** 模块即可。

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

# Save PDF file
doc.save(self.dataDir + "Text_Added.pdf")
print "Text added successfully"
```

**下载运行代码**

从以下任何一个社交编码网站下载**添加文本 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)
