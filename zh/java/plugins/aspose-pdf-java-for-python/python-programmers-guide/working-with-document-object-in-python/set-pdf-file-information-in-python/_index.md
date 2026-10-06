---
title: 在 Python 中设置 PDF 文件信息
linktitle: 在 Python 中设置 PDF 文件信息
type: docs
weight: 90
url: /zh/java/set-pdf-file-information-in-python/
description: 了解如何在 Python 中使用 Aspose.PDF 设置 PDF 文件信息，如作者、标题等，以组织文档。
lastmod: "2026-10-06"
---
要使用 **Aspose.PDF Java for Python** 更新 Pdf 文档信息，只需调用 **SetPdfFileInfo** 类。

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

下载В **Set PDF File Information (Aspose.PDF)**В 来自В 以下提到的任何社交代码站点:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
