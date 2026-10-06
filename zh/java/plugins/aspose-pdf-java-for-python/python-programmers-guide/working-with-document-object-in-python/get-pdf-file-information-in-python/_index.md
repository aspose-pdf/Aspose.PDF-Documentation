---
title: 在 Python 中获取 PDF 文件信息
linktitle: 在 Python 中获取 PDF 文件信息
type: docs
weight: 40
url: /zh/java/get-pdf-file-information-in-python/
description: 了解如何在 Python 中使用 Aspose.PDF 进行文档管理，以检索详细的 PDF 文件信息，例如元数据和属性。
lastmod: "2026-10-06"
---
要使用 **Aspose.PDF Java for Python** 获取 PDF 文档的文件信息，只需调用 **GetPdfFileInfo** 类。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get document information
doc_info = doc.getInfo();

# Show document information
print "Author:-" + str(doc_info.getAuthor())
print "Creation Date:-" + str(doc_info.getCreationDate())
print "Keywords:-" + str(doc_info.getKeywords())
print "Modify Date:-" + str(doc_info.getModDate())
print "Subject:-" + str(doc_info.getSubject())
print "Title:-" + str(doc_info.getTitle())
```

**下载运行代码**

下载 **获取 PDF 文件信息 (Aspose.PDF)** 来自以下提到的社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
