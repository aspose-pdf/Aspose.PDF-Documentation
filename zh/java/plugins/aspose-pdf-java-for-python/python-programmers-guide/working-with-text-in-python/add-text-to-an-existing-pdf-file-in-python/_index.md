---
title: 使用 Python 向已有 PDF 添加文本
linktitle: 使用 Python 向已有 PDF 添加文本
type: docs
weight: 20
url: /zh/java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2026-10-06"
description: 使用 Python 与 PDF 库在 PDF 文档中添加或写入文本的代码示例。
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

# Save PDF file
doc.save(self.dataDir + "Text_Added.pdf")
print "Text added successfully"
```

**下载运行代码**

下载В **Add Text (Aspose.PDF)**В 来自В 以下提到的任意社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)
