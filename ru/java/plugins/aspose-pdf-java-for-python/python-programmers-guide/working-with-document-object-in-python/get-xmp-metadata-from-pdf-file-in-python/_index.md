---
title: Получить XMP‑метаданные из PDF‑файла в Python
linktitle: Получить XMP‑метаданные из PDF‑файла в Python
type: docs
weight: 50
url: /ru/java/get-xmp-metadata-from-pdf-file-in-python/
description: Узнайте, как получить XMP‑метаданные из PDF‑файла в Python с использованием Aspose.PDF, позволяя выполнять детальный анализ содержимого.
lastmod: "2026-08-19"
---
Чтобы получить XMP‑метаданные из Pdf документа с помощью **Aspose.PDF Java for Python**, просто вызовите класс **GetXMPMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get properties
print "xmp:CreateDate: " + str(doc.getMetadata().get_Item("xmp:CreateDate"))
print "xmp:Nickname: " + str(doc.getMetadata().get_Item("xmp:Nickname"))
print "xmp:CustomProperty: " + str(doc.getMetadata().get_Item("xmp:CustomProperty"))
```

**Загрузить исполняемый код**

СкачатьВ **Get XMP Metadata (Aspose.PDF)**В изВ любого из перечисленных ниже сайтов для совместного кодирования:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/GetXMPMetadata/GetXMPMetadata.py)


