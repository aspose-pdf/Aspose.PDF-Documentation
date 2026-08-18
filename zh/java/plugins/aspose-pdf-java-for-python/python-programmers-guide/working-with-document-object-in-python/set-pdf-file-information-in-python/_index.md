---
title: 在Python中设置PDF文件信息
linktitle: 在Python中设置PDF文件信息
type: docs
weight: 90
url: /java/set-pdf-file-information-in-python/
description: 了解如何使用 Aspose.PDF 在 Python 中设置 PDF 文件信息（例如作者、标题等）来组织文档。
lastmod: "2026-06-09"
---
要使用 **Aspose.PDF Java for Python** 更新 Pdf 文档信息，只需调用 **SetPdfFileInfo** 类即可。

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get document information
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF for java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("PDF Information");
doc_info.setTitle("Setting PDF Document Information");

# save update document with new information

doc.save(self.dataDir + "Updated_Information.pdf")
print "Update document information, please check output file."
```

**下载运行代码**

从以下任何一个社交编码网站下载**设置 PDF 文件信息 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
