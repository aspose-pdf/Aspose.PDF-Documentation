---
title: Установить информацию о PDF-файле в Python
linktitle: Установить информацию о PDF-файле в Python
type: docs
weight: 90
url: /java/set-pdf-file-information-in-python/
description: Узнайте, как установить информацию о PDF-файле, такую ​​​​как автор, название и т. д., в Python, используя Aspose.PDF для организации документов.
lastmod: "2026-06-09"
---
Чтобы обновить информацию о документе PDF с помощью **Aspose.PDF Java for Python**, просто вызовите класс **SetPdfFileInfo**.

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

**Загрузить рабочий код**

Загрузите **Установите информацию о PDF-файле (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
