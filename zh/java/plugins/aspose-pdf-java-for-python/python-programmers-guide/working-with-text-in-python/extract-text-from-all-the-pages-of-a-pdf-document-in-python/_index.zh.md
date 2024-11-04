---
title: 从PDF文档的所有页面提取文本(Python)
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2021-06-05"
keywords: 提取 pdf 文本 python
description: 解释如何使用PDF文件格式API在Python中从PDF页面提取文本。
---

## 使用Python从PDF中提取文本

要使用 **Aspose.PDF Java for Python** 从PDF文档的所有页面提取文本，只需调用 **ExtractTextFromAllPages** 模块。

```python

# 打开目标文档
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "文本提取成功。检查输出文件。"

```

**下载运行代码**

从以下任一社交编码网站下载 **从所有页面提取文本 (Aspose.PDF)**：


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)