---
title: 在 Python 中连接 PDF 文件
linktitle: 在 Python 中连接 PDF 文件
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-python/
description: 了解如何使用 Aspose.PDF 在 Python 中将多个 PDF 文件连接成单个 PDF 文档，从而简化文档管理。
lastmod: "2026-06-09"
---
要使用 **Aspose.PDF Java for Python** 连接 PDF 文件，只需调用 **ConcatenatePdfFiles** 类。

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Open the source document
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# Add the pages of the source document to the target document
pdf1.getPages().add(pdf1.getPages())

# Save the concatenated output file (the target document)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "New document has been saved, please check the output file"
```

**下载运行代码**

从以下任何社交编码网站下载**连接 PDF 文件 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)
