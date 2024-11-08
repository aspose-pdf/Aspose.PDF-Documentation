---
title: 从 PDF 中移除元数据（使用 Python）
type: docs
weight: 70
url: /zh/java/remove-metadata-from-pdf-in-python/
lastmod: "2021-06-05"
---

要使用 **Aspose.PDF Java for Python** 从 PDF 文档中移除元数据，只需调用 **RemoveMetadata** 类。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# 保存更新后的文档与新信息
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "元数据移除成功，请检查输出文件。"

```

**下载运行代码**

从以下任何一个社交编程网站下载 **Remove Metadata (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)