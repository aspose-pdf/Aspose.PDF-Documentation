---
title: 在 Python 中提取 PDF 文档所有页面的文本
linktitle: 在 Python 中提取 PDF 文档所有页面的文本
type: docs
weight: 30
url: /zh/java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2026-10-06"
description: 解释如何在 Python 中使用 PDF 文件格式 API 提取 PDF 页面中的文本。
---
## 使用 Python 提取 PDF 文本

要使用 **Aspose.PDF Java for Python** 提取 PDF 文档所有页面的文本，只需调用 **ExtractTextFromAllPages** 模块。

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

下载\u0412\u00A0**提取所有页面的文本 (Aspose.PDF)**\u0412\u00A0来自\u0412\u00A0以下任意提到的社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)
