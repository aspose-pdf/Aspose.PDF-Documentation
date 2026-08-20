---
title: Установить информацию о PDF-файле в Python
linktitle: Установить информацию о PDF-файле в Python
type: docs
weight: 90
url: /ru/java/set-pdf-file-information-in-python/
description: Узнайте, как установить информацию о PDF-файле, такую как автор, заголовок и другое, в Python с помощью Aspose.PDF для организации документов.
lastmod: "2026-08-19"
---
Чтобы обновить информацию документа Pdf, используя **Aspose.PDF Java for Python**, просто вызовите класс **SetPdfFileInfo**.

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

**Скачать работающий код**

СкачатьВ **Установить информацию о PDF файле (Aspose.PDF)**В изВ любой из приведённых ниже социальных сайтов для разработки:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)


