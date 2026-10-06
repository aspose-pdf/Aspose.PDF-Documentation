---
title: 在 Python 中合并 PDF 文件
linktitle: 在 Python 中合并 PDF 文件
type: docs
weight: 10
url: /zh/java/concatenate-pdf-files-in-python/
description: 了解如何在 Python 中使用 Aspose.PDF 将多个 PDF 文件合并为单个 PDF 文档，从而简化文档管理。
lastmod: "2026-10-06"
---
使用 **Aspose.PDF Java for Python** 合并 PDF 文件，只需调用 **ConcatenatePdfFiles** 类。

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

下载\u0412\u00A0**Concatenate PDF Files (Aspose.PDF)**\u0412\u00A0来自\u0412\u00A0以下提到的任何社交代码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)
