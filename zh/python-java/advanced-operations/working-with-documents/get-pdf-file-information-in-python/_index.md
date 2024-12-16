---
title: 在 Python 中获取 PDF 文件信息
type: docs
weight: 40
url: /zh/python-java/get-pdf-file-information-in-python/
---

<ins>要使用 **Aspose.PDF Java for Python** 获取 PDF 文档的文件信息，只需调用 **GetPdfFileInfo** 类。

**Python 代码**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 获取文档信息
doc_info = doc.getInfo();

# 显示文档信息
print "Author:-" + str(doc_info.getAuthor())
print "Creation Date:-" + str(doc_info.getCreationDate())
print "Keywords:-" + str(doc_info.getKeywords())
print "Modify Date:-" + str(doc_info.getModDate())
print "Subject:-" + str(doc_info.getSubject())
print "Title:-" + str(doc_info.getTitle())
```

**下载运行代码**

从以下任一社交编码网站下载 **获取 PDF 文件信息 (Aspose.PDF)**：


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)