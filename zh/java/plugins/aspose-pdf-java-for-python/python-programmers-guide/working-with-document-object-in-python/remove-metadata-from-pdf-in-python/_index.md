---
title: 使用 Python 从 PDF 中删除元数据
linktitle: 使用 Python 从 PDF 中删除元数据
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-python/
description: 了解如何使用 Aspose.PDF 从 Python 中的 PDF 文档中删除元数据，确保隐私和数据安全。
lastmod: "2026-06-09"
---
要使用 **Aspose.PDF Java for Python** 从 Pdf 文档中删除元数据，只需调用 **RemoveMetadata** 类。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# save update document with new information
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "Removed metadata successfully, please check output file."

```

**下载运行代码**

从以下任何社交编码网站下载**删除元数据 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)
