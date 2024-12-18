---
title: 在 Python 中设置 PDF 文件信息
type: docs
weight: 90
url: /zh/python-java/set-pdf-file-information-in-python/
---

<ins>要使用 **Aspose.PDF Java for Python** 更新 Pdf 文档信息，只需调用 **SetPdfFileInfo** 类。

**Python 代码**
```
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 获取文档信息
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF for java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("PDF 信息");
doc_info.setTitle("设置 PDF 文档信息");

# 保存更新的文档与新信息

doc.save(self.dataDir + "Updated_Information.pdf")
print "更新文档信息，请检查输出文件。"
```

**下载运行代码**

从以下任一社交编码网站下载 **设置 PDF 文件信息 (Aspose.PDF)**：


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)