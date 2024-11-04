---
title: 在 Python 中向现有 PDF 文件添加文本
type: docs
weight: 20
url: /python-java/add-text-to-an-existing-pdf-file-in-python/
---

要在 Pdf 文档中使用 **Aspose.PDF Java for Python** 添加文本字符串，只需调用 **AddText** 模块。

```python
doc=self.Document()
doc=self.dataDir + 'input1.pdf'

pdf_page=self.Document()
pdf_page.getPages().get_Item(1)

text_fragment=self.TextFragment("主要文本")
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

从以下任何一个社交编程网站下载 **Add Text (Aspose.PDF)**：


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)