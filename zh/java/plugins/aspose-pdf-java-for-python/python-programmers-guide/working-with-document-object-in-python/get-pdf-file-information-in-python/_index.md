---
title: 在 Python 中获取 PDF 文件信息
type: docs
weight: 40
url: zh/java/get-pdf-file-information-in-python/
lastmod: "2021-06-05"
---

要使用 **Aspose.PDF Java for Python** 获取 PDF 文档的文件信息，只需调用 **GetPdfFileInfo** 类。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 获取文档信息
doc_info = doc.getInfo();

# 显示文档信息
print "作者:-" + str(doc_info.getAuthor())
print "创建日期:-" + str(doc_info.getCreationDate())
print "关键词:-" + str(doc_info.getKeywords())
print "修改日期:-" + str(doc_info.getModDate())
print "主题:-" + str(doc_info.getSubject())
print "标题:-" + str(doc_info.getTitle())
```

**下载运行代码**

从以下任一社交编码网站下载 **获取 PDF 文件信息 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)