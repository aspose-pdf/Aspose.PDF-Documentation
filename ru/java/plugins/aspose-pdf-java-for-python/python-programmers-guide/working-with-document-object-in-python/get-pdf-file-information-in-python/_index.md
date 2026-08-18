---
title: Получить информацию о PDF-файле в Python
linktitle: Получить информацию о PDF-файле в Python
type: docs
weight: 40
url: /java/get-pdf-file-information-in-python/
description: Узнайте, как получить подробную информацию о PDF-файле, такую ​​как метаданные и свойства, в Python, используя Aspose.PDF для управления документами.
lastmod: "2026-06-09"
---
Чтобы получить информацию о файле PDF-документа с помощью **Aspose.PDF Java for Python**, просто вызовите класс **GetPdfFileInfo**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get document information
doc_info = doc.getInfo();

# Show document information
print "Author:-" + str(doc_info.getAuthor())
print "Creation Date:-" + str(doc_info.getCreationDate())
print "Keywords:-" + str(doc_info.getKeywords())
print "Modify Date:-" + str(doc_info.getModDate())
print "Subject:-" + str(doc_info.getSubject())
print "Title:-" + str(doc_info.getTitle())
```

**Загрузить рабочий код**

Загрузите **Получите информацию о PDF-файле (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetPdfFileInfo/GetPdfFileInfo.py)
