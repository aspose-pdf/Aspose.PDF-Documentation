---
title: 在 Python 中删除 PDF 元数据
linktitle: 在 Python 中删除 PDF 元数据
type: docs
weight: 70
url: /zh/java/remove-metadata-from-pdf-in-python/
description: 了解如何在 Python 中使用 Aspose.PDF 删除 PDF 文档的元数据，确保隐私和数据安全。
lastmod: "2026-10-06"
---
要使用 **Aspose.PDF Java for Python** 删除 PDF 文档的元数据，只需调用 **RemoveMetadata** 类。

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

下载 **Remove Metadata (Aspose.PDF)** 来自以下提到的任意社交代码托管站点:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)
