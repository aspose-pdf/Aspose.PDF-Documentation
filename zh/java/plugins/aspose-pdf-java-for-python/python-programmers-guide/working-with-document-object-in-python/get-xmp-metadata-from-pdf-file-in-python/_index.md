---
title: 从 PDF 文件获取 XMP 元数据在 Python 中
type: docs
weight: 50
url: zh/java/get-xmp-metadata-from-pdf-file-in-python/
lastmod: "2021-06-05"
---

要使用 **Aspose.PDF Java for Python** 从 Pdf 文档获取 XMP 元数据，只需调用 **GetXMPMetadata** 类。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 获取属性
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**下载运行代码**

从以下任一社交编码网站下载 **获取 XMP 元数据 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)