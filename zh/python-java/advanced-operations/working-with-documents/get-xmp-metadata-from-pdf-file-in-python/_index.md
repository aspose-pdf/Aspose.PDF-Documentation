---
title: 从 PDF 文件中获取 XMP 元数据（Python）
type: docs
weight: 50
url: zh/python-java/get-xmp-metadata-from-pdf-file-in-python/
---

<ins>要使用 **Aspose.PDF Java for Python** 从 PDF 文档中获取 XMP 元数据，只需调用 **GetXMPMetadata** 类。

**Python 代码**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 获取属性
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**下载运行代码**

从以下任一社交编码网站下载 **Get XMP Metadata (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)