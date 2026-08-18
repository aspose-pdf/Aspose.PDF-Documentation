---
title: 使用 Python 从 PDF 文档的所有页面中提取文本
linktitle: 使用 Python 从 PDF 文档的所有页面中提取文本
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2026-06-09"
description: 解释如何使用 PDF 文件格式 API 在 Python 中从 PDF 页面中提取文本。
---
## 使用 Python 从 PDF 中提取文本

要使用 **Aspose.PDF Java for Python** 提取 TextrFrom All Pages Pdf 文档，只需调用 **ExtractTextFromAllPages** 模块即可。

```python

# Open the target document
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "Text extracted successfully. Check output file."

```

**下载运行代码**

从以下任何一个社交编码网站下载**从所有页面提取文本 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)
