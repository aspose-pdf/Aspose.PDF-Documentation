---
title: 在Python中获取PDF文件信息
linktitle: 在Python中获取PDF文件信息
type: docs
weight: 40
url: /java/get-pdf-file-information-in-python/
description: 探索如何使用 Aspose.PDF 进行文档管理，在 Python 中检索详细的 PDF 文件信息，例如元数据和属性。
lastmod: "2026-06-09"
---
要使用 **Aspose.PDF Java for Python** 获取 Pdf 文档的文件信息，只需调用 **GetPdfFileInfo** 类即可。

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

从以下任何一个社交编码网站下载**获取 PDF 文件信息 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
