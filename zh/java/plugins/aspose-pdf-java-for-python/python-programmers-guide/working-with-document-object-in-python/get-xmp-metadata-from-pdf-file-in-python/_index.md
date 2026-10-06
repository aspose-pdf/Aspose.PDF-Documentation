---
title: 在 Python 中获取 PDF 文件的 XMP 元数据
linktitle: 在 Python 中获取 PDF 文件的 XMP 元数据
type: docs
weight: 50
url: /zh/java/get-xmp-metadata-from-pdf-file-in-python/
description: 了解如何使用 Aspose.PDF 在 Python 中检索 PDF 文件的 XMP 元数据，从而实现详细的内容分析。
lastmod: "2026-10-06"
---
要使用 **Aspose.PDF Java for Python** 从 Pdf 文档获取 XMP 元数据，只需调用 **GetXMPMetadata** 类。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get properties
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**下载运行代码**

DownloadВ **获取 XMP 元数据 (Aspose.PDF)**В 来自В 以下提到的任何社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)
