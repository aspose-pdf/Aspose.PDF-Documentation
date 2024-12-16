---
title: 从 PDF 中移除元数据在 Python 中
type: docs
weight: 70
url: /zh/python-java/remove-metadata-from-pdf-in-python/
---

<ins>要使用 **Aspose.PDF Java for Python** 从 PDF 文档中移除元数据，只需调用 **RemoveMetadata** 类。

**Python 代码**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# 使用新信息保存更新的文档
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "元数据移除成功，请检查输出文件。"
```

**下载运行代码**

从以下任一社交编码网站下载 **Remove Metadata (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)