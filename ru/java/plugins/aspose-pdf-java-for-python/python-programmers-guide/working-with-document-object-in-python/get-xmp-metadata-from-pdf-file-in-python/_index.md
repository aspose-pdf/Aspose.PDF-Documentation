---
title: Получить метаданные XMP из PDF-файла в Python
linktitle: Получить метаданные XMP из PDF-файла в Python
type: docs
weight: 50
url: /java/get-xmp-metadata-from-pdf-file-in-python/
description: Узнайте, как получить метаданные XMP из файла PDF в Python с помощью Aspose.PDF, что позволяет проводить детальный анализ контента.
lastmod: "2026-06-09"
---
Чтобы получить метаданные XMP из документа PDF с помощью **Aspose.PDF Java for Python**, просто вызовите класс **GetXMPMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get properties
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**Загрузить рабочий код**

Загрузите **Получите метаданные XMP (Aspose.PDF)** с любого из перечисленных ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)
